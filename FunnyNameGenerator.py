import random

class FunnyNameGenerator:
    __adjectives = {
        "Happy": [0, 0],
        "Cheerful": [0, 0],
        "Grumpy": [0, 0],
        "Sleepy": [0, 0],
        "Bright": [0, 0],
        "Sassy": [1, 0],
        "Mighty": [0, 0],
        "Cuddly": [1, 0],
        "Bold": [0, 0],
        "Fuzzy": [1, 0],
        "Crazy": [0, 0],
        "Quirky": [1, 0],
    }

    __names = {
        "Dragon": [0, 0],
        "Unicorn": [1, 0],
        "Goblin": [0, 0],
        "Fairy": [1, 0],
        "Wolf": [0, 0],
        "Phoenix": [0, 0],
        "Mermaid": [1, 0],
        "Elf": [0, 0],
        "Troll": [0, 0],
        "Pixie": [1, 0],
        "Ogre": [0, 0],
    }

    def __get_gender(self):
        return random.choice([0, 1])

    def __filter_available(self, dictionary, gender):
        return [key for key, values in dictionary.items() if values[0] == gender and values[1] == 0]

    def __reduce_counters(self, dictionary):
        for key in dictionary:
            if dictionary[key][1] > 0:
                dictionary[key][1] -= 1

    def __rollback(self, adjective, name):
        self.__adjectives[adjective][1] = 7
        self.__names[name][1] = 7

    def __pick_random(self, items):
        return random.choice(items)

    def __validate_gender(self, gender):
        if gender == "random":
            return self.__get_gender()
        elif gender == "male":
            return 0
        elif gender == "female":
            return 1
        else:
            raise ValueError("Invalid gender input. Choose 'random', 'male', or 'female'.")

    def generate_name(self, gender="random"):
        gender = self.__validate_gender(gender)
        self.__reduce_counters(self.__adjectives)
        self.__reduce_counters(self.__names)
        adjectives = self.__filter_available(self.__adjectives, gender)
        names = self.__filter_available(self.__names, gender)
        if not adjectives or not names:
            raise ValueError("No available names or adjectives. Reset required.")
        adjective = self.__pick_random(adjectives)
        name = self.__pick_random(names)
        self.__rollback(adjective, name)
        return f"{adjective} {name}"
