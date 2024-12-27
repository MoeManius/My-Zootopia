import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_template(file_path):
    """ Reads the HTML template file """
    with open(file_path, "r") as handle:
        return handle.read()


def generate_animal_info(data):
    """ Generates a string with the animal data """
    output = ''
    for animal in data:
        if 'name' in animal:
            output += f"Name: {animal['name']}\n"

        characteristics = animal.get('characteristics', {})

        diet = characteristics.get('diet')
        if diet:
            output += f"Diet: {diet}\n"

        locations = animal.get('locations')
        if locations:
            output += f"Location: {locations[0]}\n"

        animal_type = characteristics.get('type')
        if animal_type:
            output += f"Type: {animal_type}\n"

        output += '\n'  # Add newline for better readability

    return output


def create_html(template, animal_info):
    """ Replaces the placeholder in the template with the animal info """
    return template.replace('__REPLACE_ANIMALS_INFO__', animal_info)


def write_html(file_path, content):
    """ Writes the content to a new HTML file """
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
