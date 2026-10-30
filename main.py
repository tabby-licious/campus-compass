from resources import resources

def show_menu():
    print("\n===== Campus Compass =====")
    print("1. Emergency contacts and help")
    print("2. Find resources by category")
    print("3. Search resources by keyword")
    print("4. View my favorite resources")
    print("5. Browse all campus resources")
    print("6. Exit Campus Compass")    

def main():
    print("Welcome to Campus Compass!")
    running = True
    while running:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            print("Emergency contacts and help coming soon.")
        elif choice == "2":
            print("Find resources by category coming soon.")
        elif choice == "3":
            print("Search by keyword coming soon.")
        elif choice == "4":
            print("My favorites resources coming soon.")
        elif choice == "5":
            print("Browse all campus resources coming soon.")
        elif choice == "6":
            print("Exiting Campus Compass...")
            running = False
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()