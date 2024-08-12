class Professor:
    def __init__(self, name):
        self.name = name
    def ministrar_aula(self, assunto):
        return "O professor " + self.name + " está ministrando aula sobre " + assunto

class Aluno:
    def __init__(self, name):
        self.name = name
    def presenca(self):
        return "O aluno " + self.name + " está presente\n"

class Aula:
    def __init__(self, professor, assunto, alunos = []):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    def listar_presenca(self):
        presenca = "Presença na aula sobre " + self.assunto + " ministrada pelo professor " + self.professor.name + ":\n"
        for aluno in self.alunos:
            presenca += aluno.presenca()
        return presenca

professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())
