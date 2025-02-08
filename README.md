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
📝 Future Improvements

Add a graphical user interface (GUI)
Implement user authentication
Generate rental history reports
📜 License

This project is licensed under the MIT License.
