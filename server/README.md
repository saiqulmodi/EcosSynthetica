# Ecos-Synthetica school server (optional)

The game never needs this. A school runs it only if it wants class sync or the live AI tutor.

```
set ECOS_TEACHER_KEY=choose-a-secret
set ANTHROPIC_API_KEY=sk-ant-...        (optional: only for the live AI tutor)
python server/ecos_server.py --port 8770
```

Students on the classroom Wi-Fi open `http://<teacher-laptop-ip>:8770/`, tap **School server**, enter the class code, and switch on sync and/or the live AI tutor.

Create a class (the reply contains the join code):

```
curl -X POST -H "X-Teacher-Key: choose-a-secret" -H "Content-Type: application/json" -d "{\"name\":\"7B\",\"grade\":\"7\"}" http://localhost:8770/api/v1/classes
```

Class table: `GET /api/v1/classes/<id>/progress` with the same `X-Teacher-Key` header.

- Stored: class name, join code, each student's display name, and module results (status, stars, best score). No email, no clicks, no location.
- Live AI: Eco Scientist uses `claude-haiku-5-5`, Eco Professional `claude-sonnet-5-5` (with server-side refusal fallbacks). The key stays on this computer. Names, emails and phone numbers are removed before a question is sent; answers must come from the checked concept notes; 60 questions per class per hour. Explorer (Class 1-10) never uses the live AI.
- If the server or the AI is off, the game keeps working offline.
- Tests: `python tests/test_server.py`
