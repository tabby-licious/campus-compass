from resources import resources
SAFETY_CATEGORY = "Safety & Emergency Services"
# List of categories for the resources
CATEGORIES = [
    "Academic & Study Resources",
    "Food & Dining",
    "Health & Wellness",
    "Career & Financial Support",
    "Technology & Student Help",
    "Recreation & Campus Life",
    "Safety & Emergency Services",
]
# Show the menu
def show_menu():
    print("\n===== Campus Compass =====")
    print("1. Emergency contacts and help")
    print("2. Browse all campus resources")
    print("3. Find resources by category")
    print("4. Search resources by keyword")
    print("5. View my favorite resources")
    print("6. Exit Campus Compass")    

# Show the resource
def show_resource(resource, number=None):
    """Print one resource. If a number is given, show it before the name."""
    if number is not None:
        print(f"\n{number}. {resource['name']}")
    else:
        print(f"\n{resource['name']}")
    print(f"   Category: {resource['category']}")
    print(f"   Location: {resource['location']}")
    print(f"   Hours: {resource['hours']}")
    print(f"   Contact: {resource['contact']}")
    print(f"   Notes: {resource['notes']}")

# Browse all resources
def browse_all_resources():
    """Show every resource, numbered."""
    print("\n=== All Campus Resources ===")
    if not resources:
        print("No resources are available right now.")
        return
    for number, resource in enumerate(resources, start=1):
        show_resource(resource, number)

# Show the emergency help
def show_emergency_help():
    """Show urgent contacts first, then campus safety resources."""
    print("\n=== EMERGENCY HELP ===")
    print("Life-threatening emergency: call 911")
    print("Suicide & Crisis Lifeline: call or text 988")
    print("\n--- Angelo State safety resources ---")
    found = False
    for resource in resources:
        if resource["category"] == SAFETY_CATEGORY:
            show_resource(resource)
            found = True
    if not found:
        print("No campus safety resources found. In an emergency, call 911.")
        
# Find resources by category
def find_resources_by_category():
    """ Let the user pick a category and show its resources."""
    print("\n=== Find Resources by Category ===")
    for number, category in enumerate(CATEGORIES, start=1):
        print(f"{number}. {category}")

    choice = input("Choose a category: ").strip()

    if not choice.isdigit():
        print("Please enter a number from the list.")
        return
    
    choice = int(choice)
    if choice < 1 or choice > len(CATEGORIES):
        print(f"Please enter a  number between 1 and {len(CATEGORIES)}.")
        return

    selected = CATEGORIES[choice - 1]
    print(f"\n=== Resources in the {selected} category ===")

    count = 0
    for resource in resources:
        if resource["category"] == selected:
            count += 1
            show_resource(resource, count)

    if count == 0:
        print(f"No resources found in the {selected} category.")

# Search resources by keyword
def search_resources_by_keyword():
    """ Search names, categories, tags, and quotes for a word."""
    print("\n=== Search Resources by Keyword ===")
    keyword = input("Enter a word to search for: ").strip().lower()

    if keyword == "":
        print("Please enter a word to search for.")
        return

    count = 0
    for resource in resources:
        tags_text = " ".join(resource["tags"])
        search_text = (
            resource["name"] + " "
            + resource["category"] + " "
            + tags_text.lower() + " "
            + resource["notes"]
        ).lower()

        if keyword in search_text:
            count += 1
            show_resource(resource, count)
    
    if count == 0:
        print(f"No resources found containing the word '{keyword}'.")

# Main function
def main():
    print("Welcome to Campus Compass!")
    running = True
    while running:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            show_emergency_help()
        elif choice == "2":
            browse_all_resources()
        elif choice == "3":
            find_resources_by_category()
        elif choice == "4":
            search_resources_by_keyword()
        elif choice == "5":
            print("My favorites resources coming soon.")
        elif choice == "6":
            print("Exiting Campus Compass...")
            running = False
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()