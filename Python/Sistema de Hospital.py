"""
Sistema de Atendimento de Hospital
Estruturas usadas
• Fila comum → atendimento normal
• Fila prioritária → idosos/emergência
• Pilha → histórico dos últimos atendimentos
• Busca → localizar paciente
• BST → cadastro e busca de pacientes por prontuário (Árvore Binária)
Extras interessantes
• Simulação de tempo de espera
• Atendimento automático
• Menu interativo

"""
#Importa a classe deque do módulo collections (ótima para criar filas comuns eficientes O(1))
from collections import deque

#Importa o módulo heapq, usado para criar filas de prioridade (estruturas do tipo Min-Heap)
import heapq

#Modelo para representar cada paciente e seus atributos no sistema
class Paciente:

    #Método que constroí o molde com os atributos do objeto
    def __init__(self, cpf, nome_paciente, idade, gravidade):

        #Armazena o nome do paciente recebido como parâmetro
        self.nome_paciente = nome_paciente

        #Armazena a idade do paciente recebida como parâmetro
        self.idade = idade

        #Armazena o nível de risco/urgência recebido como parâmetro
        self.gravidade = gravidade

        #Armazena o CPF do paciente
        self.cpf= cpf

#Molde (modelo) da Fila Comum
class FilaComum:

    #Método que constroí o molde
    def __init__(self):

        #Inicializa uma fila vazia usando o deque (Double-Ended Queue)
        self.fila_comum = deque()

    #Método para registrar a chamada do paciente
    def registrar_chamada(self, paciente):

        #Adiciona o objeto paciente ao final da fila comum (FIFO: First In, First Out)
        self.fila_comum.append(paciente)

    #Método para chamar o próximo paciente
    def chamar_proximo(self):

        #Verifica se o atributo que guarda a fila aponta para None
        if self.fila_comum is None:

            #Lança uma exceção de índice caso a condição acima seja verdadeira
            raise IndexError("Fila vazia")

        #Remove e retorna o primeiro elemento (paciente) da fila comum
        return self.fila_comum.popleft()

#Molde da Fila Prioritária baseada em Heap (Árvore binária de prioridades)
class FilaPrioritaria:

    #Método que constroí o molde com os atributos
    def __init__(self):

        #Inicializa uma lista vazia que será gerenciada pelo heapq
        self.fila_prioritaria = []

        #Contador numérico para registrar a ordem de chegada e desempatar prioridades iguais
        self.ordem_chegada = 0

    #Método para registrar a chamada do paciente prioritário
    def registrar_chamada(self, paciente):

        #Incrementa o contador de chegada a cada novo paciente registrado
        self.ordem_chegada += 1

        # Agrupa gravidade, ordem de chegada e o objeto do paciente em uma estrutura de tupla
        pacientes_embrulhado = (paciente.gravidade, self.ordem_chegada, paciente)

        # Insere a tupla dentro da lista organizando-a como um Min-Heap estruturado
        heapq.heappush(self.fila_prioritaria, pacientes_embrulhado)

    #Método para chamar o próximo paciente prioritário
    def chamar_proximo(self):
        # Verifica se a lista da fila prioritária aponta para None
        if self.fila_prioritaria is None:
            # Lança uma exceção indicando que não há ninguém para chamar
            raise IndexError("Fila vazia")

        #Remove e retorna o menor elemento (maior prioridade) da árvore Min-Heap
        return heapq.heappop(self.fila_prioritaria)
  
#Define a classe Prontuario que gerencia as informações médicas de um paciente
class Prontuario:
  """Gerencia o histórico de atendimento de um cliente específico."""

  #Método construtor que inicializa o prontuário recebendo o paciente como argumento
  def __init__(self, paciente):

    """Inicializa o prontuário para um cliente, criando um histórico vazio."""
    #Inicializa uma fila dinâmica (deque) vazia para armazenar o histórico de consultas
    self.Historico = deque()  # Usamos deque para um histórico eficiente (adicionar/remover do final)

    #Define a propriedade paciente do objeto para guardar os dados/nome do paciente associado
    self.paciente = paciente # Armazena o nome do cliente

  #Método para inserir um novo relato médico e classificação no prontuário
  def add_Historico(self, descricao, nivel_gravidade):

    """Adiciona um novo registro ao histórico do paciente."""
    #Cria uma estrutura de dicionário mapeando a descrição do sintoma e a gravidade em letras maiúsculas
    #Cria um dicionário para o registro
    registro = {"descricao": descricao, "gravidade": nivel_gravidade.upper()}

    #Insere o dicionário recém-criado na última posição do deque do histórico
    self.Historico.append(registro) # Adiciona o registro ao final do deque

    #Imprime no terminal a confirmação dos dados adicionados ao prontuário
    print("Prontuario adicionado para o paciente", self.paciente, "\nDescrição:", descricao, "\nGravidade:", nivel_gravidade)

  #Método utilitário para checar a existência de registros salvos
  def vazio(self):

    """Verifica se o histórico está vazio."""
    #Avalia se o tamanho do histórico é igual a zero, retornando True (vazio) ou False (com registros)
    return len(self.Historico) == 0 # Retorna True se o deque estiver vazio, False caso contrário

  #Método simulando uma Pilha (LIFO) para descartar a última informação registrada
  def remove_Historico(self):

    """Remove o último registro adicionado ao histórico."""
    #Desvia o fluxo caso o método utilitário identifique que não há dados no histórico
    if self.vazio():

      #Exibe um alerta de que a estrutura já se encontra vazia
      print("Não tem registro para remover")

      #Retorna uma ausência de valor para encerrar a execução do método prematuramente
      return None

    #Caso possua dados no histórico, entra no bloco alternativo
    else:

      #Elimina o último elemento posicionado na extremidade direita do deque
      #Remove o último item do deque
      self.Historico.pop()

  #Método para espiar o registro inserido por último na estrutura
  def Historico_atual(self):

    """Retorna o registro mais recente do histórico."""
    #Desvia o fluxo caso a lista de prontuários esteja vazia
    if self.vazio():

      #Informa ao usuário que nenhum prontuário foi encontrado na busca
      print("Não tem prontuarios registrados")

      #Retorna uma ausência de valor indicando falha na recuperação do dado
      return None

    #Caso possua dados, executa a busca do último elemento
    else:

      #Acessa e retorna o elemento no índice -1 (posição final) do deque de histórico
      #Retorna o último item do deque (o mais recente)
      return self.Historico[-1]

  #Método responsável por varrer e imprimir toda a linha do tempo médica do paciente
  def exibir_prontuario_completo(self):

    #Condicional que barra o processamento caso a fila de históricos esteja vazia
    if self.vazio():

      #Exibe mensagem de erro na tela indicando a falta de registros
      print("Não tem prontuarios registrados")
      #Aborta o restante da função retornando um valor nulo
      return None

    # Imprime uma barra divisória estilizada com o nome do paciente em letras maiúsculas
    print(f"\n=== HISTÓRICO DE ATENDIMENTOS: {self.paciente.upper()} ===")
    # Loop que percorre o deque do fim para o começo (do registro mais novo ao mais antigo)
    for r in reversed(self.Historico):

        # Passo 3: A Limpeza dos Dados (Isolar as Chaves).
        # Lembre-se que cada 'h' ali dentro é um dicionário assim: {"descricao": "Dor de cabeça", "gravidade": "POUCO URGENTE"}
        # Se printássemos 'h' direto, apareceria na tela cheio de aspas e chaves.
        # Para limpar, nós isolamos e pegamos apenas o VALOR que está guardado em cada chave
        #Extrai o valor associado à chave "descricao" do dicionário atual do loop
        texto_descricao = r["descricao"]

        #Extrai o valor associado à chave "gravidade" do dicionário atual do loop
        texto_gravidade = r["gravidade"]

        #Agora printamos apenas as variáveis limpas, sem a estrutura do dicionário aparecendo
        #Exibe os dados formatados de forma organizada e legível no console
        print(f"-> Sintoma: {texto_descricao} | Risco: {texto_gravidade}")

#Instancia (cria) o objeto da fila para pacientes comuns
fila_comum = FilaComum()
#Instancia (cria) o objeto da fila para pacientes prioritários
fila_prioritaria = FilaPrioritaria()

#Inicializa um dicionário vazio para associar o CPF do paciente ao seu respectivo objeto de dados (Tabela Hash/Busca O(1))
hospital = {}

#Inicia um loop infinito para manter o menu rodando até que o usuário decida sair
while True:

  #Exibe o cabeçalho do sistema na tela
  print("*--Sistema do Hospital--*\n")

  #Exibe as opções disponíveis para o usuário interagir
  print("1- Cadastrar Paciente\n2- Atender Próximo Paciente\n3- Buscar Dados do Paciente\n4- Ver Histórico do Prontuário do Paciente\n5- Sair do sistema\n")

  #Captura a escolha do usuário como uma string
  opcao = input("Escolha uma opção: ")

  # Estrutura de controle que analisa a opção digitada (semelhante ao switch-case de outras linguagens)
  match opcao:

    #Caso o usuário escolha a opção 1 (Cadastrar Paciente)
    case "1":
      
        #Exibe uma mensagem no console e captura o documento de identificação única do paciente (CPF) como texto
        cpf= input("Digite o CPF do paciente: ")

        #Exibe uma mensagem no terminal e aguarda o usuário digitar o nome do paciente.
        nome = input("Digite o nome do paciente: ")

        #Exibe uma mensagem solicitando a idade do paciente e a converte em um tipo inteiro.
        idade = int(input("Digite a idade do paciente: "))

        #Exibe a tabela de triagem baseada no Protocolo de Manchester
        print("Níveis de Prioridade\n")
        print("1 - Emergência\n2 - Muito Urgente\n3 - Urgente\n4 - Pouco Urgente\n5 - Não Urgente\n")

        #Captura o nível de gravidade digitado pelo usuário e converte para número inteiro
        nivel = int(input("Qual é o nível de prioridade do paciente: "))

        #Altera o nível do paciente para 1 (Emergência) caso ele tenha 60 anos ou mais
        if idade >= 60:
            nivel = 1

        #Instancia o objeto Paciente enviando os dados de nome, idade, nível e cpf definidos antes
        paciente = Paciente(nome, idade, nivel, cpf)
        
        #Cria uma instância da classe Prontuario passando o nome do paciente associado
        prontuario_paciente = Prontuario(paciente.nome_paciente)

        #Salva uma estrutura de dicionário interna para o CPF contendo o objeto do paciente e o prontuário em branco
        hospital[cpf] = {"dados": paciente, "prontuario": prontuario_paciente}


        #Avalia se a idade é maior/igual a 60 ou se o nível de gravidade está entre 1 e 3
        if paciente.idade >= 60 or nivel <= 3:

            #Chama o método para colocar o objeto do paciente dentro da fila de prioridade
            fila_prioritaria.registrar_chamada(paciente)

            #Exibe a mensagem de sucesso confirmando a inserção na fila prioritária
            print(f"🏥 Paciente {paciente.nome_paciente} encaminhado para a FILA PRIORITÁRIA (Gravidade: {nivel}).\n")

        else:
            #Executa este bloco se o paciente não cumprir nenhum critério de prioridade
            fila_comum.registrar_chamada(paciente)

            #Ajuste no print para mostrar a confirmação na tela para o usuário
            print(f"🟢 Paciente {paciente.nome_paciente} encaminhado para a FILA COMUM (Atendimento Normal).\n")

    #Caso o usuário escolha a opção 2 (Atender Próximo Paciente)
    case "2":

        #Para verificar se uma Fila de Heap tem pacientes, checamos o tamanho da lista interna (.fila_prioritaria)
        if len(fila_prioritaria.fila_prioritaria) > 0:

            #Pega a tupla embrulhada que saiu da fila
            tupla_paciente = fila_prioritaria.chamar_proximo()

            #Desembrulha pegando apenas o objeto Paciente que está na terceira posição (índice 2)
            paciente_chamado = tupla_paciente[2]

            print(f"⚕️ Atendendo Paciente Prioritário: {paciente_chamado.nome_paciente} (Idade: {paciente_chamado.idade})\n")

        #Além disso, checamos se o deque possui elementos usando o tamanho dele (.fila_comum)
        elif len(fila_comum.fila_comum) > 0:

            #Invoca o método para remover e retornar o próximo paciente da fila comum (FIFO)
            paciente_chamado = fila_comum.chamar_proximo()

            #Exibe na tela os dados do paciente comum que está sendo atendido agora
            print(f"🩺 Atendendo Paciente Comum: {paciente_chamado.nome_paciente} (Idade: {paciente_chamado.idade})\n")

        #Se ambas as verificações anteriores falharem, significa que o hospital está sem nenhum paciente aguardando
        else:
            # Exibe a mensagem de alerta informando que não há ninguém nas filas
            print("⚠️ Não há pacientes na fila de espera.\n")

        #Se encontramos um paciente em alguma das duas checagens acima:
        if paciente_chamado is not None:

            #Capturamos o CPF que está armazenado dentro do próprio objeto do paciente que acabou de ser chamado
            cpf_atendido = paciente_chamado.cpf
            
            #Usamos esse CPF para ir direto no nosso dicionário 'hospital' e puxar a pasta completa dele
            pasta_do_paciente = hospital[cpf_atendido]
            
            #Nós usamos o colchete ["pron tuario"]para dizer ao Python: "Ignore os dados básicos (como idade/nome) por um momento. Eu quero esticar a mão especificamente na divisória que guarda a folha de histórico médico."
            prontuario_do_paciente = pasta_do_paciente["prontuario"]
            
            #Solicitamos via teclado os dados médicos da consulta que está acontecendo agora
            sintoma_relatado = input("Digite o sintoma/diagnóstico médico para o prontuário: ")
            
            #Chamamos o método da classe Prontuario que dá o '.append()' no histórico (Pilha do Paciente)
            prontuario_do_paciente.add_Historico(sintoma_relatado, "Consulta Concluída")

            print("📝 Prontuário atualizado no histórico individual com sucesso!\n")

    #Caso o usuário escolha a opção 3 (Buscar Dados do Paciente)
    case "3":
      
      #Solicita ao usuário o número de CPF do paciente que deseja encontrar no banco de dados
      alvo = input("Digite o CPF do paciente que está buscando: ")
      
      #Verifica se a chave do CPF informado existe indexada dentro do dicionário do hospital
      if alvo in hospital:
         
        #'hospital[alvo]' -> Vai no dicionário e abre a pasta do CPF digitado.
        #'['dados']' -> Entra na repartição que guarda o objeto Paciente.
        #'.nome_paciente' -> Puxa o texto do nome que está salvo dentro desse objeto
         print(f"Paciente encontrado: {hospital[alvo]['dados'].nome_paciente}\n")

      #Executa este bloco caso a chave procurada não seja encontrada no dicionário
      else:
         
         #Exibe uma notificação informando que o cadastro não foi localizado
         print("⚠️ Paciente não encontrado com este CPF.\n")

    #Caso o usuário escolha a opção 4 (Ver Histórico do Prontuário)
    case "4":
        
        #Solicita o CPF do paciente que o médico deseja investigar o histórico
        cpf_busca = input("Digite o CPF do paciente para ver o prontuário: ")
        
        #Faz a busca relâmpago no dicionário para ver se esse paciente tem registro no hospital
        if cpf_busca in hospital:
           
            #Puxa a pasta associada ao CPF digitado
            pasta_do_paciente = hospital[cpf_busca]

            #O 'pasta_do_paciente' é a gaveta do CPF, que contém as duas divisórias: {"dados": ..., "prontuario": ...}.
            #Ao digitar '["prontuario"]', nós ignoramos os dados pessoais (nome/idade) e pegamos especificamente o objeto da classe 'Prontuario' que foi guardado lá no momento do cadastro.
            prontuario_do_paciente = pasta_do_paciente["prontuario"]

            #Invoca o método para ler o histórico como Pilha
            prontuario_do_paciente.exibir_prontuario_completo()

    #Caso seja 5
    case "5":
      #Exibe mensagem de encerramento
      print("Saindo do sistema...\n")

      #Quebra o loop 'while True', finalizando o programa
      break

    #Caso seja nenhuma das opções acima
    case _:
      #O '_' funciona como um "default" (caso não seja nenhuma das opções anteriores)
      print("Opção inválida! Por favor, digite um número de 1 a 5")