from database import get_db


class Client:
    def __init__(self, id_client, name, cpf, telephone):
        self.id_client = id_client
        self.name = name
        self.cpf = cpf
        self.telephone = telephone

    def register(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO clients (name, cpf, telephone) "
                       "VALUES (?, ?, ?)",
                       (self.name, self.cpf, self.telephone))
        db.commit()
        print("Cliente cadastrado com sucesso!")
        print("------------------------")

    @staticmethod
    def list():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM clients")
        clients = cursor.fetchall()

        if not clients:
            print(">>Nenhum cliente cadastrado!<<")

        for client in clients:
            print(f"ID: {client[0]}")
            print(f"Nome: {client[1]}")
            print(f"CPF: {client[2]}")
            print(f"Telefone: {client[3]}")
            print("------------------------")

    def update(self):
        db = get_db()
        cursor = db.cursor()
        sql_select = "SELECT * FROM clients WHERE id_client = ?"
        cursor.execute(sql_select, (self.id_client,))
        result = cursor.fetchone()

        if result is None:
            print("Cliente com o ID fornecido não existe!")
        else:
            sql_update = "UPDATE clients SET name = ?, cpf = ?, telephone = ? WHERE id_client = ?"
            values = (self.name, self.cpf, self.telephone, self.id_client)
            cursor.execute(sql_update, values)
            db.commit()
            print("Cliente atualizado com sucesso!")
            print("------------------------")

    @staticmethod
    def exists(id_client):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM clients WHERE id_client = ?", (id_client,))
        result = cursor.fetchone()
        return result[0] > 0

    @staticmethod
    def delete(id_client):
        db = get_db()
        cursor = db.cursor()
        sql = "DELETE FROM clients WHERE id_client = ?"
        values = (id_client)
        cursor.execute(sql, values)
        affected_rows = cursor.rowcount
        db.commit()

        if affected_rows == 0:
            print(">>Nenhum cliente encontrado com o ID fornecido")
        else:
            print("Cliente excluído com sucesso!")
            print("------------------------")


