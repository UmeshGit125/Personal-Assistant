# 🚀 AI Personal Assistant (Streamlit + n8n + Groq)

This project is a deterministic AI Personal Assistant built using:

- Streamlit (Frontend Chat UI)
- n8n (Automation Backend)
- Groq LLM (meta-llama/llama-4-scout-17b)
- Google Services (Gmail, Calendar, Tasks, Docs, Sheets)

The assistant performs real-world actions strictly through predefined tools inside n8n.

It does NOT execute actions directly — all actions are validated and automated via workflow.

---

# 📦 Features

- Send emails (Gmail)
- Create calendar events
- Create/Delete tasks
- Update Google Docs notes
- Add expenses to Google Sheets
- Deterministic tool-based execution
- Strict schema validation

---

# 🏗 How The System Works

User → Streamlit UI → n8n Webhook → Groq LLM → Tool Call → Google Service → Response

---

# ⚙️ Requirements

Before starting, make sure you have:

- Python 3.9+
- Node access to n8n (self-hosted or cloud)
- Groq API key
- Google Cloud project with:
  - Gmail API enabled
  - Google Calendar API enabled
  - Google Docs API enabled
  - Google Sheets API enabled

---

# 🔐 Environment Setup

Create a `.env` file in the root directory of the project.

Example:
# 🚀 AI Personal Assistant (Streamlit + n8n + Groq)

This project is a deterministic AI Personal Assistant built using:

- Streamlit (Frontend Chat UI)
- n8n (Automation Backend)
- Groq LLM (meta-llama/llama-4-scout-17b)
- Google Services (Gmail, Calendar, Tasks, Docs, Sheets)

The assistant performs real-world actions strictly through predefined tools inside n8n.

It does NOT execute actions directly — all actions are validated and automated via workflow.

---

# 📦 Features

- Send emails (Gmail)
- Create calendar events
- Create/Delete tasks
- Update Google Docs notes
- Add expenses to Google Sheets
- Deterministic tool-based execution
- Strict schema validation

---

# 🏗 How The System Works

User → Streamlit UI → n8n Webhook → Groq LLM → Tool Call → Google Service → Response

---

# ⚙️ Requirements

Before starting, make sure you have:

- Python 3.9+
- Node access to n8n (self-hosted or cloud)
- Groq API key
- Google Cloud project with:
  - Gmail API enabled
  - Google Calendar API enabled
  - Google Docs API enabled
  - Google Sheets API enabled

---

# 🔐 Environment Setup

Create a `.env` file in the root directory of the project.

Example:

GROQ_API_KEY=your_groq_api_key_here
N8N_WEBHOOK_URL=https://your-n8n-domain/webhook/your-endpoint 




IMPORTANT:
- Never commit `.env` to GitHub.
- Add `.env` to `.gitignore`.

---

# 🛠 Installation Steps

## 1️⃣ Clone the Repository




