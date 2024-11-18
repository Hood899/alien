import json

# Nom du fichier pour stocker les données
filename = 'people_info.json'

# Fonction pour charger les données à partir du fichier
def load_data():
    try:
        with open(filename, 'r') as file:
            return json.load(file)  # Lire et convertir le JSON en dictionnaire
    except FileNotFoundError:
        return []  # Retourne une liste vide si le fichier n'existe pas

# Fonction pour sauvegarder les données dans le fichier
def save_data(data):
    with open(filename, 'w') as file:
        json.dump(data, file)  # Convertit le dictionnaire en JSON et l'écrit dans le fichier

# Fonction pour demander le mot de passe
def check_password():
    password = "yellow"  # Remplacez par le mot de passe souhaité
    attempts = 2  # Nombre de tentatives autorisées

    while attempts > 0:
        entered_password = input("Enter the password to access the program: ")
        if entered_password == password:
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. You have {attempts} attempts left.")
    
    print("Access denied!")
    return False

# Vérification du mot de passe avant d'accéder au programme
if check_password():
    # Charge les données existantes
    people_info = load_data()

    while True:
        name = input("Enter the name of the person (or 'quit' to exit): ")
        if name.lower() == 'quit':
            break

        age = input("Enter the age of the person: ")
        city = input("Enter the city of the person: ")

        # Créer un dictionnaire pour la nouvelle personne
        person = {
            'name': name,
            'age': age,
            'city': city
        }

        # Ajouter la nouvelle personne à la liste
        people_info.append(person)

    # Sauvegarder les données mises à jour dans le fichier
    save_data(people_info)

    # Afficher toutes les personnes enregistrées
    print("\nPeople Information:")
    for person in people_info:
        print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")
