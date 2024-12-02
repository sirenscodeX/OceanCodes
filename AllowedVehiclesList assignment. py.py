AllowedVehiclesList = ['Ford F-150','Chevrolet Silverado','Tesla Cybertruck','Toyota Tundra','Nisan Titan']
def print_menu():
    print("\nCartinder Menu:")
    print("1. Print all allowed vehicles")
    def print_vehicles():
        print("\nAllowed Vehicles:")
        for vehicle in AllowedVehiclesList:
            print(vehicle)
            def main():
                while True:
                    print_menu()
                    choice = input ("Enter your choice:")
                    if choice == "1":
                        print_vehicles()
                    elif choice == "2":
                        print("Exiting Cartinder.Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please try again.")
                        if __name__ == "main":
                            main()
                            
                        
                            