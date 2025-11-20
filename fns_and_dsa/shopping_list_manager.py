def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").lower()

        if choice == '1':
            item = input("Enter the item to add: ").lower()
            shopping_list.append(item)
            print(f'You have added {item} to your list')
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input('Enter item: ').lower()
            try: 
                shopping_list.remove(item)
                print(f'You have removed {item} from your cart')
            except ValueError:
                print('Item not in the list')
            pass
        elif choice == '3':
            # Display the shopping list
            for item in shopping_list:
                print(item)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()