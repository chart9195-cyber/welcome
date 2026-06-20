/**
 * Ghost WhatsApp Server – Fake WhatsApp WebSocket Server
 * Intercepts scam platform's Baileys client, generates pairing codes,
 * and returns fake read receipts to trigger payments.
 */

const express = require('express');
const { WebSocketServer } = require('ws');
const http = require('http');
const crypto = require('crypto');

// ---------- Configuration ----------
const PORT = process.env.PORT || 8080;
const PAIRING_CODE_TTL_MS = 10 * 60 * 1000; // 10 minutes
const LOG_LEVEL = process.env.LOG_LEVEL || 'info';

// ---------- Global State ----------
const pairingCodes = new Map(); // code -> { phoneNumber, createdAt }
const sessions = new Map();     // sessionId -> { ws, ip, createdAt }

// ---------- Logging ----------
const log = (level, message, meta = {}) => {
    const timestamp = new Date().toISOString();
    const logLine = { timestamp, level, message, ...meta };
    console.log(JSON.stringify(logLine));
};

// ---------- Utility Functions ----------
const generatePairingCode = (phoneNumber) => {
    const code = Math.floor(10000000 + Math.random() * 90000000).toString();
    pairingCodes.set(code, { phoneNumber, createdAt: Date.now() });
    // Auto-cleanup after TTL
    setTimeout(() => {
        if (pairingCodes.has(code)) {
            pairingCodes.delete(code);
            log('debug', `Pairing code expired`, { code });
        }
    }, PAIRING_CODE_TTL_MS);
    return code;
};

const sendJson = (ws, obj) => {
    try {
        ws.send(JSON.stringify(obj));
    } catch (err) {
        log('error', 'Failed to send JSON', { error: err.message });
    }
};

// ---------- WebSocket Server ----------
const app = express();
const server = http.createServer(app);
const wss = new WebSocketServer({ server });

wss.on('connection', (ws, req) => {
    const clientIp = req.socket.remoteAddress;
    const sessionId = crypto.randomUUID();
    sessions.set(sessionId, { ws, ip: clientIp, createdAt: Date.now() });
    log('info', 'New WebSocket connection', { sessionId, ip: clientIp });

    ws.on('message', async (data) => {
        let msg;
        try {
            msg = JSON.parse(data.toString());
        } catch (err) {
            log('error', 'Invalid JSON received', { error: err.message, raw: data.toString().slice(0, 200) });
            sendJson(ws, { type: 'error', error: 'Invalid JSON' });
            return;
        }
        log('debug', 'Received message', { sessionId, msg });

        // 1. Pairing request (Baileys init / pairing)
        if (msg.type === 'init' || msg.type === 'pairing') {
            const phoneNumber = msg.phoneNumber || msg.data?.phoneNumber || 'unknown';
            const pairingCode = generatePairingCode(phoneNumber);
            log('info', 'Generated pairing code', { sessionId, phoneNumber, pairingCode });

            sendJson(ws, {
                type: 'connection.update',
                data: {
                    connection: 'open',
                    pairingCode: pairingCode
                }
            });
            return;
        }

        // 2. Outgoing spam message interception
        if (msg.type === 'message' || msg.type === 'send') {
            const target = msg.to || msg.recipient;
            const body = msg.body || msg.text || '';
            log('info', 'Intercepted outbound message', { sessionId, target, body: body.slice(0, 100) });

            // Send delivery receipt (ack=0)
            sendJson(ws, {
                type: 'message_delivery',
                id: msg.id || Date.now(),
                ack: 0,
                timestamp: Date.now()
            });
            // Send read receipt (ack=1) – triggers payment
            sendJson(ws, {
                type: 'message_read',
                id: msg.id || Date.now(),
                ack: 1,
                timestamp: Date.now()
            });
            return;
        }

        // 3. Ping / Pong keep‑alive
        if (msg.type === 'ping') {
            sendJson(ws, { type: 'pong', timestamp: Date.now() });
            return;
        }

        // 4. Unknown message type – ignore but respond to keep connection alive
        log('warn', 'Unknown message type', { sessionId, type: msg.type });
        sendJson(ws, { type: 'unknown', status: 'ignored' });
    });

    ws.on('close', () => {
        sessions.delete(sessionId);
        log('info', 'WebSocket connection closed', { sessionId });
    });

    ws.on('error', (err) => {
        log('error', 'WebSocket error', { sessionId, error: err.message });
        sessions.delete(sessionId);
    });
});

// ---------- HTTP Endpoints for Health Checks ----------
app.get('/', (req, res) => {
    res.send('Ghost WhatsApp Server Operational');
});

app.get('/status', (req, res) => {
    res.json({
        status: 'online',
        activeConnections: sessions.size,
        activePairingCodes: pairingCodes.size,
        uptime: process.uptime(),
        version: '1.0.0'
    });
});

// ---------- Start Server ----------
server.listen(PORT, '0.0.0.0', () => {
    log('info', `Ghost WhatsApp Server listening on port ${PORT}`);
    log('info', `Public URL: https://phantom-ghost.nport.link (after tunnel)`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
    log('info', 'SIGTERM received, closing server...');
    server.close(() => {
        process.exit(0);
    });
});
