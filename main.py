
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.rotas import router  # importa o router de exemplo

app = FastAPI(
    title="Minha API",
    version="1.0.0",
    description="Exemplo de estrutura FastAPI com routers, controllers, services e repositories",
)

# CORS (libera acesso a partir de outros domínios, útil em desenvolvimento)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique domínios como ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra as rotas
app.include_router(router, prefix="/api", tags=["Usuários"])

# Rota de teste
@app.get("/")
def root():
    return {"message": "API está no ar 🚀"}
