import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_template(file_path):
    """Reads the HTML template file."""
    with open(file_path, "r") as handle:
        return handle.read()


def serialize_animal(animal):
    """Serializes a single animal object into an HTML list item."""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal.get("name", "Unknown")}</div>\n'
    output += '  <p class="card__text">\n'
    output += '    <ul class="animal-details">\n'

    characteristics = animal.get('characteristics', {})

    diet = characteristics.get('diet')
    if diet:
        output += f'      <li class="animal-detail"><strong>Diet:</strong> {diet}</li>\n'

    locations = animal.get('locations')
    if locations:
        output += f'      <li class="animal-detail"><strong>Location:</strong> {", ".join(locations)}</li>\n'

    animal_type = characteristics.get('type')
    if animal_type:
        output += f'      <li class="animal-detail"><strong>Type:</strong> {animal_type}</li>\n'

    lifespan = characteristics.get('lifespan')
    if lifespan:
        output += f'      <li class="animal-detail"><strong>Lifespan:</strong> {lifespan}</li>\n'

    weight = characteristics.get('weight')
    if weight:
        output += f'      <li class="animal-detail"><strong>Weight:</strong> {weight}</li>\n'

    length = characteristics.get('length')
    if length:
        output += f'      <li class="animal-detail"><strong>Length:</strong> {length}</li>\n'

    output += '    </ul>\n'
    output += '  </p>\n'
    output += '</li>\n'

    return output


def generate_animal_info(data):
    """Generates a string with the animal data in HTML format."""
    return ''.join(serialize_animal(animal) for animal in data)


def create_html(template, animal_info):
    """Replaces the placeholder in the template with the animal info."""
    return template.replace('__REPLACE_ANIMALS_INFO__', animal_info)


def write_html(file_path, content):
    """Writes the content to a new HTML file."""
    with open(file_path, "w") as handle:
        handle.write(content)


def get_unique_skin_types(data):
    """Returns a list of unique skin types from the animals' data."""
    skin_types = set()
    for animal in data:
        skin_type = animal.get('characteristics', {}).get('skin_type')
        if skin_type:
            skin_types.add(skin_type)
    return sorted(skin_types)


def filter_animals_by_skin_type(data, selected_skin_type):
    """Filters the animals by the selected skin type."""
    return [
        animal for animal in data
        if animal.get('characteristics', {}).get('skin_type') == selected_skin_type
    ]


def main():
    # Load data and template
    animals_data = load_data('animals_data.json')
    template = read_template('animals_template.html')

    # Get unique skin types
    skin_types = get_unique_skin_types(animals_data)

    # Display available skin types to the user
    print("Available skin types:")
    for idx, skin_type in enumerate(skin_types, 1):
        print(f"{idx}. {skin_type}")

    # Ask the user to select a skin type
    while True:
        try:
            choice = int(input(f"Select a skin type (1-{len(skin_types)}): "))
            if 1 <= choice <= len(skin_types):
                selected_skin_type = skin_types[choice - 1]
                break
            else:
                print(f"Error: Please enter a number between 1 and {len(skin_types)}.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

    # Filter animals by selected skin type
    filtered_animals = filter_animals_by_skin_type(animals_data, selected_skin_type)

    if filtered_animals:
        # Generate animal info string for the filtered animals
        animal_info = generate_animal_info(filtered_animals)

        # Create the new HTML content
        new_html_content = create_html(template, animal_info)

        # Write the new HTML content to a file
        write_html('animals.html', new_html_content)
        print(f"HTML file generated for animals with skin type '{selected_skin_type}'.")

    else:
        print(f"No animals found with the skin type '{selected_skin_type}'.")


if __name__ == "__main__":
    main()
