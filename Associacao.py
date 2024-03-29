class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = nome

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print("Caneta está escrevendo...")


class MaquinaDeEscrever:
    def __init__(self, modelo):
        self.__modelo = modelo

    @property
    def modelo(self):
        return self.__modelo

    def escrever(self):
        print("Maquina está escrevendo...")
