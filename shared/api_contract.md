# NAMI API Contract

## REST

GET /api/health

Returns backend status.

---

## Future Endpoints

POST /api/chat

Send a user message to the agent.

Response:

```json
{
  "session_id": "",
  "message": ""
}
```

---

POST /api/task

Execute a planned task.

---

GET /api/session/{id}

Return session information.

---

WebSocket

/ws

Messages

Client

{
    "type":"chat",
    "content":"Open my ISM thesis"
}

Server

{
    "type":"thinking"
}

{
    "type":"plan"
}

{
    "type":"execution"
}

{
    "type":"finished"
}