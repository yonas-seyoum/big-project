from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def on_startup():
    print("on_startup")

@app.get("/")
def read_root():
    return {"status": "Live", "version":"0.1.0"}