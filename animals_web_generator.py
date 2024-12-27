import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    animals_data = load_data('animals_data.json')

    for animal in animals_data:
        if 'name' in animal:
            print(f"Name: {animal['name']}")

        characteristics = animal.get('characteristics', {})

        diet = characteristics.get('diet')
        if diet:
            print(f"Diet: {diet}")

        locations = animal.get('locations')
        if locations:
            print(f"Location: {locations[0]}")

        animal_type = characteristics.get('type')
        if animal_type:
            print(f"Type: {animal_type}")

        print()  # Print a newline for better readability


if __name__ == "__main__":
    main()
