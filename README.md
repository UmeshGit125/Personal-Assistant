# 🚀 AI Personal Assistant (Streamlit + n8n + Groq)

This project is a deterministic AI Personal Assistant that performs real-world actions using:

- 🖥 Streamlit (Frontend Chat UI)
- 🔄 n8n (Automation Backend)
- 🧠 Groq LLM (meta-llama/llama-4-scout-17b)
- 📧 Gmail
- 📅 Google Calendar
- ✅ Google Tasks
- 📄 Google Docs
- 💰 Google Sheets

All actions are executed strictly through structured tool calls inside n8n.

---

## ✨ Features

- Send emails
- Create calendar events
- Manage tasks
- Update notes (Google Docs)
- Track expenses (Google Sheets)
- Deterministic & schema-validated execution

---

# ⚙️ Setup Guide

## 1️⃣ Requirements

- Python 3.9+
- n8n (self-hosted or cloud)
- Groq API key
- Google Cloud project with:
  - Gmail API
  - Calendar API
  - Docs API
  - Sheets API enabled

---

## 2️⃣ Clone the Repository

```bash
git clone https://github.com/UmeshGit125/Personal-Assistant.git
cd Personal-Assistant
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
N8N_WEBHOOK_URL=https://your-n8n-domain/webhook/your-endpoint
```

⚠️ Do NOT commit `.env` to GitHub. Add it to `.gitignore`.

---

# 🔄 n8n Configuration

1. Import the provided workflow JSON into n8n.
2. Configure credentials:
   - Gmail OAuth2
   - Google Calendar OAuth2
   - Google Tasks OAuth2
   - Google Docs OAuth2
   - Google Sheets OAuth2
3. In the AI Agent node:
   - Model: `meta-llama/llama-4-scout-17b`
   - Temperature: `0`
4. Activate the workflow.
5. Copy the webhook URL and paste it into your `.env`.

---

# ▶️ Run the App

```bash
streamlit run app.py
```

The assistant will open in your browser.

---

# 🧪 Example Commands

- `Send an email to john@example.com about tomorrow's meeting at 10 AM`
- `Schedule meeting with Suraj tomorrow at 11 PM for 30 minutes`
- `Add expense 500 in travel for taxi ride`
- `Delete task Submit report`

---

# 🔒 Security Notes

- Never expose API keys.
- Keep `.env` private.
- Use OAuth2 securely.
- Restrict webhook access in production.

---

# 📜 License

MIT License

---

⭐ If this project helps you, consider starring the repository.
