# Importering af de nødvendige biblioteker
import csv

# Funktion til at tilføje en bog til biblioteket


def add_book():
    title = input("Indtast bogens titel: ")
    author = input("Indtast bogens forfatter: ")
    genre = input("Indtast bogens genre: ")
    year = input("Indtast bogens udgivelsesår: ")
    with open('bibliotek.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, genre, year])
    print("Bogen er tilføjet til biblioteket.\n")

# Funktion til at søge efter en bog i biblioteket


def search_book():
    search_term = input("Indtast søgeord: ")
    with open('bibliotek.csv', 'r') as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            if search_term.lower() in [item.lower() for item in row]:
                print(row)
                found = True
        if not found:
            print("Ingen bøger blev fundet med det angivne søgeord.\n")

# Funktion til at vise alle bøger i biblioteket


def show_all_books():
    with open('bibliotek.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Hovedmenuen for programmet


def main_menu():
    while True:
        print("\n*** Biblioteksprogram ***\n")
        print("1. Tilføj en bog til biblioteket")
        print("2. Søg efter en bog")
        print("3. Vis alle bøger i biblioteket")
        print("4. Afslut programmet")
        choice = input("\nVælg en handling (1-4): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            show_all_books()
        elif choice == "4":
            print("Tak fordi du brugte Biblioteksprogrammet. På gensyn!\n")
            break
        else:
            print("Ugyldigt valg. Prøv igen.\n")


# Kald hovedmenuen for at starte programmet
main_menu()
