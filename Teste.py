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

candidato1 = Candidato(
    'Joao',
    'Rua De cima',
    4,
    'Desenvolvedor frontend'
)

candidato2 = Candidato(
    'Maria',
    'Rua de Cima',
    3,
    'Desenvolvedora Frontend'
)

candidato3 = Candidato(
    'Pedro',
    'Rua de cima',
    3,
    'Deb'
)
# instanciar provas
prova1_joao = Prova('04/08/2021', 6)
prova2_joao = Prova('10/08/2021', 6)

prova1_maria = Prova('04/08/2021', 3)

prova1_pedro = Prova('04/08/2021', 10)

# adicionando prova a joao
candidato1.adicionarProva(prova1_joao)
candidato1.adicionarProva(prova2_joao)

# adicionando prova a maria
candidato2.adicionarProva(prova1_maria)

# adicionando prova a pedro
candidato3.adicionarProva(prova1_pedro)

processo_seletivo_2021.adicionarCandidato(candidato1)
processo_seletivo_2021.adicionarCandidato(candidato2)
processo_seletivo_2021.adicionarCandidato(candidato3)

print(processo_seletivo_2021.verificarAprovados())