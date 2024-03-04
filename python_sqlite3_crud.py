import sqlite3
from time import sleep

#Cria um banco de dados.
banco = sqlite3.connect("Banco.db")

#Criação do cursor que é responsável por possibilitar executarmos os comandos SQL.
cursor = banco.cursor()

#Cria uma tabela.
def criar_tabela() -> str:
    """
    Cria uma tabela com o nome desejado pelo usuário.
    :return:O retorno será o nome da tabela em formato de string.
    """
    nome_tabela = str(input("Qual será o nome da sua tabela? ")).lower()
    comando = f"CREATE TABLE IF NOT EXISTS {nome_tabela}(id integer primary key AUTOINCREMENT," \
              f"Nome varchar(20) not null," \
              f"Sobrenome varchar(20) not null," \
              f"Idade integer not null," \
              f"Sexo varchar(20) not null," \
              f"Email varchar(50) not null)"
    cursor.execute(comando)
    banco.commit()
    print("Tabela criada com sucesso!")
    return nome_tabela

#Cria e adiciona dados referentes a uma entidade/pessoa.
def create(nome_tabela) -> None:
    """
    Cria e adiciona dados referente a uma entidade/pessoa em sua tabela.
    :param nome_tabela: Aqui vai a sua tabela para que a criação e adicição de dados seja feita de forma correta.
    :return: Não há retorno (None).
    """
    while True:
        try:
            nome = str(input("Nome: ")).lower()
            sobrenome = str(input("Sobrenome: ")).lower()
            idade = int(input("Idade: "))
            sexo = str(input("Sexo: ")).lower()
            email = str(input("Email: "))
            comando = f"INSERT INTO {nome_tabela}(Nome, Sobrenome, Idade, Sexo, Email)" \
                      f"Values('{nome}','{sobrenome}',{idade},'{sexo}','{email}')"
            cursor.execute(comando)
            banco.commit()
            print("Dado criado com sucesso!")
            break
        except ValueError:
            print("Ocorreu um problema: dado na idade incorreto.\n"
                  "Por favor, tente novamente!")

#Lê todos os dados da sua tabela.
def read(nome_tabela) -> None:
    """
    Lê todos os dados da sua tabela e os mostra na tela.
    :param nome_tabela: Aqui vai o nome da sua tabela para que a função possa acessá-la e ler os dados.
    :return: Não há retorno (None).
    """
    comando = f"SELECT * FROM {nome_tabela}"
    cursor.execute(comando)
    print(cursor.fetchall())

#Atualiza algum dado específico de uma determinada entidade/pessoa.
def update(nome_tabela) -> None:
    """
    Atualiza os dados de uma entidade/pessoa em sua tabela.
    :param nome_tabela: Aqui vai o nome da sua tabela para que a função possa acessá-la e editar os dados.
    :return: Não há retorno (None).
    """
    while True:
        try:
            id = str(input("Qual é o id da pessoa? "))
            coluna = str(input("Qual o nome da coluna que você deseja atualizar? ")).lower()
            if coluna == "idade":
                dado = int(input("Novo dado: "))
            else:
                dado = str(input("Novo dado: "))
            comando = f"UPDATE {nome_tabela} SET {coluna} = '{dado}' WHERE id = {id}"
            cursor.execute(comando)
            banco.commit()
            print("Dado atualizado com sucesso!")
            break
        except ValueError:
            print("Ocorreu um problema: dado 'idade' incorreto.\n"
                  "Por favor, tente novamente!")
            sleep(2)
        except sqlite3.OperationalError:
            print("Digite o NOME da coluna que deseja atualizar.")
            sleep(2)

#Deleta todos os dados de uma entidade/pessoa.
def delete(nome_tabela) -> None:
    """
    Deleta todos os dados de uma entidade/pessoa específica baseado no id.
    :param nome_tabela: Aqui vai o nome da sua tabela para que a função possa acessá-la deletar todos os dados.
    :return: Não há retorno (None).
    """
    try:
        id = str(input("Qual é o id da pessoa? "))
        comando = f"DELETE FROM {nome_tabela} WHERE id = {id}"
        cursor.execute(comando)
        banco.commit()
        print("Dado deletado com sucesso!")
    except ValueError:
        print("Ocorreu um erro: Alguma informação foi fornecida de forma errada.\n"
              "Por favor, tente novamente.")

#imprime na tela a apresentação do programa.
def apresentacao() -> None:
    """
    Imprime uma tela de apresentação do programa.
    :return: Não há retorno (None).
    """
    print("-" * 16)
    print("| Sistema CRUD |")
    print("-" * 16)

#Permite ao usuário escolher uma das opções CRUD ou sair do programa.
def opcao_crud() -> int:
    """
    Solicita ao usuário que escolha uma opção do CRUD.
    :return: Retorna a opção fornecida pelo usuário (int).
    """
    while True:
        try:
            opcao = int(input("Escolha uma das opções abaixo:\n"
                              "[1]Criar dado.\n"
                              "[2]Ler dados.\n"
                              "[3]Atualizar dados.\n"
                              "[4]Deletar dados.\n"
                              "[0]Sair.\n"
                              "Opção: "))
            return opcao
        except ValueError:
            print("Dado inválido. Por favor, tente novamente.")
            sleep(2)

#Executa de fato o programa.
if __name__ == "__main__":
    apresentacao()
    sleep(2)
    nome_tabela = criar_tabela()
    sleep(2)
    while True:
            opcao = opcao_crud()
            if opcao == 1:
                create(nome_tabela)
                sleep(2)
            elif opcao == 2:
                read(nome_tabela)
                sleep(2)
            elif opcao == 3:
                update(nome_tabela)
                sleep(2)
            elif opcao == 4:
                delete(nome_tabela)
                sleep(2)
            elif opcao == 0:
                print("Até a próxima!")
                sleep(2)
                cursor.close()
                banco.close()
                break
            else:
                print("Opção inválida. Por favor, tente novamente!")
                sleep(2)