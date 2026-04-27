# 👨‍💻 Developer Deployment Guide (Vercel)

Since the `.env` file is ignored by Git for security, you must manually add the keys to Vercel.

### 1. Push Code to GitHub
```bash
git remote add origin <your-repo-url>
git push -u origin main
```

### 2. Vercel Configuration
1. Import the repository into **Vercel**.
2. During setup (or in **Settings > Environment Variables**), add these 3 keys:
   - `GEMINI_API_KEY`: (From Manager)
   - `META_ACCESS_TOKEN`: (From Manager)
   - `META_VERIFY_TOKEN`: (A secret string of your choice)

### 3. Meta Webhook Configuration
1. In Meta Developer Portal, set the **Callback URL** to:
   `https://your-vercel-domain.vercel.app/api/webhook`
2. Set the **Verify Token** to the same `META_VERIFY_TOKEN` you chose in Step 2.
3. Subscribe to `messages` under the Instagram field.

### 4. Database Seeding
The project uses SQLite. On Vercel (Serverless), the DB is initialized on the first request. To update the machine list:
1. Edit `data/catalog.json`.
2. Push changes to GitHub.
3. The bot will automatically recognize new items on the next restart.
