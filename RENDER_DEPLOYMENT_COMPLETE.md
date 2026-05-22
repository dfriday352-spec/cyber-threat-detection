# 🚀 Complete Render Deployment Guide - Fresh Start

**Repository:** https://github.com/dfriday352-spec/cyber-threat-detection

This guide will deploy your AI Cyber Threat Detection project on Render in **5 easy steps**.

---

## 📋 Table of Contents

1. [Step 1: Create Render Account](#step-1-create-render-account)
2. [Step 2: Create PostgreSQL Database](#step-2-create-postgresql-database)
3. [Step 3: Create Web Service with Docker](#step-3-create-web-service-with-docker)
4. [Step 4: Add Environment Variables](#step-4-add-environment-variables)
5. [Step 5: Deploy and Verify](#step-5-deploy-and-verify)

---

## Step 1: Create Render Account

### What is Render?
Render is a cloud platform where you can host your application. It's similar to Heroku but better.

### How to Create Account:

1. **Open your browser** and go to:
   ```
   https://render.com
   ```

2. **Click "Get Started" button** (top right)

3. **Choose "Sign up with GitHub"** (easier option)
   - Click: "Continue with GitHub"
   - You'll be redirected to GitHub to authorize Render

4. **Authorize Render**
   - Click: "Authorize render-oss"
   - This allows Render to access your repositories

5. **Complete Setup**
   - Fill in your email and name
   - Click "Continue"
   - You're now logged into Render Dashboard!

### ✅ You're Done with Step 1

---

## Step 2: Create PostgreSQL Database

Your application needs a database. Here's how to create one:

### Create Database:

1. **Go to Render Dashboard:**
   ```
   https://dashboard.render.com
   ```

2. **Click "New +" button** (top right of dashboard)

3. **Select "PostgreSQL"** from the dropdown menu

4. **Fill in the Form:**

   | Field | Value to Enter |
   |-------|----------|
   | **Name** | `cyber-threat-db` |
   | **Database** | `threat_detection` |
   | **User** | `threat_user` |
   | **Region** | Select closest to you (e.g., "Oregon") |
   | **PostgreSQL Version** | Keep default (usually latest) |

5. **Click "Create Database"** button

6. **Wait 2-3 minutes** for database to be created

### ⏳ Status Check:
Look at your PostgreSQL service - when status shows "Available", it's ready!

### 🔐 Copy Your Database URL:

1. Click on your PostgreSQL service name
2. Go to **"Info"** tab (or **"Connections"**)
3. Find **"External Database URL"**
4. **COPY the entire URL** (it looks like):
   ```
   postgresql://threat_user:xxxxxxxxxxxxx@dpg-abc123def456.oregon-postgres.render.com:5432/threat_detection
   ```
5. **SAVE IT somewhere** - you'll need it in Step 4

### ✅ You're Done with Step 2

---

## Step 3: Create Web Service with Docker

Now create the service that runs your application.

### Create Web Service:

1. **Go back to Render Dashboard:**
   ```
   https://dashboard.render.com
   ```

2. **Click "New +" button** (top right)

3. **Select "Web Service"** from the dropdown

4. **Connect Your GitHub Repository:**
   - Click **"Connect account"** (if not connected)
   - Select: `dfriday352-spec/cyber-threat-detection`
   - Click **"Connect"**

5. **Fill in Web Service Settings:**

   | Field | Value |
   |-------|-------|
   | **Name** | `cyber-threat-api` |
   | **Environment** | Select **"Docker"** (NOT Python!) |
   | **Region** | Same as PostgreSQL (e.g., Oregon) |
   | **Branch** | `main` |
   | **Build Command** | Leave empty (Docker auto-detects) |
   | **Start Command** | Leave empty (uses Dockerfile) |
   | **Plan** | Select **"Standard"** |

6. **⚠️ IMPORTANT - Select Docker Runtime:**
   - You'll see a dropdown that says "Python 3"
   - **Click it and change to "Docker"** ← This is important!
   - Docker will handle all your ML libraries (TensorFlow, PyTorch, etc.)

7. **Click "Create Web Service"** button

8. **Wait for initial build** (5-10 minutes)
   - You'll see logs appear
   - It's building your Docker image

### ✅ You're Done with Step 3

---

## Step 4: Add Environment Variables

Your app needs these settings to connect to the database and work properly.

### Add Environment Variables:

1. **Go to your Web Service:**
   - Render Dashboard → Click `cyber-threat-api` service

2. **Click "Settings"** tab (top navigation)

3. **Scroll down to "Environment"** section

4. **Click "Add Environment Variable"** button

5. **Add 8 Variables** - use these exactly:

---

### Variable 1: DATABASE_URL

```
Key: DATABASE_URL
Value: [PASTE the URL you copied in Step 2]
Scope: Run and Build
```

**Example:**
```
postgresql://threat_user:xxxxx@dpg-abc123.oregon-postgres.render.com:5432/threat_detection
```

---

### Variable 2: REDIS_URL

```
Key: REDIS_URL
Value: redis://localhost:6379/0
Scope: Run
```

---

### Variable 3: KAFKA_SERVERS

```
Key: KAFKA_SERVERS
Value: localhost:9092
Scope: Run
```

---

### Variable 4: FLASK_ENV

```
Key: FLASK_ENV
Value: production
Scope: Run
```

---

### Variable 5: LOG_LEVEL

```
Key: LOG_LEVEL
Value: INFO
Scope: Run
```

---

### Variable 6: API_HOST

```
Key: API_HOST
Value: 0.0.0.0
Scope: Run
```

---

### Variable 7: API_PORT

```
Key: API_PORT
Value: 8000
Scope: Run
```

---

### Variable 8: SECRET_KEY

```
Key: SECRET_KEY
Value: your_secret_key_change_me_12345abcdef
Scope: Run
```

---

### How to Add Each Variable:

1. Click **"Add Environment Variable"** button
2. Type the **Key** (e.g., `DATABASE_URL`)
3. Type the **Value** (e.g., the PostgreSQL URL)
4. Select **Scope** from dropdown (`Run` or `Run and Build`)
5. Click **"Add Variable"** button
6. **Repeat** for all 8 variables

### ✅ Verification:

After adding all variables, you should see all 8 listed:

```
✓ DATABASE_URL = postgresql://... (Run and Build)
✓ REDIS_URL = redis://localhost:6379/0 (Run)
✓ KAFKA_SERVERS = localhost:9092 (Run)
✓ FLASK_ENV = production (Run)
✓ LOG_LEVEL = INFO (Run)
✓ API_HOST = 0.0.0.0 (Run)
✓ API_PORT = 8000 (Run)
✓ SECRET_KEY = your_secret_key... (Run)
```

### ✅ You're Done with Step 4

---

## Step 5: Deploy and Verify

Final step - deploy your application!

### Deploy:

1. **Still in Web Service Settings**

2. **Scroll to Top** of the page

3. **Click "Deploy"** button (large blue button)

4. **Watch the Build Process:**
   - Click **"Logs"** tab
   - You'll see Docker building your image
   - Takes about 5-10 minutes
   - Watch for: `✓ Build successful`

5. **Wait for Service to Go Live:**
   - Look for message: 
   ```
   Your service is live at: https://cyber-threat-api.onrender.com
   ```

6. **Copy Your Live URL:**
   ```
   https://cyber-threat-api.onrender.com
   ```

### Verify Deployment:

1. **Test Your API** by opening:
   ```
   https://cyber-threat-api.onrender.com/health
   ```

2. **Expected Response** (if health endpoint exists):
   ```json
   {
     "status": "healthy",
     "message": "API is running"
   }
   ```

3. **If you get an error:**
   - Click "Logs" tab
   - Look for error messages
   - Common issues are usually in logs

### ✅ You're Done with Step 5 - Deployment Complete! 🎉

---

## 🎯 Your Live Application

Your application is now live at:
```
https://cyber-threat-api.onrender.com
```

You can:
- ✅ Visit the URL in browser
- ✅ Share it with others
- ✅ Make API calls to it
- ✅ Monitor logs anytime

---

## 📊 Quick Reference - All Copy & Paste Values

### PostgreSQL URL (from Step 2):
```
postgresql://threat_user:xxxxx@dpg-abc123.oregon-postgres.render.com:5432/threat_detection
```

### All Environment Variables (for Step 4):

| # | Key | Value | Scope |
|---|-----|-------|-------|
| 1 | `DATABASE_URL` | `postgresql://threat_user:xxxxx@dpg-abc123.oregon-postgres.render.com:5432/threat_detection` | Run and Build |
| 2 | `REDIS_URL` | `redis://localhost:6379/0` | Run |
| 3 | `KAFKA_SERVERS` | `localhost:9092` | Run |
| 4 | `FLASK_ENV` | `production` | Run |
| 5 | `LOG_LEVEL` | `INFO` | Run |
| 6 | `API_HOST` | `0.0.0.0` | Run |
| 7 | `API_PORT` | `8000` | Run |
| 8 | `SECRET_KEY` | `your_secret_key_change_me_12345abcdef` | Run |

---

## ⚠️ Important Notes

### Why Docker?
- ✅ Your project has TensorFlow, PyTorch, Kafka (large dependencies)
- ✅ Docker handles all of these perfectly
- ✅ Python 3 runtime would timeout

### Scope Explanation:
- **"Run and Build"** = Available during build AND when app runs
  - Only DATABASE_URL needs this
- **"Run"** = Available only when app is running
  - All other variables use this

### DATABASE_URL is Different:
- Don't guess or make it up
- Go to PostgreSQL service → Copy the real URL
- It's the most important variable

---

## 🚨 Troubleshooting

### Build Failed?
1. Check logs in Render Dashboard
2. Usually missing dependencies in `requirements.txt`
3. Try redeploying

### Can't Connect to Database?
1. Verify DATABASE_URL is correct
2. Check PostgreSQL is running (status: Available)
3. Verify database name and user are correct

### Service Won't Start?
1. Check API_PORT is 8000
2. Verify FLASK_ENV is production
3. Look at logs for error messages

### Forgot a Variable?
1. Go to Settings → Environment
2. Add the missing variable
3. Click "Deploy" to restart with new variable

---

## 🔗 Useful Links

| Resource | URL |
|----------|-----|
| Your Repository | https://github.com/dfriday352-spec/cyber-threat-detection |
| Render Dashboard | https://dashboard.render.com |
| Your Live App | https://cyber-threat-api.onrender.com |
| Render Docs | https://render.com/docs |

---

## ✅ Final Checklist

- [ ] Step 1: Render account created
- [ ] Step 2: PostgreSQL database created and URL copied
- [ ] Step 3: Web Service created with Docker runtime
- [ ] Step 4: All 8 environment variables added
- [ ] Step 5: Deployment clicked and logs show success
- [ ] Verified: App is live at https://cyber-threat-api.onrender.com

---

**Congratulations! Your Cyber Threat Detection API is now deployed on Render! 🚀**

For questions or issues, check the logs in Render Dashboard or review this guide.

---

**Status:** ✅ Ready to Deploy | Last Updated: May 2026