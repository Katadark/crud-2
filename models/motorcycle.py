from database import get_db


class Motorcycle:
    def __init__(self, brand, model, year, value):
        self.brand = brand
        self.model = model
        self.year = year
        self.value = value

    def register(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO motorcycles (brand, model, year, value) "
                       "VALUES (?, ?, ?, ?)",
                       (self.brand, self.model, self.year, self.value))
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
