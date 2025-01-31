# API Documentation for Warren

## Overview
Warren provides a unified API for interacting with various DeFi protocols, including lending, staking, and decentralized exchanges (DEX). This document outlines the available endpoints, request parameters, and response formats.

---
## Authentication
All API requests require an API key, which must be included in the request headers:

```
Authorization: Bearer YOUR_API_KEY
```

---
## Endpoints

### 1. Lending Protocols
#### **Get Available Lending Protocols**
**Endpoint:** `/api/lending/protocols`

**Method:** `GET`

**Response:**
```json
{
  "protocols": ["aave", "lulo"]
}
```

#### **Execute Lending Action**
**Endpoint:** `/api/lending/{protocol}/execute`

**Method:** `POST`

**Request Body:**
```json
{
  "action": "supply",
  "chain": "base",
  "amount": "100",
  "asset": "usdc"
}
```

**Response:**
```json
{
  "transaction_hash": "0x123abc...",
  "status": "success"
}
```

---
### 2. Staking Protocols
#### **Get Available Staking Protocols**
**Endpoint:** `/api/staking/protocols`

**Method:** `GET`

**Response:**
```json
{
  "protocols": ["lido"]
}
```

#### **Execute Staking Action**
**Endpoint:** `/api/staking/{protocol}/execute`

**Method:** `POST`

**Request Body:**
```json
{
  "action": "stake",
  "amount": "50",
  "asset": "eth"
}
```

**Response:**
```json
{
  "transaction_hash": "0x456def...",
  "status": "success"
}
```

---
### 3. DEX (Decentralized Exchange)
#### **Get Available DEX Protocols**
**Endpoint:** `/api/dex/protocols`

**Method:** `GET`

**Response:**
```json
{
  "protocols": ["uniswap"]
}
```

#### **Execute Swap Action**
**Endpoint:** `/api/dex/{protocol}/swap`

**Method:** `POST`

**Request Body:**
```json
{
  "from_asset": "eth",
  "to_asset": "usdc",
  "amount": "1.5"
}
```

**Response:**
```json
{
  "transaction_hash": "0x789ghi...",
  "status": "success"
}
```

---
## Error Handling
All errors return a JSON response with an error message and HTTP status code:

```json
{
  "error": "Unsupported lending protocol",
  "status_code": 400
}
```

---
## Rate Limits
- **Standard Plan:** 100 requests per minute
- **Premium Plan:** 500 requests per minute

Exceeding the limit will return:
```json
{
  "error": "Rate limit exceeded. Try again later.",
  "status_code": 429
}
```

---
## Webhooks
Clients can register webhooks to receive real-time updates on transactions.

**Endpoint:** `/api/webhooks/register`

**Method:** `POST`

**Request Body:**
```json
{
  "url": "https://your-webhook-url.com/updates",
  "event": "transaction_completed"
}
```

**Response:**
```json
{
  "message": "Webhook registered successfully"
}
```

---
## Contact & Support
For further assistance, contact support at [support@warren.finance](mailto:support@warren.finance).

