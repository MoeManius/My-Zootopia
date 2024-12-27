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


def main():
    # Load data and template
    animals_data = load_data('animals_data.json')
    template = read_template('animals_template.html')

    # Generate animal info string
    animal_info = generate_animal_info(animals_data)

    # Create the new HTML content
    new_html_content = create_html(template, animal_info)

    # Write the new HTML content to a file
    write_html('animals.html', new_html_content)


if __name__ == "__main__":
    main()
