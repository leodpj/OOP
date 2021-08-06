from Associacao import Escritor
from Associacao import Caneta
from Associacao import MaquinaDeEscrever

escritor = Escritor("Machado de Assis")
caneta = Caneta("Caneta Tinteiro MontBlanc")
maquina = MaquinaDeEscrever("Olivetti Valentine")

escritor.ferramenta = maquina

escritor.ferramenta.escrever()