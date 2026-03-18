# NemoClaw

**Container Security for AI Coding Agents**

[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](https://opensource.org/licenses/MIT)
[![Demo](https://img.shields.io/badge/Live-Demo-blue)](http://77.42.71.243:8086)
[![Security](https://img.shields.io/badge/Security-Policy%20Enforcement-green)]()

NemoClaw is a container security enforcement layer that protects your infrastructure from AI coding agent exploits. It sandboxes AI agents (Cursor, Claude Code, Aider, etc.) and enforces strict policies on filesystem access, network egress, privilege escalation, binary execution, and resource usage.

**HIPAA-Ready Architecture** - Building toward HIPAA compliance (v2) and SOC 2 (v3).

---

## 🔒 What It Protects Against

| Attack Type | Example | Block Reason |
|-------------|---------|--------------|
| **Filesystem** | `rm -rf /` | Read-only filesystem |
| **Network** | `curl https://google.com` | Egress proxy blocklist |
| **Privilege** | `sudo su` | Unprivileged user (uid=998) |
| **Binary** | `cp /usr/bin/node /tmp/evil` | No binary execution |
| **Resource** | Fork bomb `:(){ :|:& };:` | CPU/memory limits |
| **Logs** | `rm /var/log/audit.log` | Audit log protection |

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/TrustlessMike/nemoclaw.git
cd nemoclaw

# Install dependencies
pip install -r requirements.txt

# Start the dashboard
python src/dashboard/app.py

# Open in browser
open http://localhost:8086
```

---

## 📊 Features

- **Real-time Dashboard** - Live sandbox status, block activity charts, security feed
- **Audit Logs** - Searchable event history with CSV export
- **Policy Engine** - Toggle enforcement rules, custom domain blocklists
- **Team Management** - User roles, API keys, access control
- **OpenShell Integration** - Production-ready sandbox enforcement

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│  AI Coding Agent (Cursor, Claude Code, etc.)   │
└───────────────────┬─────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│  NemoClaw Policy Engine                         │
│  - Filesystem rules (read-only /tmp, /workspace)│
│  - Network rules (egress proxy, blocked domains)│
│  - Privilege rules (uid=998, no root)           │
│  - Resource rules (CPU, memory, fork limits)    │
│  - Audit logging (all blocks logged)            │
└───────────────────┬─────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│  OpenShell Sandbox (Container Enforcement)      │
│  - Actual blocking happens here                 │
└───────────────────┬─────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│  Dashboard + API                                │
│  - Live status, audit logs, policy editor       │
│  - Team management, billing (SaaS)              │
└─────────────────────────────────────────────────┘
```

---

## 🎯 Use Cases

### For AI Dev Shops
- Prevent client agents from breaking production
- Audit compliance for enterprise clients
- Reduce liability from AI-generated code

### For Healthcare/HealthTech
- **HIPAA-eligible architecture** (v2 roadmap)
- Prevent AI agents from accessing PHI without authorization
- Audit trails for compliance reporting

### For Enterprises
- Secure internal coding agent deployments
- Meet SOC2/HIPAA compliance requirements (v2-v3 roadmap)
- Protect secrets and sensitive data

### For Solo Developers
- Safe local AI agent experimentation
- Prevent accidental `rm -rf` disasters
- API key protection

---

## 🛠️ Tech Stack

- **Backend:** Python/Flask
- **Frontend:** Tailwind CSS + Alpine.js + Chart.js
- **Sandbox:** OpenShell (container security)
- **Database:** SQLite (audit logs) → PostgreSQL (team features)

---

## 📱 Dashboard Screenshots

### Security Overview
![Dashboard](images/dashboard.png)

### Audit Logs
![Audit Logs](images/audit.png)

### Policy Editor
![Policies](images/policies.png)

---

## 🔧 Configuration

### Environment Variables

```bash
NEMOCLAW_PORT=8086
NEMOCLAW_HOST=0.0.0.0
NEMOCLAW_DEBUG=false
OPENCLAW_SANDBOX_NAME=openclaw-sandbox
```

### Policy Templates

```yaml
# Strict (Default)
filesystem: enabled
network: enabled
privilege: enabled
binary: enabled
resource: enabled
logs: enabled

# Balanced
filesystem: enabled
network: enabled
privilege: disabled
binary: disabled
resource: disabled
logs: enabled

# Development
filesystem: enabled
network: disabled
privilege: disabled
binary: disabled
resource: disabled
logs: disabled
```

---

## 🚢 Deployment

### Local Development

```bash
python src/dashboard/app.py
# Access: http://localhost:8086
```

### Production (Docker)

```bash
docker build -t nemoclaw .
docker run -p 8086:8086 nemoclaw
```

### Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nemoclaw
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: nemoclaw
        image: nemoclaw:latest
        ports:
        - containerPort: 8086
```

---

## 📈 Roadmap

### v0 (Complete ✅)
- Interactive demo
- Dashboard UI
- Audit logs
- Policy editor
- **Status:** Demo-ready, SMB sales

### v1 (4-6 weeks)
- Encrypted audit log storage (AES-256)
- Authentication (Auth0/Okta)
- Role-based access control (RBAC)
- HTTPS/TLS
- **Status:** Security-hardened, early enterprise

### v2 (8-10 weeks) - HIPAA Ready
- 6-year log retention
- SIEM integration (Splunk, Datadog)
- Access logging + MFA
- Business Associate Agreement (BAA) capability
- **Status:** HIPAA technical safeguards complete

### v3 (12-16 weeks) - SOC 2 Ready
- SOC 2 Type 2 audit
- Formal security policies
- Penetration testing
- Incident response workflows
- **Status:** Enterprise compliance complete

---

## 🔐 Compliance Roadmap

### HIPAA Technical Safeguards

| Requirement | v0 | v1 | v2 | v3 |
|-------------|----|----|----|----|
| Access Control | ❌ | ✅ | ✅ | ✅ |
| Audit Controls | ✅ | ✅ | ✅ | ✅ |
| Integrity Controls | ✅ | ✅ | ✅ | ✅ |
| Transmission Security | ❌ | ✅ | ✅ | ✅ |
| Encryption at Rest | ❌ | ✅ | ✅ | ✅ |
| Log Retention (6 years) | ❌ | ❌ | ✅ | ✅ |
| BAA Capability | ❌ | ❌ | ✅ | ✅ |

### SOC 2 Trust Criteria

| Criteria | v0 | v1 | v2 | v3 |
|----------|----|----|----|----|
| Security | ✅ | ✅ | ✅ | ✅ |
| Availability | ❌ | ⚠️ | ✅ | ✅ |
| Processing Integrity | ✅ | ✅ | ✅ | ✅ |
| Confidentiality | ❌ | ✅ | ✅ | ✅ |
| Privacy | ❌ | ❌ | ✅ | ✅ |

**Legend:** ✅ Complete | ⚠️ Partial | ❌ Not implemented

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built on top of [OpenShell](https://openshell.io) container security
- Inspired by the need for safe AI coding agent deployments
- Community feedback from AI dev shops and enterprises

---

## 📞 Contact

**Cortana Solutions** - Building secure AI operations

- Website: https://cortanasolutions.com
- Demo: http://77.42.71.243:8086
- Email: mike@cortanasolutions.com
- GitHub: https://github.com/TrustlessMike/nemoclaw

---

**Built with ❤️ by Cortana Solutions**

*HIPAA compliance roadmap: v2 (8-10 weeks). SOC 2 roadmap: v3 (12-16 weeks).*
