"""
Prática do 1° princípio do SOLID: Responsabilidade Única (Sistema escolar)

"""

"""
MÉTODO ERRADO:
"""

"""
#Criando molde dos Alunos do jeito "errado"
class Alunos:
    def __init__(self):

        #Atributos que atribuem valores
        self.alunos= [] #Guarda uma lista vazia para os alunos
        self.notas= [] #Guarda uma lista vazia para as notas dos alunos
    
    #Método para adicionar o aluno com parâmetro(s)
    def adicionar_aluno(self, nome):
        self.alunos.append(nome) #Adiciona parâmetro(s) na lista alunos
        self.alunos.sort() #Ordena a lista para a busca binária funcionar
        return self.alunos #Retorna a lista alunos
    
    #Método para buscar aluno 
    def buscar_aluno(self,alvo):
        inicio = 0
        fim = len(self.alunos) - 1

        #Enquanto for inicio for menor ou igual a fim
        while inicio <= fim:
            meio= (inicio + fim) // 2

            #Se o valor do meio da lista alunos for igual ao alvo
            if self.alunos[meio] == alvo:
                return meio #Retorna o meio
        
            #Mas se o valor do meio da lista alunos for menor que o alvo
            elif self.alunos[meio] < alvo:
                inicio = meio + 1
            else:
                fim= meio - 1
        return -1 #Retorna -1 caso o não seja nenhuma das opções acima
    
    #Método para adicionar as notas do aluno
    def adicionar_notas(self,nota):
        self.notas.append(nota) #Adiciona a nota na lista notas

    #Método para calcular média das notas
    def calcular_media(self):

        if len(self.notas) == 0:
            return 0 #Evita erro de divisão por zero caso não tenha notas

        #Calcula a média das notas, somando o total da lista notas dividida pelo tamanho dela
        media= sum(self.notas)/len(self.notas)
        return media #Retorna a média
    
    #Método para mostrar o status do aluno
    def status(self):

        #Chamamos o método calcular_media() e guardamos o retorno na variável local media
        media = self.calcular_media()

        #Se a media do aluno maior ou igual a 7
        if media >= 7:
            print("Aprovado")
        
        #Mas se a media é maior ou igual 5
        elif media >= 5:
            print("Recuperação")
        else:
            print("Reprovado")

alunos= Alunos()

alunos.adicionar_aluno("Fernado")
alunos.adicionar_aluno("Julia")
alunos.adicionar_aluno("Laura")

#Chama a alunos.alunos e exibe a lista
print(f"{alunos.alunos}")

#Atribui o aluno quer quer buscar
alvo= input("Digite o nome do aluno que quer buscar: ")

#Chama o buscar_aluno e atribui na variável
posicao_aluno= alunos.buscar_aluno(alvo)

if posicao_aluno != -1:
    print(f"Aluno {posicao_aluno} encontrado")
    alunos.adicionar_notas(6.6)
    alunos.adicionar_notas(5.0)
    alunos.adicionar_notas(7.5)

    media= alunos.calcular_media()
    print(f"Média: {media:.2f}")
    alunos.status()
else:
    print(f"\nAluno {alvo} não encontrado")

"""

"""
MÉTODO CERTO:
"""

#Criando molde responsável EXCLUSIVAMENTE pelo gerenciamento dos alunos
class Alunos:
    def __init__(self):

        #Atributo que atribui valor
        self.alunos= [] #Guarda uma lista vazia para os alunos
    
    #Método para adicionar o aluno com parâmetro(s)
    def adicionar_aluno(self, nome):

        self.alunos.append(nome) #Adiciona parâmetro(s) na lista alunos

        self.alunos.sort() #Ordena a lista para a busca binária funcionar

        return self.alunos #Retorna a lista alunos
    
    #Método para buscar aluno 
    def buscar_aluno(self,alvo):
        inicio = 0
        fim = len(self.alunos) - 1

        #Enquanto for inicio for menor ou igual a fim
        while inicio <= fim:
            meio= (inicio + fim) // 2

            #Se o valor do meio da lista alunos for igual ao alvo
            if self.alunos[meio] == alvo:
                return meio #Retorna o meio
        
            #Mas se o valor do meio da lista alunos for menor que o alvo
            elif self.alunos[meio] < alvo:
                inicio = meio + 1
            else:
                fim= meio - 1
        return -1 #Retorna -1 caso o não seja nenhuma das opções acima

#Criando molde responsável EXCLUSIVAMENTE pelas notas, cálculos e avaliações
class Notas:
    def __init__(self,sistema_alunos):

        #Atributos que atribuem valores
        self.notas= {} #Dicionário para guardar as notas vinculadas a cada aluno 
        self.sistema_alunos= sistema_alunos #Recebe a referência da classe Alunos para podermos consultar a busca

    #Método para adicionar as notas do aluno
    def adicionar_nota(self, nome_aluno, nota):

        #Usa o método de busca da classe Alunos para verificar se ele existe antes de lançar a nota
        if self.sistema_alunos.buscar_aluno(nome_aluno) != -1:

            #Se o aluno ainda não tem lista de notas no dicionário, cria uma lista vazia para ele
            if nome_aluno not in self.notas:
                self.notas[nome_aluno] = [] #Cria a lista de notas se for o 1º lançamento

            self.notas[nome_aluno].append(nota) #Adiciona a nota na lista do aluno

            print(f"Nota {nota} adicionada para {nome_aluno}.")
        else:
            print(f"Erro: Aluno '{nome_aluno}' não está cadastrado!")

    #Método para calcular média das notas
    def calcular_media(self, nome_aluno):

        #Garante que o aluno existe no dicionário e que possui pelo menos uma nota
        if nome_aluno in self.notas and len(self.notas[nome_aluno]) > 0:

            return sum(self.notas[nome_aluno]) / len(self.notas[nome_aluno]) #Retorna a média
        
        return 0 #Retorna 0 caso não haja notas para evitar erro de divisão por zero
    
    #Método para mostrar o status do aluno
    def status(self, nome_aluno):

        #Chamamos o método calcular_media() e guardamos o retorno na variável local 'media'
        media = self.calcular_media(nome_aluno)

        #Se a media do aluno maior ou igual a 7
        if media >= 7:
            print("Aprovado")
        
        #Mas se a media é maior ou igual 5
        elif media >= 5:
            print("Recuperação")
        else:
            print("Reprovado")

#Instancia (cria) o objeto 'Alunos'
alunos= Alunos()

#Cadastra os alunos no sistema
alunos.adicionar_aluno("Fernado")
alunos.adicionar_aluno("Julia")
alunos.adicionar_aluno("Laura")

print("\nAlunos cadastrados:", alunos.alunos)
print("-" * 40)

#Instancia (cria) o objeto 'Notas' PASSANDO a instância de alunos para conectar as duas
notas= Notas(alunos)

#Pede ao usuário qual aluno ele quer buscar e lançar notas
alvo = input("Digite o nome do aluno que quer buscar: ")

print("\n--- Lançando Notas ---")
notas.adicionar_nota(alvo, 6.6)
notas.adicionar_nota(alvo, 5.0)
notas.adicionar_nota(alvo, 7.5)

#Exibe a Média e o Status apenas se o aluno tiver notas registradas no dicionário
if alvo in notas.notas:
    print("-" * 40)
    media = notas.calcular_media(alvo)
    print(f"Média de {alvo}: {media:.2f}")
    
    print("Status: ", end="")
    notas.status(alvo)