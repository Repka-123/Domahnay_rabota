def save_data(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")
