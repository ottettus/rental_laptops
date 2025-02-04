import psycopg2

class Database:
    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname=rental_laptops_db user=postgres")
            self.cursor = self.conn.cursor()
        except psycopg2.Error as e:
            self.conn = None
            self.cursor = None


    def execute_query(self, query: str, params = None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Bad query!: Error: {e}")


    def fetch_query(self, query: str):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except psycopg2.Error as e:
            print(f"Bad fetch! Error: {e}")
            

    def update_laptop_status(self, id, new_status):
        query = "UPDATE laptops SET status = %s WHERE id = %s"
        try:
            self.execute_query(query, (new_status, id))
            print('Status Updated')
        except psycopg2.Error as e:
            print(f"Bad query!: Error: {e}")

