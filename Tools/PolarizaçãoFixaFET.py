# Importar Biblioteclas
from tkinter import *
# Importar Ferramentas
from Tools.Ferramentas import paralelo

class PolarizaçãoFixaFET(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		Label(self, text="Iterative Transistor Calculater\nPolarização Fixa FET").grid(row=0, column=0, columnspan=7)
		linha = 1

		self.dados = {
			"Rg":	{ "val" : "",	"un" : "Ω" },
			"Rd":	{ "val" : "",	"un" : "Ω" },
			"Vp":	{ "val" : "",	"un" : "V" },
			"Vgs":	{ "val" : "",	"un" : "V" },
			"Yos":	{ "val" : "",	"un" : "S" },
			"Idss":	{ "val" : "",	"un" : "A" },
			"Zi":	{ "val" : "",	"un" : "Ω" },
			"Zo":	{ "val" : "",	"un" : "Ω" },
			"rd":	{ "val" : "",	"un" : "Ω" },
			"gm":	{ "val" : "",	"un" : "S" },
			"Avnl":	{ "val" : "",	"un" : "" }}

		# Ordem Entradas
		self.t_entradas = ["Rg", "Rd", "Vp", "Vgs", "Yos", "Idss"]
		# Ordem Saidas
		self.t_saidas =  ["rd", "gm", "Avnl", "Zi", "Zo"]
		
		self.entradas = []
		self.var_entradas = []
		self.var_saidas = []
		for e in range(max([len(self.t_entradas),len(self.t_saidas)])):
			if e < len(self.t_entradas):
				Label(self, text=self.t_entradas[e], width=5).grid(row=linha, column=0)
				self.var_entradas.append(StringVar())
				self.var_entradas[e].trace("w", self.calcular)
				self.entradas.append(Entry(self, width=15, textvariable=self.var_entradas[e], bg="red"))
				self.entradas[e].grid(row=linha, column=1)
				Label(self, text=self.dados[self.t_entradas[e]]["un"], width=3).grid(row=linha, column=2)
			if e < len(self.t_saidas):
				Label(self, text="", width=5).grid(row=linha, column=3)
				Label(self, text=self.t_saidas[e], width=5).grid(row=linha, column=4)
				self.var_saidas.append(StringVar())
				self.var_saidas[e].set("-")
				Label(self, textvariable=self.var_saidas[e], width=25).grid(row=linha, column=5)
				Label(self, text=self.dados[self.t_saidas[e]]["un"], width=3).grid(row=linha, column=6)
			linha += 1

	def calcular(self, *args):
		self.lerDados()
		self.dadosT2N()
		self.calcularSaidas()

	# Ler dados das entradas
	def lerDados(self):
		for e in range(len(self.t_entradas)):
			self.dados[self.t_entradas[e]]["val"] = self.var_entradas[e].get()

	# Tentar transformar textos dos dados em números
	def dadosT2N(self):
		for e in range(len(self.t_entradas)):
			try:
				self.dados[self.t_entradas[e]]["val"] = float(self.dados[self.t_entradas[e]]["val"])
				self.entradas[e].config(bg="white")
			except:
				self.dados[self.t_entradas[e]]["val"] = "-"
				self.entradas[e].config(bg="red")

	# Tentar fazer os cálculos das saidas
	def calcularSaidas(self):
		# rd
		try:
			self.dados["rd"]["val"] = 1/self.dados["Yos"]["val"]
			self.var_saidas[self.t_saidas.index("rd")].set(f'{self.dados["rd"]["val"]:e}')
		except:
			self.dados["rd"]["val"] = "-"
			self.var_saidas[self.t_saidas.index("rd")].set(f'{self.dados["rd"]["val"]}')
		# gm
		try:
			self.dados["gm"]["val"] = (2*self.dados["Idss"]["val"]/abs(self.dados["Vp"]["val"]))*(1-(self.dados["Vgs"]["val"]/self.dados["Vp"]["val"]))
			self.var_saidas[self.t_saidas.index("gm")].set(f'{self.dados["gm"]["val"]:e}')
		except:
			self.dados["gm"]["val"] = "-"
			self.var_saidas[self.t_saidas.index("gm")].set(f'{self.dados["gm"]["val"]}')
		# Avnl
		try:
			self.dados["Avnl"]["val"] = -self.dados["gm"]["val"]*paralelo(self.dados["Rd"]["val"],self.dados["rd"]["val"])
			self.var_saidas[self.t_saidas.index("Avnl")].set(f'{self.dados["Avnl"]["val"]:e}')
		except:
			self.dados["Avnl"]["val"] = "-"
			self.var_saidas[self.t_saidas.index("Avnl")].set(f'{self.dados["Avnl"]["val"]}')
		# Zi
		try:
			self.dados["Zi"]["val"] = self.dados["Rg"]["val"]
			self.var_saidas[self.t_saidas.index("Zi")].set(f'{self.dados["Zi"]["val"]:e}')
		except:
			self.dados["Zi"]["val"] = "-"
			self.var_saidas[self.t_saidas.index("Zi")].set(f'{self.dados["Zi"]["val"]}')
		# Zo
		try:
			self.dados["Zo"]["val"] = paralelo(self.dados["Rd"]["val"],self.dados["rd"]["val"])
			self.var_saidas[self.t_saidas.index("Zo")].set(f'{self.dados["Zo"]["val"]:e}')
		except:
			self.dados["Zo"]["val"] = "-"
			self.var_saidas[self.t_saidas.index("Zo")].set(f'{self.dados["Zo"]["val"]}')