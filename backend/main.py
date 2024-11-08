from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints import router as api_router

app = FastAPI()

origins = [
    "http://localhost:3000",]
# Configuración de CORS para permitir el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas de la API
app.include_router(api_router)

# Esto permite ejecutar el archivo main.py y levantar el servidor
if __name__ == "_main_":
    import uvicorn
    #uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)