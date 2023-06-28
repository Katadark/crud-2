import sqlite3


def create_tables():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Verifica se a tabela 'clients' já existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clients'")
    clients_table_exists = cursor.fetchone()

    if not clients_table_exists:
        # Criação da tabela 'clients'
        cursor.execute(
            """
            CREATE TABLE clients (
                id_client INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                cpf TEXT NOT NULL,
                telephone TEXT NOT NULL
            )
            """
        )

    # Verifica se a tabela 'motorcycles' já existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='motorcycles'")
    motorcycles_table_exists = cursor.fetchone()

    if not motorcycles_table_exists:
        # Criação da tabela 'motorcycles'
        cursor.execute(
            """
            CREATE TABLE motorcycles (
                id_motorcycle INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL,
                price DECIMAL(10,2) NOT NULL
            )
            """
        )

        # Verifica se a tabela 'sales' já existe
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sales'")
        sales_table_exists = cursor.fetchone()

        if not sales_table_exists:
            # Criação da tabela 'sales'
            cursor.execute(
                """
                CREATE TABLE sales (
                    id_sale INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_client INTEGER NOT NULL,
                    id_motorcycle INTEGER NOT NULL,
                    sale_date TEXT NOT NULL,
                    FOREIGN KEY (id_client) REFERENCES clients (id_client),
                    FOREIGN KEY (id_motorcycle) REFERENCES motorcycles (id_motorcycle)
                )
                """
            )

    conn.commit()
    conn.close()


def get_db():
    conn = sqlite3.connect("database.db")
    return conn
