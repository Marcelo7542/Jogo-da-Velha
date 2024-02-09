from tkinter import *
import random

def proximo_turno(linha, coluna):

    global jogador

    if botoes[linha][coluna]['text'] == "" and vencedor() is False:

        if jogador == jogadores[0]:

            botoes[linha][coluna]['text'] = jogador

            if vencedor() is False:
                jogador = jogadores[1]
                label.config(text=(jogadores[1]+" Turno"))

            elif vencedor() is True:
                label.config(text=(jogadores[0]+" Venceu"))

            elif vencedor() == "Empate":
                label.config(text="Empate!")

        else:

            botoes[linha][coluna]['text'] = jogador

            if vencedor() is False:
                jogador = jogadores[0]
                label.config(text=(jogadores[0]+" Turno"))

            elif vencedor() is True:
                label.config(text=(jogadores[1]+" Venceu"))

            elif vencedor() == "Empate":
                label.config(text="Empate!")

def vencedor():

    for linha in range(3):
        if botoes[linha][0]['text'] == botoes[linha][1]['text'] == botoes[linha][2]['text'] != "":
            botoes[linha][0].config(bg="green")
            botoes[linha][1].config(bg="green")
            botoes[linha][2].config(bg="green")
            return True

    for coluna in range(3):
        if botoes[0][coluna]['text'] == botoes[1][coluna]['text'] == botoes[2][coluna]['text'] != "":
            botoes[0][coluna].config(bg="green")
            botoes[1][coluna].config(bg="green")
            botoes[2][coluna].config(bg="green")
            return True

    if botoes[0][0]['text'] == botoes[1][1]['text'] == botoes[2][2]['text'] != "":
        botoes[0][0].config(bg="green")
        botoes[1][1].config(bg="green")
        botoes[2][2].config(bg="green")
        return True

    elif botoes[0][2]['text'] == botoes[1][1]['text'] == botoes[2][0]['text'] != "":
        botoes[0][2].config(bg="green")
        botoes[1][1].config(bg="green")
        botoes[2][0].config(bg="green")
        return True

    elif espaço_vazio() is False:

        for linha in range(3):
            for coluna in range(3):
                botoes[linha][coluna].config(bg="yellow")
        return "Empate"

    else:
        return False


def espaço_vazio():

    espaço = 9

    for linha in range(3):
        for coluna in range(3):
            if botoes[linha][coluna]['text'] != "":
                espaço -= 1

    if espaço == 0:
        return False
    else:
        return True

def novo_jogo():

    global jogador

    jogador = random.choice(jogadores)

    label.config(text=jogador+" Turno")

    for linha in range(3):
        for coluna in range(3):
            botoes[linha][coluna].config(text="",bg="#F0F0F0")


window = Tk()
window.title("Jogo da Velha")
jogadores = ["x","o"]
jogador = random.choice(jogadores)
botoes = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=jogador + " Turno", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="reiniciar", font=('consolas',20), command=novo_jogo)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for linha in range(3):
    for coluna in range(3):
        botoes[linha][coluna] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda linha=linha, coluna=coluna: proximo_turno(linha,coluna))
        botoes[linha][coluna].grid(row=linha,column=coluna)

window.mainloop()