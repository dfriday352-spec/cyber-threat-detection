# Quick Start: Deploy to Render in 5 Minutes

## 1. Prepare Your Repository
```bash
git pull origin main
git push origin main
```

## 2. Go to Render
Visit https://dashboard.render.com

## 3. Create a New Service
- Click **"New +"** → **"Web Service"**
- Select your GitHub repository
- Branch: `main`
- Build Command: `pip install -r requirements.txt && python scripts/setup_db.py`
- Start Command: `python -m src.api.main`

## 4. Add Environment Variables
In Render dashboard:
```
DATABASE_URL: [Render will provide this]
REDIS_URL: redis://localhost:6379
KAFKA_BOOTSTRAP_SERVERS: your-kafka-broker:9092
FLASK_ENV: production
LOG_LEVEL: INFO
```

## 5. Create Database
- In Render: Create PostgreSQL instance
- Note the connection string
- Add to `DATABASE_URL` env var

## 6. Deploy
Click **"Create Web Service"** → Render deploys automatically

## 7. Verify
```bash
curl https://your-service.onrender.com/health
```

✅ Done! Your app is live on Render.

---

**For detailed guide:** See `RENDER_DEPLOYMENT.md`
