import os

def display_menu():
    print("\nNote-taking App Menu:")
    print("1. Create a new note")
    print("2. View all notes")
    print("3. Search for a note")
    print("4. Exit")

def create_note():
    note_title = input("Enter note title: ")
    note_content = input("Enter note content: ")

    with open(f"{note_title}.txt", "w") as file:
        file.write(note_content)
    print("Note created successfully!")

def view_all_notes():
    notes = [note for note in os.listdir() if note.endswith(".txt")]
    
    if notes:
        print("\nList of available notes:")
        for note in notes:
            print(f"- {note[:-4]}")
    else:
        print("No notes found.")

def search_note():
    search_term = input("Enter search term: ").lower()
    notes = [note for note in os.listdir() if note.endswith(".txt")]
    found_notes = []

    for note in notes:
        with open(note, "r") as file:
            content = file.read().lower()
            if search_term in content:
                found_notes.append(note[:-4])

    if found_notes:
        print("\nFound notes matching the search:")
        for note in found_notes:
            print(f"- {note}")
    else:
        print("No matching notes found.")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            create_note()
        elif choice == "2":
            view_all_notes()
        elif choice == "3":
            search_note()
        elif choice == "4":
            print("Exiting the Note-taking App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
