"""
    Programa gerencial facilitador para gerente, retorna itens da loja, 
    valores dos itens da loja, informações sobre os funcionarios, pagamento dos salarios, 
    demissão, contratação, retirada de produtos, mudança de valor de itens
"""

class Sistema():
    """
        classe de controle de listas dos produtos e funcionarios
    """

    def __init__(self):
        self.prod = []
        self.func = []

    """
        Função para adicionar objetos a lista de produtos
    """
    def adicionar_produto(self,obj):
        self.prod.append(obj)

    """
        Função para adicionar objetos a lista de funcionarios
    """
    def adicionar_funcionario(self,obj):
        self.func.append(obj)

    """
        Função para retornar objetos da lista de produtos
    """
    def retorne_produto(self):
        return self.prod
    
    """
        Função para retornar objetos da lista de Funcionarios
    """
    def retorne_funcionario(self):
        return self.func
    
    """
        Função para excluir produto do sistema
    """
    def remove_produto(self, delet):
        for i in self.prod:
            if i.item == delet:
                self.prod.remove(i)
                return "\nProduto Removido"
        else:
            return "\nProduto não encontrado"
    
    """
        Função para excluir funcionario do sistema
    """
    def remove_funcionario(self, delet):
        for i in self.func:
            if i.nome == delet:
                self.func.remove(i)
                return "\nFuncionario Removido"
        else:
            return "\nFuncionario não encontrado"
        

class Loja():
    """
        Classe de controle dos produtos e valores da loja
    """

    def __init__(self, item, valor):
        self.item = item
        self.valor = valor

    """
        Função para trocar valor de um produto escolhido
    """
    def troca_valor(self, val_novo):
        if val_novo >= 0:
            self.valor = val_novo
            return "\nValor alterado!"
        else:
            return "\nErro numero negativo"
        
    """
        Função para mostrar itens da loja
    """
    def __str__(self):
        return f"\nProduto: {self.item}, Valor: {self.valor}R$"
        

class Funcionario():
    """
        Classe de informações dos funcionarios podendo alterar salarios
    """

    def __init__(self, salario, tempo_trabalho, nome, idade, cpf, cargo):
        self.salario = salario
        self.tempo_trabalho = tempo_trabalho
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cargo = cargo

    """
        Função para trocar salario de um funcionario escolhido
    """
    def troca_sal(self, val_novo):
        if val_novo >= 0:
            self.salario = val_novo
            return f"\nValor alterado para {self.salario}!"
        
        else:
            return "\nErro numero negativo"
        
    """
        Informações de cada funcionario
    """
    def __str__(self):
        return f"\n{self.cargo}:{self.nome}, Idade: {self.idade} anos, CPF: {self.cpf}, Tempo de Trabalho: {self.tempo_trabalho} anos, Salario: {self.salario:.2f}R$"
    

"""
    Função de menu da loja
"""
def menu_loja():
    print("\nBem vindo ao sistema da Loja!")

    while True:
        try:
            opcao_loja = int(input("\nQual opção deseja realizar: 1 - Cadastrar Produto, 2 - Deletar Produto, 3 - buscar, 4 - Mudar Valor, 5 - Mostrar itens cadastrados, 6 - Voltar: "))

        except ValueError:
            print("\nErro")
            continue

        match opcao_loja:
            case 1:
                try:
                    item = input("\nDigite o nome do seu Produto: ")
                    valor = int(input("\nDigite o preço do Produto: "))
                    if valor >= 0:
                        produto = Loja(item, valor)
                        listas.adicionar_produto(produto)
                        print("\nProduto criado")
                    else:
                        print("\nErro")
                        continue

                except ValueError:
                    print("\nErro")
                    continue

            case 2:
                delet = input("\nNome do produto que deseja deletar: ")
                print(listas.remove_produto(delet))
    
            case 3:
                busque = input("\nNome do produto que deseja buscar: ")
                for i in listas.retorne_produto():
                    if i.item == busque:
                        print(i)
                        break
                else:
                    print("\nProduto não encontrato!")
                        
            case 4:
                    item_val = input("\nDigite o nome do produto que deseja trocar o valor: ")
                    for i in listas.retorne_produto():
                        if i.item == item_val:
                            try:
                                valor_nov = float(input("\nDigite o novo valor do Produto: "))
                            
                            except ValueError:
                                print("\nErro, Digite apenas numeros")
                                break

                            print(i.troca_valor(valor_nov))
                            break
                    else:
                        print("\nProduto não encontrato!")       

            case 5:
                if listas.retorne_produto():
                    for i in listas.retorne_produto():
                        print(i)
                else:
                    print("\nNão a Produtos cadastrados ainda")

            case 6:
                break

            case _:
                print("\nErro")

"""
    Função de menu do funcionario
"""
def menu_funcionario():
    print("\nBem vindo ao sistema da Funcionarios!")

    while True:
        try:
            opcao_func = int(input("\nQual opção deseja realizar: 1 - Cadastrar Funcionario, 2 - Demitir Funcionario, 3 - buscar, 4 - Mudar Salario, 5 - Mostrar funcionarios, 6 - Voltar: "))

        except ValueError:
            print("\nErro")
            continue
        
        match opcao_func:
            case 1:
                try:
                    nome = input("\nDigite o nome do funcionario: ")
                    salario = float(input("\nDigite o salario do seu Funcionario: "))
                    temp_trabalho = float(input("\nDigite o tempo de trabalho do funcionario em anos: "))
                    idade = int(input("\nDigite a idade do Funcionario: "))
                    cpf = input("\nDigite o CPF do seu funcionario: ")
                    cargo = input("\nDigite o Cargo do funcionario: ")
            
                    if salario >= 0 and idade >= 0 and temp_trabalho >= 0:
                        pessoa = Funcionario(salario, temp_trabalho, nome, idade, cpf, cargo)
                        listas.adicionar_funcionario(pessoa)
                    else:
                        print("\nErro, salario, tempo de trabalho e idade não podem ser negativos!")

                except ValueError:
                    print("\nErro")

            case 2:
                delet = input("\nNome do Funcionario que deseja demitir: ")
                print(listas.remove_funcionario(delet))

            case 3:
                busque = input("\nNome do Funcionario que deseja buscar: ")
                for i in listas.retorne_funcionario():
                    if i.nome == busque:
                        print(i)
                        break
                else:
                    print("\nFuncionario não encontrato!")
            
            case 4:
                funci = input("\nDigite o Funcionario que deseja alterar o salario: ")
                for i in listas.retorne_funcionario():
                    if i.nome == funci:
                        valor_novo = float(input("\nDigite o novo salario do Funcionario: "))
                        print(i.troca_sal(valor_novo))
                        break
                else:
                    print("\nFuncionario não encontrato!")      

            case 5:
                if listas.retorne_funcionario():
                    for i in listas.retorne_funcionario():
                        print(i)
                else:
                    print("\nNão a Funcionarios cadastrados ainda")

            case 6:
                break

            case _:
                print("\nErro")

print("\n====================================SISTEMA GERENCIAL====================================")

listas = Sistema()

while True:
    try:
        opcao = int(input("\nDigite a opção que dejesa realizar: 1 - Loja, 2 - Funcionario, 3 - Desligar Sistema: "))

        if opcao not in [1,2,3]:
            print("\nErro, Digite apenas 1, 2 ou 3")
            continue

    except ValueError:
        print("\nErro")
        continue

    if opcao == 1:
        menu_loja()

    elif opcao == 2:
        menu_funcionario()
        
    elif opcao == 3:
        break

print("\n====================================FIM DO PROGRAMA====================================\n")