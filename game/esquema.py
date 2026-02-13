from pydantic import BaseModel
from typing import List

class ResultadoJogo(BaseModel):
    resultado: List[str]
    status: str