Laptop Rental System

A simple laptop rental management system using Python and PostgreSQL.

📌 Features

✅ Add and remove laptops
✅ Rent and return laptops
✅ Automatic status updates for laptops
✅ Check laptop availability
✅ PostgreSQL database integration

🔧 Technologies Used

Python (OOP, psycopg2)
PostgreSQL + pgAdmin
MVC architecture
🛠 Installation

How to Restore the Database

To restore the database for this project, follow these steps:

Download the Database Backup:
The backup file is available in this repository under the name rental_laptops_db.dump.
Install PostgreSQL:
If you don't have PostgreSQL installed on your machine, please install it. Follow the instructions here:
PostgreSQL Installation Guide.
Create a New Database:
Before restoring the backup, create a new database where the data will be loaded. You can do this through pgAdmin or using the command line.
To create a new database from the command line, use the following command (replace your_database_name with your desired database name):

createdb your_database_name
Restore the Backup:
After the new database is created, restore the backup by running the following command:
pg_restore -U your_username -d your_database_name /path/to/rental_laptops_db.dump
Replace your_username with your PostgreSQL username.
Replace your_database_name with the name of the database you created.
Replace /path/to/rental_laptops_db.dump with the actual path to the backup file.
Example command:

pg_restore -U postgres -d rental_laptops /path/to/rental_laptops_db.dump
Check the Data:
Once the restore is complete, you should see all the tables and data loaded into the new database. You can check this using pgAdmin or by running SQL queries in your terminal.
Known Issues:
If you encounter an error with foreign key constraints (e.g., rentals_laptop_id_fkey already exists), you can ignore it for now as the database was still loaded successfully.

Clone the repository:
git clone https://github.com/your-repo/laptop_rental.git
cd laptop_rental
Install dependencies:
pip install -r requirements.txt
Set up the PostgreSQL database and create the required tables (you can include an SQL schema in schema.sql).
🚀 How to Use

Run the application:

python main.py
Follow the instructions in the menu to manage laptops and rentals.

📂 Project Structure

laptop_rental/
│── database/
│   ├── db.py           # Handles database connection
│── models/
│   ├── rental.py       # Handles rental operations
│   ├── laptops.py      # Handles laptop operations
│── controllers/
│   ├── rental_service.py # Business logic for rentals
│── views/
│   ├── menu.py         # CLI interface
│── main.py             # Entry point of the program
│── README.md           # Project documentation
│── requirements.txt    # Dependencies
│── rental_laptops_db.dump    # Database backup for pgAdmin4



📝 Future Improvements

Add a graphical user interface (GUI)
Implement user authentication
Generate rental history reports
📜 License

This project is licensed under the MIT License.
