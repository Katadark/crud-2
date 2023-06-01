from database import get_db


class Client:
    def __init__(self, name, cpf, telephone):
        self.name = name
        self.cpf = cpf
        self.telephone = telephone

    def register(self):
        db = get_db()
        cursor = db.cursor()
        sql = "INSERT INTO client (name, cpf, telephone) VALUES (%s, %s, %s)"
        values = (self.name, self.cpf, self.telephone)
        cursor.execute(sql, values)
        db.commit()
        print("Cliente cadastrado com sucesso!")

    @staticmethod
    def list():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM client")
        clients = cursor.fetchall()
        for client in clients:
            print(f"ID: {client[0]}")
            print(f"Nome: {client[1]}")
            print(f"CPF: {client[2]}")
            print(f"Telefone: {client[3]}")
            print("------------------------")

    @staticmethod
    def delete(id_client):
        db = get_db()
        cursor = db.cursor()
        sql = "DELETE FROM client WHERE id_client = %s"
        values = (id_client,)
        cursor.execute(sql, values)
        db.commit()
        print("Cliente excluído com sucesso!")
