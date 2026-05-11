// ==UserScript==
// @name         OpenCode Voice Input
// @namespace    https://knssnr.local
// @version      1.0
// @description  Add microphone button to OpenCode for voice-to-text via local Whisper
// @match        http://192.168.178.68:39023/*
// @match        http://localhost:39023/*
// @match        http://127.0.0.1:39023/*
// @grant        none
// ==/UserScript==

(function () {
  'use strict';

  const WHISPER_URL = 'http://127.0.0.1:7788/transcribe';
  let mediaRecorder = null;
  let audioChunks   = [];
  let micBtn        = null;

  function setButtonState(state) {
    if (!micBtn) return;
    const labels = { idle: '🎤', recording: '⏹', processing: '⏳' };
    const colors  = { idle: '#1a1a2e', recording: '#c0392b', processing: '#8e44ad' };
    const borders = { idle: '#555',    recording: '#e74c3c',  processing: '#9b59b6' };
    micBtn.textContent         = labels[state];
    micBtn.style.background    = colors[state];
    micBtn.style.border        = `2px solid ${borders[state]}`;
    micBtn.style.animation     = state === 'recording' ? 'oc-pulse 1s infinite' : '';
    micBtn.title = state === 'recording' ? 'Stop recording' : 'Voice input';
  }

  function createMicButton() {
    const btn = document.createElement('button');
    btn.id        = 'oc-mic-btn';
    btn.textContent = '🎤';
    btn.title     = 'Voice input (click to record, click again to stop)';
    Object.assign(btn.style, {
      position:     'fixed',
      bottom:       '80px',
      right:        '20px',
      zIndex:       '9999',
      width:        '48px',
      height:       '48px',
      borderRadius: '50%',
      border:       '2px solid #555',
      background:   '#1a1a2e',
      color:        '#fff',
      fontSize:     '20px',
      cursor:       'pointer',
      boxShadow:    '0 2px 8px rgba(0,0,0,0.4)',
      transition:   'all 0.2s',
    });
    btn.addEventListener('click', toggleRecording);
    document.body.appendChild(btn);
    return btn;
  }

  async function toggleRecording() {
    if (mediaRecorder && mediaRecorder.state === 'recording') {
      mediaRecorder.stop();
      return;
    }

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      audioChunks  = [];
      const mimeType = MediaRecorder.isTypeSupported('audio/webm;codecs=opus')
        ? 'audio/webm;codecs=opus' : 'audio/webm';
      mediaRecorder = new MediaRecorder(stream, { mimeType });

      mediaRecorder.ondataavailable = e => { if (e.data.size > 0) audioChunks.push(e.data); };
      mediaRecorder.onstop = async () => {
        stream.getTracks().forEach(t => t.stop());
        setButtonState('processing');
        const blob = new Blob(audioChunks, { type: mimeType });
        await sendToWhisper(blob);
      };

      mediaRecorder.start();
      setButtonState('recording');
    } catch (err) {
      alert('Microphone access denied: ' + err.message);
    }
  }

  async function sendToWhisper(blob) {
    try {
      const form = new FormData();
      form.append('audio', blob, 'audio.webm');
      const res  = await fetch(WHISPER_URL, { method: 'POST', body: form });
      const data = await res.json();
      if (data.text) insertText(data.text);
      else showToast('⚠️ ' + (data.error || 'Empty transcript'));
    } catch (err) {
      showToast('⚠️ Whisper server unreachable: ' + err.message);
    } finally {
      setButtonState('idle');
    }
  }

  function insertText(text) {
    const selectors = [
      'textarea[placeholder*="message" i]',
      'textarea[placeholder*="ask" i]',
      'textarea[placeholder*="type" i]',
      '[contenteditable="true"]',
      'textarea',
    ];
    let input = null;
    for (const sel of selectors) {
      input = document.querySelector(sel);
      if (input) break;
    }

    if (!input) {
      navigator.clipboard.writeText(text).then(() =>
        showToast('🎤 Copied to clipboard: "' + text.slice(0, 60) + '"')
      );
      return;
    }

    if (input.tagName === 'TEXTAREA' || input.tagName === 'INPUT') {
      const start = input.selectionStart ?? input.value.length;
      const prefix = input.value && !input.value.endsWith(' ') ? ' ' : '';
      input.value = input.value.slice(0, start) + prefix + text + input.value.slice(input.selectionEnd ?? start);
      input.selectionStart = input.selectionEnd = start + prefix.length + text.length;
      input.dispatchEvent(new Event('input', { bubbles: true }));
    } else {
      input.focus();
      document.execCommand('insertText', false, text);
    }
    input.focus();
    showToast('🎤 "' + text.slice(0, 60) + (text.length > 60 ? '…' : '') + '"');
  }

  function showToast(msg) {
    const t = document.createElement('div');
    t.textContent = msg;
    Object.assign(t.style, {
      position: 'fixed', bottom: '140px', right: '20px', zIndex: '10000',
      background: '#2d2d2d', color: '#eee', padding: '8px 14px',
      borderRadius: '8px', fontSize: '13px', maxWidth: '300px',
      boxShadow: '0 2px 8px rgba(0,0,0,0.4)', whiteSpace: 'pre-wrap',
      transition: 'opacity 0.5s',
    });
    document.body.appendChild(t);
    setTimeout(() => { t.style.opacity = '0'; setTimeout(() => t.remove(), 500); }, 3000);
  }

  const style = document.createElement('style');
  style.textContent = '@keyframes oc-pulse { 0%,100%{box-shadow:0 0 0 0 rgba(231,76,60,0.5)} 50%{box-shadow:0 0 0 8px rgba(231,76,60,0)} }';
  document.head.appendChild(style);

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => { micBtn = createMicButton(); });
  } else {
    micBtn = createMicButton();
  }
})();
