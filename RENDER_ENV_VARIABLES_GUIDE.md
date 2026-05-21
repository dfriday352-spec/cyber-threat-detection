# Render Environment Variables Guide

## ✅ Render Variable Naming Rules

Render environment variable names **MUST**:
- ✅ Use ONLY: **Letters (A-Z), Numbers (0-9), and Underscore (_)**
- ✅ Start with a letter
- ❌ NO: Hyphens (-), Dots (.), Spaces, or special characters

---

## Correct vs Incorrect Examples

### ❌ WRONG - These Will Show Errors:

| Variable Name | Error | Reason |
|---|---|---|
| `database.url` | ❌ Invalid character | Contains **dot (.)** |
| `kafka-servers` | ❌ Invalid character | Contains **hyphen (-)** |
| `api-port` | ❌ Invalid character | Contains **hyphen (-)** |
| `log_level_debug` | ⚠️ May fail | Contains too many characters? |
| `2FA_KEY` | ❌ Invalid start | Starts with **number** |
| `@SECRET_KEY` | ❌ Invalid character | Contains **@ symbol** |

### ✅ CORRECT - These Will Work:

| Variable Name | Usage |
|---|---|
| `DATABASE_URL` | ✅ Database connection |
| `KAFKA_SERVERS` | ✅ Kafka brokers |
| `API_PORT` | ✅ API port |
| `LOG_LEVEL` | ✅ Logging level |
| `SECRET_KEY` | ✅ Secret key |
| `REDIS_URL` | ✅ Redis connection |
| `FLASK_ENV` | ✅ Flask environment |
| `MY_CUSTOM_VAR` | ✅ Custom variable |

---

## Required Variables for Your Project

### Set These in Render Dashboard:

1. **DATABASE_URL** (from PostgreSQL service)
   ```
   postgresql://threat_user:password@host:5432/cyber_threat_db
   ```

2. **REDIS_URL** (if using Redis)
   ```
   redis://host:6379/0
   ```

3. **KAFKA_SERVERS** (Kafka brokers)
   ```
   broker1:9092,broker2:9092
   ```

4. **FLASK_ENV**
   ```
   production
   ```

5. **LOG_LEVEL**
   ```
   INFO
   ```

6. **API_PORT**
   ```
   8000
   ```

7. **API_HOST**
   ```
   0.0.0.0
   ```

---

## Step-by-Step: Add Environment Variables in Render

### Step 1: Go to Environment Variables Section
- Render Dashboard → Your Web Service
- Click **"Settings"** tab
- Scroll to **"Environment"** section

### Step 2: Click "Add Environment Variable"

### Step 3: Fill in the Form

**Field 1: Key** (Variable Name)
```
DATABASE_URL
```
(Only: letters, numbers, underscore)

**Field 2: Value** (Variable Value)
```
postgresql://threat_user:password@dpg-abc.oregon-postgres.render.com:5432/cyber_threat_db
```
(Can contain any characters)

**Field 3: Scope**
- Select: **"Run"** or **"Run and Build"**
- For most variables: **"Run"**

### Step 4: Click "Add Variable"

### Step 5: Repeat for Each Variable

---

## Common Mistakes & Fixes

### ❌ Problem 1: Using Hyphens in Variable Names

```
❌ WRONG:
kafka-bootstrap-servers

✅ CORRECT:
KAFKA_SERVERS
or
KAFKA_BOOTSTRAP_SERVERS
```

### ❌ Problem 2: Using Dots in Variable Names

```
❌ WRONG:
database.url
app.secret.key

✅ CORRECT:
DATABASE_URL
APP_SECRET_KEY
```

### ❌ Problem 3: Variable Name Too Long or Invalid

```
❌ WRONG:
KAFKA-BOOTSTRAP-SERVERS-LIST-1
threat.detection.model.version

✅ CORRECT:
KAFKA_SERVERS
THREAT_MODEL_VERSION
```

### ❌ Problem 4: Special Characters

```
❌ WRONG:
@DATABASE_URL
$API_KEY
#LOG_LEVEL

✅ CORRECT:
DATABASE_URL
API_KEY
LOG_LEVEL
```

---

## Your Project's Variables (CORRECTED)

### Use These Names:

```
DATABASE_URL          ← Connection string for PostgreSQL
REDIS_URL            ← Connection string for Redis
KAFKA_SERVERS        ← Kafka brokers (was KAFKA_BOOTSTRAP_SERVERS)
FLASK_ENV            ← Flask environment
LOG_LEVEL            ← Log level
API_HOST             ← API host
API_PORT             ← API port
SECRET_KEY           ← Secret key
ALGORITHM            ← Algorithm (HS256)
ENVIRONMENT          ← Environment (development/production)
```

---

## Complete Variable Setup Form

| Key | Value | Scope |
|-----|-------|-------|
| `DATABASE_URL` | `postgresql://threat_user:pwd@host:5432/cyber_threat_db` | Run |
| `REDIS_URL` | `redis://host:6379/0` | Run |
| `KAFKA_SERVERS` | `localhost:9092` | Run |
| `FLASK_ENV` | `production` | Run |
| `LOG_LEVEL` | `INFO` | Run |
| `API_HOST` | `0.0.0.0` | Run |
| `API_PORT` | `8000` | Run |
| `SECRET_KEY` | `your_secret_key_here` | Run |

---

## ✅ Troubleshooting

### Error: "Invalid character in key"

**Cause:** Using `-`, `.`, or other special characters in variable name

**Solution:** Replace with `_`:
```
kafka-servers  → KAFKA_SERVERS
db.host        → DB_HOST
api-key        → API_KEY
```

### Error: "Key must start with a letter"

**Cause:** Variable name starts with a number or symbol

**Solution:** Add prefix letter:
```
2FA_KEY  → TWO_FA_KEY
@SECRET  → AT_SECRET
```

### Variables Not Loading

**Cause:** Changed variables but service not restarted

**Solution:** 
1. After adding/changing variables
2. Go to **"Settings"** → **"Restart Service"**
3. Or wait for automatic redeploy

---

## Reference

**Render Variable Rules (Official):**
- Pattern: `^[a-zA-Z_][a-zA-Z0-9_]*$`
- Max length: Typically 256 characters
- Values can contain anything

**Pattern Explanation:**
- `[a-zA-Z_]` = Start with letter or underscore
- `[a-zA-Z0-9_]*` = Followed by letters, numbers, underscores

---

**Now your environment variables should work correctly! 🎉**

Need help setting up specific variables? Let me know!
