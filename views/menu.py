from controllers.rental_service import RentalServices
from models.laptops import Laptop
from models.clients import Client


class Menu:
    def __init__(self):
        self.rental_services = RentalServices()

    def display_menu(self):

        print("1.Add new client")
        print("2.Delete client")
        print("3.View all clients")
        print("4.View all laptops")
        print("5.Update laptop status")
        print("6.Exit")


    def choice(self):
        
        while True:
            self.display_menu()
            choice = int(input("Choice an option"))

            if choice == 1:
                print("Input data: ")
                name = input("Name")
                surname = input("Surname")
                email = input("Emial")
                self.rental_services.new_client(name, surname, email)
            elif choice == 2:
                print("All clients:")
                all_clients = self.rental_services.get_all_clients()
                Client.display_all_clients(all_clients)
                id = input("Input ID to delete")
                self.rental_services.delete_client(id)
            elif choice == 3:
                print("All clients:")
                all_clients = self.rental_services.get_all_clients()
                Client.display_all_clients(all_clients)
            elif choice == 4:
                print("All laptops list:")
                all_laptops = self.rental_services.get_all_laptops()
                Laptop.display_all_laptops(all_laptops)
            elif choice == 5:
                print("all_laptops")
                all_laptops = self.rental_services.get_all_laptops()
                Laptop.display_all_laptops(all_laptops)
                id = input("Input ID to delete")
                self.rental_services.delete_laptop(id)
            elif choice == 6:
                print("exiting...")
                break
            else:
                print("Invalid choice!")


