from database import get_db

class Motorcycle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def register(self):
        db = get_db()
        cursor = db.cursor()
        sql = "INSERT INTO motorcycle (brand, model, year) VALUES (%s, %s, %s)"
        values = (self.brand, self.model, self.year)
        cursor.execute(sql, values)
        db.commit()
        print("Motocicleta cadastrada com sucesso!")

    @staticmethod
    def list():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM motorcycle")
        motorcycles = cursor.fetchall()
        for motorcycle in motorcycles:
            print(f"ID: {motorcycle[0]}")
            print(f"Marca: {motorcycle[1]}")
            print(f"Modelo: {motorcycle[2]}")
            print(f"Ano: {motorcycle[3]}")
            print("------------------------")

    @staticmethod
    def delete(id_motorcycle):
        db = get_db()
        cursor = db.cursor()
        sql = "DELETE FROM motorcycle WHERE id_motorcycle = %s"
        values = (id_motorcycle,)
        cursor.execute(sql, values)
        db.commit()
        print("Motocicleta excluída com sucesso!")
