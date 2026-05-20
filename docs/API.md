# API Reference

## Base URL
```
http://localhost:8000/api/v1
```

## Threat Analysis

### Analyze Event
**POST** `/threats/analyze`

Analyze a security event for potential threats.

**Request Body**:
```json
{
  "source_ip": "192.168.1.1",
  "destination_ip": "10.0.0.1",
  "protocol": "TCP",
  "port": 443
}
```

**Response**:
```json
{
  "threat_id": "threat_001",
  "risk_score": 0.85,
  "threat_type": "malware",
  "severity": "high"
}
```

### Get Threat Details
**GET** `/threats/{threat_id}`

Get detailed information about a specific threat.

**Response**:
```json
{
  "threat_id": "threat_001",
  "risk_score": 0.85,
  "threat_type": "malware",
  "indicators": [],
  "explanations": {}
}
```

## Response Execution

### Execute Response
**POST** `/response/execute`

Execute automated response actions.

**Request Body**:
```json
{
  "threat_id": "threat_001",
  "actions": ["isolate_host", "block_ip"]
}
```

**Response**:
```json
{
  "response_id": "resp_001",
  "status": "executing",
  "actions": ["isolate_host", "block_ip"]
}
```
