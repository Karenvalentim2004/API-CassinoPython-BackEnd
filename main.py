from fastapi import FastAPI
from game.logica import jogar
from game.esquema import ResultadoJogo

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Cassino API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"mensagem": "Cassino rodando 🚀"}

@app.post("/jogar", response_model=ResultadoJogo)
def jogar_cassino():
    return jogar()
