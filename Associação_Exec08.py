class Prova:
    def __init__(self, data, pontuacao):
        self.data = data
        self.pontuacao = pontuacao


class Candidato:
    def __init__(self, nome, endereco, experiencia, descricao):
        self.nome = nome
        self.endereco = endereco
        self.experiencia = experiencia
        self.descricao = descricao
        self.provas = []
        self.score = 0

    def adicionarProva(self, nova_prova):
        self.provas.append(nova_prova)

    def getScore(self):
        acc = 0
        qto = len(self.provas)
        for prova in self.provas:
            acc += prova.pontuacao
        return acc / qto


class ProcessoSeletivo:
    def __init__(self):
        self.inscritos = []
        self.aprovados = []

    def adicionarCandidato(self, novo_candidato):
        self.inscritos.append(novo_candidato)

    def verificarAprovados(self):
        for candidato in self.inscritos:
            score = candidato.getScore()
            if score >= 8:
                self.aprovados.append(candidato.nome)

        return self.aprovados


processo_seletivo_2021 = ProcessoSeletivo()

candidato1 = Candidato("Leonardo", "Arembepe", 16, "Desenvolverdor FullStack")
candidato2 = Candidato("Vera", "Arembepe", 10, "Administrador")
candidato3 = Candidato("Dinho", "Vista Alegre", 8, "Desenvolverdor FrontEnd")
candidato4 = Candidato("Pirulito", "Fazenda Grande II ", 8, "Contador")


# INSTANCIAR PROVAS
prova1_leonardo = Prova("05/08/2021", 8)
prova2_leonardo = Prova("05/08/2021", 9.5)

prova1_vera = Prova("05/08/2021", 7)
prova2_vera = Prova("05/08/2021", 9)

prova1_dinho = Prova("05/08/2021", 8)
prova2_dinho = Prova("05/08/2021", 8)

prova1_pirulito = Prova("05/08/2021", 8)
prova2_pirulito = Prova("05/08/2021", 8)


# ADICIONAR PROVA LEO

candidato1.adicionarProva(prova1_leonardo)
candidato1.adicionarProva(prova2_leonardo)

candidato2.adicionarProva(prova1_vera)
candidato2.adicionarProva(prova2_vera)

candidato3.adicionarProva(prova1_dinho)
candidato3.adicionarProva(prova2_dinho)

candidato4.adicionarProva(prova1_pirulito)
candidato4.adicionarProva(prova2_pirulito)



processo_seletivo_2021.adicionarCandidato(candidato1)
processo_seletivo_2021.adicionarCandidato(candidato2)
processo_seletivo_2021.adicionarCandidato(candidato3)
processo_seletivo_2021.adicionarCandidato(candidato4)

print(processo_seletivo_2021.verificarAprovados())

