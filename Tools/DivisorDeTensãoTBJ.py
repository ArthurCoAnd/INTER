# Importar Biblioteclas
from tkinter import *
# Importar Ferramentas
from Tools.Ferramentas import paralelo

class DivisorDeTensãoTBJ(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		Label(self, text="Iterative Transistor Calculater\nDivisor de Tensão TBJ").grid(row=0, column=0, columnspan=7)
		linha = 1

		self.dados = {
			"R1":	{ "val" : "",	"un" : "Ω" },
			"R2":	{ "val" : "",	"un" : "Ω" },
			"Rc":	{ "val" : "",	"un" : "Ω" },
			"Re":	{ "val" : "",	"un" : "Ω" },
			"ro":	{ "val" : "",	"un" : "Ω" },
			"Beta":	{ "val" : "",	"un" : "" },
			"Ci":	{ "val" : "",	"un" : "F" },
			"Co":	{ "val" : "",	"un" : "F" },
			"Ce":	{ "val" : "",	"un" : "F" },
			"Vcc":	{ "val" : "",	"un" : "V" },
			"Vi":	{ "val" : "",	"un" : "V" },
			"Zi":	{ "val" : "",	"un" : "Ω" },
			"Zo":	{ "val" : "",	"un" : "Ω" },
			"R_":	{ "val" : "",	"un" : "Ω" },
			"re":	{ "val" : "",	"un" : "Ω" },
			"Ie":	{ "val" : "",	"un" : "A" },
			"Ve":	{ "val" : "",	"un" : "V" },
			"Vb":	{ "val" : "",	"un" : "V" },
			"Avnl":	{ "val" : "",	"un" : "" }}

		# Ordem Entradas
		self.t_entradas = ["R1", "R2", "Rc", "Re", "ro", "Beta", "Vcc"]
		# Ordem Saidas
		self.t_saidas =  ["Vb", "Ve", "Ie", "re", "R_", "Avnl", "Zi", "Zo"]
		
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
		# Vb
		try:
			self.dados["Vb"]["val"] = (self.dados["Vcc"]["val"]*self.dados["R2"]["val"])/(self.dados["R1"]["val"]+self.dados["R2"]["val"])
			self.var_saidas[self.t_saidas.index("Vb")].set(f'{self.dados["Vb"]["val"]:e}')
		except:
			self.dados["Vb"]["val"] = "-"
			self.var_saidas[self.t_saidas.index("Vb")].set(f'{self.dados["Vb"]["val"]}')
		# Ve
		try:
			self.dados["Ve"]["val"] = self.dados["Vb"]["val"] - 0.7
			self.var_saidas[self.t_saidas.index("Ve")].set(f'{self.dados["Ve"]["val"]:e}')
		except:
			self.dados["Ve"]["val"] = "-"
			self.var_saidas[self.t_saidas.index("Ve")].set(f'{self.dados["Ve"]["val"]}')
		# Ie
		try:
			self.dados["Ie"]["val"] = self.dados["Ve"]["val"]/self.dados["Re"]["val"]
			self.var_saidas[self.t_saidas.index("Ie")].set(f'{self.dados["Ie"]["val"]:e}')
		except:
			self.dados["Ie"]["val"] = "-"
			self.var_saidas[self.t_saidas.index("Ie")].set(f'{self.dados["Ie"]["val"]}')
		# re
		try:
			self.dados["re"]["val"] = (26e-3)/self.dados["Ie"]["val"]
			self.var_saidas[self.t_saidas.index("re")].set(f'{self.dados["re"]["val"]:e}')
		except:
			self.dados["re"]["val"] = "-"
			self.var_saidas[self.t_saidas.index("re")].set(f'{self.dados["re"]["val"]}')
		# R_
		try:
			self.dados["R_"]["val"] = paralelo(self.dados["R1"]["val"],self.dados["R2"]["val"])
			self.var_saidas[self.t_saidas.index("R_")].set(f'{self.dados["R_"]["val"]:e}')
		except:
			self.dados["R_"]["val"] = "-"
			self.var_saidas[self.t_saidas.index("R_")].set(f'{self.dados["R_"]["val"]}')
		# Avnl
		try:
			self.dados["Avnl"]["val"] = -paralelo(self.dados["ro"]["val"],self.dados["Rc"]["val"])/self.dados["re"]["val"]
			self.var_saidas[self.t_saidas.index("Avnl")].set(f'{self.dados["Avnl"]["val"]:e}')
		except:
			self.dados["Avnl"]["val"] = "-"
			self.var_saidas[self.t_saidas.index("Avnl")].set(f'{self.dados["Avnl"]["val"]}')
		# Zi
		try:
			self.dados["Zi"]["val"] = paralelo(self.dados["R_"]["val"],self.dados["Beta"]["val"]*self.dados["re"]["val"])
			self.var_saidas[self.t_saidas.index("Zi")].set(f'{self.dados["Zi"]["val"]:e}')
		except:
			self.dados["Zi"]["val"] = "-"
			self.var_saidas[self.t_saidas.index("Zi")].set(f'{self.dados["Zi"]["val"]}')
		# Zo
		try:
			self.dados["Zo"]["val"] = paralelo(self.dados["ro"]["val"],self.dados["Rc"]["val"])
			self.var_saidas[self.t_saidas.index("Zo")].set(f'{self.dados["Zo"]["val"]:e}')
		except:
			self.dados["Zo"]["val"] = "-"
			self.var_saidas[self.t_saidas.index("Zo")].set(f'{self.dados["Zo"]["val"]}')