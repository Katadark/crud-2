from database import get_db


class Motorcycle:
    def __init__(self, id_motorcycle, brand, model, year, price):
        self.id_motorcycle = id_motorcycle
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def register(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO motorcycles (brand, model, year, price) "
                       "VALUES (?, ?, ?, ?)",
                       (self.brand, self.model, self.year, self.price))
        db.commit()
        print("Motocicleta cadastrada com sucesso!")

    @staticmethod
    def list():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM motorcycles")
        motorcycles = cursor.fetchall()

        if not motorcycles:
            print(">>Nenhuma motocicleta cadastrada!<<")
        else:
            for motorcycle in motorcycles:
                print(f"ID: {motorcycle[0]}")
                print(f"Marca: {motorcycle[1]}")
                print(f"Modelo: {motorcycle[2]}")
                print(f"Ano: {motorcycle[3]}")
                print(f"Valor: R$ {motorcycle[4]}")
                print("------------------------")


    def update(self):
        db = get_db()
        cursor = db.cursor()

        # Verifica se a motocicleta existe
        sql_select = "SELECT * FROM motorcycles WHERE id_motorcycle = ?"
        cursor.execute(sql_select, (self.id_motorcycle,))
        result = cursor.fetchone()

        if result is None:
            print(">>Motocicleta com o ID fornecido não existe!<<")
        else:
            sql_update = "UPDATE motorcycles SET brand = ?, model = ?, year = ?, price = ? WHERE id_motorcycle = ?"
            values = (self.brand, self.model, self.year, self.price, self.id_motorcycle)
            cursor.execute(sql_update, values)
            db.commit()
            print("Motocicleta atualizada com sucesso!")

    @staticmethod
    def exists(id_motorcycle):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM motorcycles WHERE id_motorcycle = ?", (id_motorcycle,))
        result = cursor.fetchone()
        return result[0] > 0

    @staticmethod
    def delete(id_motorcycle):
        db = get_db()
        cursor = db.cursor()
        sql = "DELETE FROM motorcycles WHERE id_motorcycle = ?"
        values = (id_motorcycle,)
        cursor.execute(sql, values)
        affected_rows = cursor.rowcount
        db.commit()

        if affected_rows == 0:
            print(">>Nenhuma motocicleta encontrada com o ID fornecido!<<")
        else:
            print("Motocicleta excluída com sucesso!")
