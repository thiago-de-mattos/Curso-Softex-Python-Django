import sqlite3
from datetime import datetime
from database import DatabaseConnection

class BlogModel:
    def __init__(self):    
        self.db_conn = DatabaseConnection()
        self._create_table_blog()

    def _create_table_blog(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS blogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuarios interger,
                titulo TEXT NOT NULL,
                conteudo TEXT NOT NULL,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DATETIME DEFAULT CURRENT_TIMEST,
                Foreign Key (id_usuarios) references usuarios(usuarios)
            );
        """
        )
        self.db_conn.close()

    def create_user(self, titulo, conteudo):
        """Cria um novo usuário."""
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                """
                INSERT INTO usuarios (titulo, conteudo)
                VALUES (?, ?);
            """,
                (titulo, conteudo),
            )
            print("Usuário criado com sucesso!")
        except sqlite3.IntegrityError:
            print(f"Erro: O e-mail '{titulo}' já está em uso.")
        finally:
            self.db_conn.close()

    
    def find_user_by_id(self, id_usuarios):
        """Busca um usuário pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM usuarios WHERE id = ?;", (id_usuarios,))
        user = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return user

    def update_user_by_id(self, id_usuarios, titulo=None, conteudo=None):
        """Atualiza informações de um usuário pelo ID."""
        self.db_conn.connect()
        updates = []
        params = []
        if titulo:
            updates.append("titulo = ?")
            params.append()
        if conteudo:
            updates.append("conteudo = ?")
            params.append(conteudo)

        if not updates:
            print("Nenhum dado para atualizar.")
            self.db_conn.close()
            return

        updates.append("data_atualizacao = ?")
        params.append(datetime.now())
        params.append(id_usuarios)
        query = f"UPDATE usuarios SET {', '.join(updates)} WHERE id = ?;"

        self.db_conn.cursor.execute(query, params)
        print("Usuário atualizado com sucesso!")
        self.db_conn.close()