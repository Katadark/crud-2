from models.client import Client
from models.motorcycle import Motorcycle
from models.sale import Sale
from database import create_tables

# Chama a função para criar as tabelas
create_tables()


def main():
    while True:
        print("ESCOLHA UMA OPÇÃO:")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Excluir cliente")
        print("4. Cadastrar motocicleta")
        print("5. Listar motocicletas")
        print("6. Excluir motocicleta")
        print("7. Editar cliente")
        print("8. Editar motocicleta")
        print("9. Registrar venda")
        print("10. Listar vendas")
        print("11. Consultar venda")
        print("0. Sair")
        print("------------------------")

        option = input("Opção: ")

        if option == "1":
            name = input("Nome: ")
            cpf = input("CPF: ")
            telephone = input("Telefone: ")
            client = Client(None, name, cpf, telephone)
            client.register()
        elif option == "2":
            Client.list()
        elif option == "3":
            id_client = input("ID do cliente a ser excluído: ")
            Client.delete(id_client)
        elif option == "4":
            brand = input("Marca: ")
            model = input("Modelo: ")
            year = input("Ano: ")
            price = float(input("Valor: R$ "))
            motorbike = Motorcycle(None, brand, model, year, price)
            motorbike.register()
        elif option == "5":
            Motorcycle.list()
        elif option == "6":
            id_motorbike = input("ID da motocicleta a ser excluída: ")
            Motorcycle.delete(id_motorbike)
        elif option == "7":
            id_client = input("ID do cliente a ser atualizado: ")

            # Verifica se o cliente existe
            if not Client.exists(id_client):
                print(">>Cliente com o ID fornecido não existe!<<")
                continue

            # Solicita os novos dados do cliente
            name = input("Novo Nome: ")
            cpf = input("Novo CPF: ")
            telephone = input("Novo Telefone: ")

            # Cria a instância do cliente com os novos dados
            client = Client(id_client, name, cpf, telephone)
            client.update()
        elif option == "8":
            id_motorcycle = input("ID da motocicleta a ser atualizada: ")

            # Verifica se a motocicleta existe
            if not Motorcycle.exists(id_motorcycle):
                print(">>Motocicleta com o ID fornecido não existe!<<")
                continue

            # Solicita os novos dados da motocicleta
            brand = input("Nova marca: ")
            model = input("Novo modelo: ")
            year = input("Novo ano: ")
            price = float(input("Novo preço: R$ "))
            motorcycle = Motorcycle(id_motorcycle, brand, model, year, price)
            motorcycle.update()
        elif option == "9":
            id_client = input("ID do cliente: ")
            id_motorcycle = input("ID da motocicleta: ")
            sale_date = input("Data da venda (formato: dd/mm/aaaa): ")


            # Verifica se o cliente e a motocicleta existem
            if not Client.exists(id_client):
                print(">>Cliente com o ID fornecido não existe!<<")
                continue

            if not Motorcycle.exists(id_motorcycle):
                print(">>Motocicleta com o ID fornecido não existe!<<")
                continue

            # Cria a instância da venda
            sale = Sale(None, id_client, id_motorcycle, sale_date)
            sale.register()
        elif option == "10":
            Sale.list()
        elif option == "11":
            id_sale = input("ID da venda a ser consultada: ")
            Sale.get_sale(id_sale)


if __name__ == "__main__":
    main()
