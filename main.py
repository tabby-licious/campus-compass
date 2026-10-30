from resources import resources

def show_menu():
    print("\n===== Campus Compass =====")
    print("1. Emergency contacts and help")
    print("2. Browse all campus resources")
    print("3. Find resources by category")
    print("4. Search resources by keyword")
    print("5. View my favorite resources")
    print("6. Exit Campus Compass")    

def browse_all_resources():
    print("\n=== All Campus Resources ===")
    for number, resource in enumerate(resources, start=1):
        print(f"\n{number}. {resource['name']}")
        print(f"Category: {resource['category']}")
        print(f"Location: {resource['location']}")
        print(f"Hours: {resource['hours']}")
        print(f"Contact: {resource['contact']}")
        print(f"Notes: {resource['notes']}")    

def main():
    print("Welcome to Campus Compass!")
    running = True
    while running:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            print("Emergency contacts and help coming soon.")
        elif choice == "2":
            browse_all_resources()
        elif choice == "3":
            print("Find resources by category coming soon.")
        elif choice == "4":
            print("Search resources by keyword coming soon.")
        elif choice == "5":
            print("My favorites resources coming soon.")
        elif choice == "6":
            print("Exiting Campus Compass...")
            running = False
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()