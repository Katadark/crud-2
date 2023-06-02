from models.client import Client
from models.motorcycle import Motorcycle
from database import create_tables

# Chama a função para criar as tabelas
create_tables()


def main():
    while True:
        print("Escolha uma opção:")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Excluir cliente")
        print("4. Cadastrar motocicleta")
        print("5. Listar motocicletas")
        print("6. Excluir motocicleta")
        print("0. Sair")

        option = input("Opção: ")

        if option == "1":
            name = input("Nome: ")
            cpf = input("CPF: ")
            telephone = input("Telefone: ")
            client = Client(name, cpf, telephone)
            client.register()
        elif option == "2":
            Client.list()
        elif option == "3":
            id_client = input("ID do client a ser excluído: ")
            Client.delete(id_client)
        elif option == "4":
            brand = input("Marca: ")
            model = input("Modelo: ")
            year = input("Ano: ")
            value = input("Valor: R$ ")
            motorbike = Motorcycle(brand, model, year, value)
            motorbike.register()
        elif option == "5":
            Motorcycle.list()
        elif option == "6":
            id_motorbike = input("ID da motocicleta a ser excluída: ")
            Motorcycle.delete(id_motorbike)
        elif option == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
