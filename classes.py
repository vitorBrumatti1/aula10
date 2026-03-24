class Campus: 

    def __init__(self):
        self.cidade = ""
        self.nome = ""
        self.endereco = ""

    def __str__(self):
        return f"Campus: {self.nome}"

    def revelar(self): 
        print(f"O {self.nome} está na cidade {self.cidade}")

class Estudante:
    def __init__(self):
        self.nome = ""
        self.cpf = ""
        self.dataNascimento = ""

    def __str__(self):
        return f"Estudante: {self.nome}"
    
    def apresentar(self): 
        print(f"O {self.nome} nasceu {self.dataNascimento}")
    

vitor = Estudante()
vitor.nome = "Vitor Brumatti"
vitor.cpf = "1021528494-0"
vitor.dataNascimento = "01/04/2008"
vitor.apresentar()


samuel = Estudante()
samuel.nome = "Samuel Rodrigues"
samuel.cpf = "1021528494-0"
samuel.dataNascimento = "06/02/2009"
vitor.apresentar()