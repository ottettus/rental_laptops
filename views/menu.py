from controllers.rental_service import RentalServices
from models.laptops import Laptop
from models.clients import Client
from models.rental import Rental


class Menu:
    def __init__(self):
        self.rental_services = RentalServices()
        self.rental = Rental

    def display_menu(self):

        print("1.Add new client")
        print("2.Delete client")
        print("3.View all clients")
        print("4.View all laptops")
        print("5.Add new laptop")
        print("6.Delete Laptop")
        print("7.Rent laptop")
        print("8.Exit")


    def choice(self):
        
        while True:
            self.display_menu()
            choice = int(input("Choice an option: "))

            if choice == 1:
                self.add_client()
            elif choice == 2:
                self.delete_client()
            elif choice == 3:
                self.all_clients_list()
            elif choice == 4:
                self.all_laptops_list()
            elif choice == 5:
                self.option_add_new_laptop_to_list()
            elif choice == 6:
                self.delete_laptop()
            elif choice == 7:
                self.rent_laptop()
            elif choice == 8:
                print("exiting...")
                break
            else:
                print("Invalid choice!")

    def add_client(self):
        print("Input data: ")
        name = input("Name: ")
        surname = input("Surname: ")
        email = input("Emial: ")
        self.rental_services.new_client(name, surname, email)


    def delete_client(self):
        id = input("Input ID to delete")
        self.rental_services.delete_client(id)


    def view_all_clients(self):
        print("All clients:")
        all_clients = self.rental_services.get_all_clients()
        Client.display_all_clients(all_clients)


    def all_laptops_list(self):
        print("All laptops list:")
        self.rental_services.view_all_laptops()
    

    def all_clients_list(self):
        print("All clients list")
        self.rental_services.View_all_clients()


    def option_add_new_laptop_to_list(self):
        mark = input("Mark: ")
        model = input("Model: ")
        spec = input("Spec: ")
        self.rental_services.new_laptop(mark, model, spec)


    def delete_laptop(self):
        id_to_delete = input("Input ID: ")
        self.rental_services.delete_laptop(id_to_delete)

    
    def rent_laptop(self):
        id_client = input("input client id:")
        id_laptop = input("Input laptop id:")
        self.rental_services.laptop_rent_ser(id_client,id_laptop)




