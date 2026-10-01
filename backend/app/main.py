from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import dependencies

app = FastAPI(title="MyApp API", version="1.0")

# === это CORS импортировать fastapi-cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://frontend:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/api/health")
async def health():
    return {"status": "ok"}

app.include_router(dependencies.router, prefix="/api/dependencies")