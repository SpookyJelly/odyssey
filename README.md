# Odyseey

## start local env (for test)

- you need to add secrets.json in backend dir

* backend (python 3.10.x)

  1. `cd backend`
  2. `python3 -m venv .venv`
  3. `pip install -r requirement.txt`
  4. `uvicorn app.main:app --reload`

* frontend (node.js 14.x)
  1. `cd frontend`
  2. `npm install`
  3. `npm run dev`
