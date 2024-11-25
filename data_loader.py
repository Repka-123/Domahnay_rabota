def load_data(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return [int(x.strip()) for x in data]
