from fastapi import FastAPI
from game.logica import jogar
from game.esquema import ResultadoJogo

app = FastAPI(
    title="Cassino API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"mensagem": "Cassino rodando 🚀"}

@app.get("/jogar", response_model=ResultadoJogo)
def jogar_cassino():
    return jogar()
