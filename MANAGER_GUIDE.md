# 🛠 Gupta Traders Bot: Manager's Setup Guide

To get the bot running, we need 3 specific "Keys" from Google and Meta. Please follow these steps:

### Step 1: Get the Google Gemini API Key (The "Brain")
1. Go to **[Google AI Studio](https://aistudio.google.com/app/apikey)**.
2. Sign in with any Google Account.
3. Click **"Create API key"**.
4. Copy this key. (This allows the bot to understand and reply to customers).

### Step 2: Get the Meta Access Token (The "Phone Line")
*Note: You must have a Facebook Page connected to your Instagram Professional/Business account.*
1. Go to the **[Meta for Developers](https://developers.facebook.com/)** portal.
2. Create a **New App** (Select "Other" -> "Business").
3. In the App Dashboard, find **"Instagram Graph API"** and click "Set up".
4. Go to **API Test Tool** or **Generate Token** section.
5. Ensure the token has these permissions: `instagram_manage_messages`, `pages_manage_metadata`, `pages_show_list`.
6. Copy the **Page Access Token**.

### Step 3: Create a Verify Token (The "Password")
1. This can be any secret password you want (e.g., `GuptaBot2026!`). 
2. We will enter this into the Vercel settings and the Meta Webhook settings so they can "handshake" securely.

---

### What I've done in the codebase:
- Created `api/index.py` which is ready for **Vercel**.
- Added this guide for easy reference.
- Configured the bot to use the latest **Gemini 2.5 Flash** (Free tier).
