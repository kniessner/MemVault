#!/usr/bin/env node
// whisper-server.js — local HTTP transcription endpoint for OpenCode voice input
// POST /transcribe with multipart audio → returns { text: "..." }

const http  = require("http");
const fs    = require("fs");
const path  = require("path");
const os    = require("os");
const { spawnSync } = require("child_process");

const PORT        = 7788;
const PYTHON_BIN  = process.env.WHISPER_PYTHON || `${os.homedir()}/.venv-whisper/bin/python3`;
const SCRIPT      = path.join(__dirname, "../telegram-claude/transcribe.py");
const MODEL       = process.env.WHISPER_MODEL || "base";

function transcribeLocal(audioPath) {
  if (!fs.existsSync(PYTHON_BIN)) throw new Error(`Python not found: ${PYTHON_BIN}`);
  const r = spawnSync(PYTHON_BIN, [SCRIPT, audioPath, MODEL],
    { encoding: "utf8", timeout: 60000, maxBuffer: 1024 * 1024 });
  if (r.status !== 0) throw new Error(r.stderr?.slice(0, 300) || "Whisper failed");
  return r.stdout.trim();
}

async function transcribeOpenAI(audioPath) {
  const https  = require("https");
  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) throw new Error("OPENAI_API_KEY not set");
  const fileData = fs.readFileSync(audioPath);
  const boundary = `----WsBoundary${Date.now()}`;
  const body = Buffer.concat([
    Buffer.from(`--${boundary}\r\nContent-Disposition: form-data; name="model"\r\n\r\nwhisper-1\r\n`),
    Buffer.from(`--${boundary}\r\nContent-Disposition: form-data; name="file"; filename="audio.webm"\r\nContent-Type: audio/webm\r\n\r\n`),
    fileData,
    Buffer.from(`\r\n--${boundary}--\r\n`),
  ]);
  return new Promise((resolve, reject) => {
    const req = https.request({
      hostname: "api.openai.com", path: "/v1/audio/transcriptions", method: "POST",
      headers: { "Authorization": `Bearer ${apiKey}`, "Content-Type": `multipart/form-data; boundary=${boundary}`, "Content-Length": body.length },
    }, (res) => {
      let raw = ""; res.on("data", c => raw += c);
      res.on("end", () => { try { resolve(JSON.parse(raw).text || ""); } catch { reject(new Error(raw.slice(0,200))); } });
    });
    req.on("error", reject); req.write(body); req.end();
  });
}

function parseMultipart(body, boundary) {
  const parts = [];
  const sep = Buffer.from(`--${boundary}`);
  let start = 0;
  while (start < body.length) {
    const idx = body.indexOf(sep, start);
    if (idx === -1) break;
    start = idx + sep.length;
    if (body[start] === 45 && body[start + 1] === 45) break; // --
    start += 2; // skip \r\n
    const headerEnd = body.indexOf(Buffer.from("\r\n\r\n"), start);
    if (headerEnd === -1) break;
    const headers = body.slice(start, headerEnd).toString();
    const dataStart = headerEnd + 4;
    const nextSep = body.indexOf(sep, dataStart);
    const dataEnd = nextSep === -1 ? body.length : nextSep - 2;
    parts.push({ headers, data: body.slice(dataStart, dataEnd) });
    start = nextSep === -1 ? body.length : nextSep;
  }
  return parts;
}

const server = http.createServer(async (req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Headers", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, GET, OPTIONS");

  if (req.method === "OPTIONS") { res.writeHead(204); return res.end(); }
  if (req.method === "GET" && req.url === "/health") {
    res.writeHead(200, { "Content-Type": "application/json" });
    return res.end(JSON.stringify({ ok: true, model: MODEL, python: PYTHON_BIN }));
  }
  if (req.method !== "POST" || req.url !== "/transcribe") {
    res.writeHead(404); return res.end("Not found");
  }

  const chunks = [];
  req.on("data", c => chunks.push(c));
  req.on("end", async () => {
    const body = Buffer.concat(chunks);
    const ct   = req.headers["content-type"] || "";
    const boundaryMatch = ct.match(/boundary=(.+)/);
    if (!boundaryMatch) {
      res.writeHead(400); return res.end("No boundary");
    }
    const boundary = boundaryMatch[1];
    const parts    = parseMultipart(body, boundary);
    const audioPart = parts.find(p => p.headers.includes('name="audio"'));
    if (!audioPart) {
      res.writeHead(400); return res.end("No audio part");
    }

    const ext = audioPart.headers.includes("webm") ? ".webm"
              : audioPart.headers.includes("ogg")  ? ".ogg"
              : audioPart.headers.includes("mp4")  ? ".mp4" : ".webm";
    const tmpFile = path.join(os.tmpdir(), `oc-voice-${Date.now()}${ext}`);
    fs.writeFileSync(tmpFile, audioPart.data);

    try {
      let text;
      if (fs.existsSync(PYTHON_BIN)) {
        text = transcribeLocal(tmpFile);
      } else {
        text = await transcribeOpenAI(tmpFile);
      }
      console.log(`[${new Date().toISOString()}] 🎤 "${text.slice(0, 80)}"`);
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ text }));
    } catch (err) {
      console.error("Transcription error:", err.message);
      res.writeHead(500, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: err.message }));
    } finally {
      fs.unlink(tmpFile, () => {});
    }
  });
});

server.listen(PORT, "127.0.0.1", () => {
  console.log(`🎤 Whisper server running at http://127.0.0.1:${PORT}`);
  console.log(`   Python: ${PYTHON_BIN}`);
  console.log(`   Model:  ${MODEL}`);
});
