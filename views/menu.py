from controllers.rental_service import RentalServices


class Menu:
    def __init__(self):
        self.rental_services = RentalServices()

    def display_menu(self):

        print("1.Add new client")
        print("2.Delete client")
        print("3.View all clients")
        print("4.Update laptop status")
        print("5.Exit")


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
                print(all_clients)
                id = input("Input ID to delete")
                self.rental_services.delete_client(id)
            elif choice == 3:
                print("All clients:")
                all_clients = self.rental_services.get_all_clients()
                print(all_clients)
            elif choice == 4:
                print(all_laptops = self.rental_services.get_all_laptops())
                id = input("Input ID to delete")
                self.rental_services.delete_laptop(id)
            elif choice == 5:
                print("exiting...")
                break
            else:
                print("Invalid choice!")


