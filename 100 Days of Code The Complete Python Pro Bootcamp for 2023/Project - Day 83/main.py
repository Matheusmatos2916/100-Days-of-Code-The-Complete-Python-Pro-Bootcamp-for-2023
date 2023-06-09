from tkinter import Tk, Button, messagebox
 
 
class JogoDaVelha:
    def __init__(self):
        self.jogador_atual = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.janela = Tk()
        self.janela.title("Jogo da Velha")
        self.botoes = [[Button(self.janela, text="", width=10, height=5,
                               command=lambda row=row, col=col: self.clicar_botao(row, col)) for col in range(3)] for
                       row in range(3)]
        for row in range(3):
            for col in range(3):
                self.botoes[row][col].grid(row=row, column=col)
 
    def clicar_botao(self, row, col):
        if self.tabuleiro[row][col] == "":
            self.tabuleiro[row][col] = self.jogador_atual
            self.botoes[row][col].config(text=self.jogador_atual)
            if self.verificar_vitoria():
                messagebox.showinfo("Fim de jogo", f"O jogador {self.jogador_atual} venceu!")
                self.janela.quit()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de jogo", "O jogo empatou!")
                self.janela.quit()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
 
    def verificar_vitoria(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != "":
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != "":
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != "":
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != "":
            return True
        return False
 
    def verificar_empate(self):
        for row in self.tabuleiro:
            if "" in row:
                return False
        return True
 
    def iniciar(self):
        self.janela.mainloop()
 
 
jogo = JogoDaVelha()
jogo.iniciar()