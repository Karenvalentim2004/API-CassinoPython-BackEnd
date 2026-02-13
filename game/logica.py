import random

simbolos = ["🍒", "🍋", "🍇", "🔔", "⭐", "💎"]

def girar_rolo():
    return random.choice(simbolos)

def jogar():
    resultado = [girar_rolo(), girar_rolo(), girar_rolo()]

    if resultado[0] == resultado[1] == resultado[2]:
        status = "WIN"
    elif (
        resultado[0] == resultado[1] or
        resultado[1] == resultado[2] or
        resultado[0] == resultado[2]
    ):
        status = "QUASE"
    else:
        status = "PERDEU"

    return {
        "resultado": resultado,
        "status": status
    }