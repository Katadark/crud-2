from database import get_db


class Sale:
    def __init__(self, id_sale, id_client, id_motorcycle, sale_date):
        self.id_sale = id_sale
        self.id_client = id_client
        self.id_motorcycle = id_motorcycle
        self.sale_date = sale_date

    def register(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO sales (id_client, id_motorcycle, sale_date) "
                       "VALUES (?, ?, ?)",
                       (self.id_client, self.id_motorcycle, self.sale_date))
        db.commit()
        print("Venda registrada com sucesso!")

    @staticmethod
    def list():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT sales.id_sale, sales.sale_date, "
                       "clients.name, clients.cpf, clients.telephone,"
                       "motorcycles.brand, motorcycles.model, motorcycles.year, motorcycles.price "
                       "FROM sales "
                       "INNER JOIN clients ON sales.id_client = clients.id_client "
                       "INNER JOIN motorcycles ON sales.id_motorcycle = motorcycles.id_motorcycle")
        sales = cursor.fetchall()

        if not sales:
            print("Não há vendas registradas.")
        else:
            print("Lista de Vendas:")
            for sale in sales:
                print(f"ID da Venda: {sale[0]}")
                print(f"Data da Venda: {sale[1]}")
                print(f"Nome do Cliente: {sale[2]}")
                print(f"CPF do Cliente: {sale[3]}")
                print(f"Telefone do Cliente: {sale[4]}")
                print(f"Marca da Motocicleta: {sale[5]}")
                print(f"Modelo da Motocicleta: {sale[6]}")
                print(f"Ano da Motocicleta: {sale[7]}")
                print(f"Valor da Motocicleta: R${sale[8]}")
                print("------------------------")

    @staticmethod
    def get_sale(id_sale):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT sales.id_sale, sales.sale_date, "
                       "clients.name, clients.cpf, clients.telephone,"
                       "motorcycles.brand, motorcycles.model, motorcycles.year, motorcycles.price "
                       "FROM sales "
                       "INNER JOIN clients ON sales.id_client = clients.id_client "
                       "INNER JOIN motorcycles ON sales.id_motorcycle = motorcycles.id_motorcycle "
                       "WHERE sales.id_sale = ?",
                       (id_sale,))
        sale = cursor.fetchone()

        if sale is None:
            print(">>Venda não encontrada!<<")
        else:
            print("Detalhes da Venda:")
            print(f"ID da Venda: {sale[0]}")
            print(f"Data da Venda: {sale[1]}")
            print(f"Nome do Cliente: {sale[2]}")
            print(f"CPF do Cliente: {sale[3]}")
            print(f"Telefone do Cliente: {sale[4]}")
            print(f"Marca da Motocicleta: {sale[5]}")
            print(f"Modelo da Motocicleta: {sale[6]}")
            print(f"Ano da Motocicleta: {sale[7]}")
            print(f"Valor da Motocicleta: R${sale[8]}")
            print("------------------------")
