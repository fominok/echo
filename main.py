from typing import Optional, Any

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/echo")
async def echo(request: Request):
    content_type = request.headers.get("content-type", "")
    
    if "application/json" not in content_type:
        return {"error": "expected a json"}
    
    try:
        body = await request.json()
        return {"echo": body}
    except Exception:
        return {"error": "expected a json"}