# Campus Compass
# A text-based directory of Angelo State University resources.
# Features: emergency help, browse, search by category or keyword, favorites.
# Author: Tabitha Ondieki    Course: CS 1314

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

# List of favorite resources
FAVORITES = []

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
    offer_to_save(resources)

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

    matches = []
    for resource in resources:
        if resource["category"] == selected:
            matches.append(resource)

    if not matches:
        print("No resources found in that category.")
        return

    for number, resource in enumerate(matches, start=1):
        show_resource(resource, number)
    offer_to_save(matches)

# Search resources by keyword
def search_resources_by_keyword():
    """ Search names, categories, tags, and quotes for a word."""
    print("\n=== Search Resources by Keyword ===")
    keyword = input("Enter a word to search for: ").strip().lower()

    if keyword == "":
        print("Please enter a word to search for.")
        return

    matches = []
    for resource in resources:
        tags_text = " ".join(resource["tags"])
        search_text = (
            resource["name"] + " "
            + resource["category"] + " "
            + tags_text + " "
            + resource["notes"]
        ).lower()
        if keyword in search_text:
            matches.append(resource)

    if not matches:
        print(f"No resources found containing the word '{keyword}'.")
        return

    for number, resource in enumerate(matches, start=1):
        show_resource(resource, number)
    offer_to_save(matches)

# View my favorite resources
def add_to_favorites(resource):
    """ Add a resource to the favorites list unless it is already there."""
    if resource in FAVORITES:
        print(f"{resource['name']} is already in your favorites.")
    else:
        FAVORITES.append(resource)
        print(f"Added '{resource['name']}' to your favorites.")

def offer_to_save(results):
    """After showing results, let the user save one by its number."""
    if not results:
        return

    choice = input("\nEnter a number to save to favorites, or press Enter to skip: ").strip()  
    if choice == "":
        return
    if not choice.isdigit():
        print("Please enter a number from the list.")
        return
    number = int(choice)
    if number < 1 or number > len(results):
        print(f"Please enter a number between 1 and {len(results)}.")
        return
    add_to_favorites(results[number - 1])

# View my favorite resources
def show_favorites():
    """ Show saved favorite resources, and let the user remove one"""
    print("\n=== My Favorite Resources ===")
    if not FAVORITES:
        print("You have no favorite resources yet. Save some from browse, category, or search screen.")
        return
    
    for number, resource in enumerate(FAVORITES, start=1):
        show_resource(resource, number)

    choice = input("\nEnter a number to remove a favorite, or press Enter to go back: ").strip()
    if choice == "":
        return
    if not choice.isdigit():
        print("Please enter a number from the list.")
        return
    number = int(choice)
    if number < 1 or number > len(FAVORITES):
        print(f"Please enter a number between 1 and {len(FAVORITES)}.")
        return
    removed = FAVORITES.pop(number - 1)
    print(f"Removed '{removed['name']}' from your favorites.")

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
            show_favorites()
        elif choice == "6":
            print("Exiting Campus Compass...")
            running = False
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
