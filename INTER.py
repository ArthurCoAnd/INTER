# INTER - INterative Transistor calculatER

# "A LICENÇA BEER-WARE" ou "A LICENÇA DA CERVEJA" (Revisão 42):
# <arthurcoand@gmail.com> escreveu este arquivo.
# Enquanto você manter este comentário, você poderá fazer o que quiser com este arquivo.
# Caso nos encontremos algum dia e você ache que este arquivo vale, você poderá me comprar uma cerveja em retribuição.
# Arthur Cordeiro Andrade.

# Importar Bibliotecas
import os
import sys
from tkinter import *
from pygame import mixer
# Importar Ferrementas
from Tools.PolarizaçãoFixaTBJ import PolarizaçãoFixaTBJ as PFTBJ
from Tools.DivisorDeTensãoTBJ import DivisorDeTensãoTBJ as DTTBJ
from Tools.SeguidorEmissorTBJ import SeguidorEmissorTBJ as SETBJ

class Inter(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.menu = Menu(self)
		self.configure(menu=self.menu)

		self.menu_métodos = Menu(self.menu, tearoff=0)
		self.menu_métodos.add_command(label="Polarização Fixa TBJ", command=lambda: self.TrocarJanela(PFTBJ))
		self.menu_métodos.add_command(label="Divisor de Tensão TBJ", command=lambda: self.TrocarJanela(DTTBJ))
		self.menu_métodos.add_command(label="Seguidor Emissor TBJ", command=lambda: self.TrocarJanela(SETBJ))
		self.menu_métodos.add_command(label="Base Comum TBJ", command=lambda: self.Teste("BCTBJ"))
		self.menu_métodos.add_command(label="Polarização Fixa FET", command=lambda: self.Teste("PFFET"))
		self.menu_métodos.add_command(label="Divisor de Tensão FET", command=lambda: self.Teste("DTFET"))
		self.menu_métodos.add_command(label="Dreno Comum TBJ", command=lambda: self.Teste("DCTBJ"))
		self.menu.add_cascade(label="Circuitos", menu=self.menu_métodos)

		self.janela = None
		self.TrocarJanela(PFTBJ)

	def TrocarJanela(self, tipoJanela):
		self.configure(menu=None)
		novaJanela = tipoJanela(self)
		if self.janela is not None:
			self.janela.destroy()
		self.janela = novaJanela
		self.janela.grid(row=0, column=0)

	def Teste(self, t):
		print(f"Teste - {t}")

def resource_path(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def TocarHino():
	mixer.music.load(resource_path("Sounds/Hino Internacional.mp3"))
	mixer.music.play(loops=-1)

if __name__ == "__main__":
	mixer.init()
	TocarHino()
	app = Inter()
	app.resizable(False, False)
	app.title("Inter")
	app.iconbitmap(resource_path("Images/Inter.ico"))
	app.mainloop()