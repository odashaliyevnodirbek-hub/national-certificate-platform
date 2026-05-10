from fastapi import FastAPI

app = FastAPI(title="National Certificate Mock Platform")

@app.get("/")
def root():
    return {"message": "Backend is running"}
