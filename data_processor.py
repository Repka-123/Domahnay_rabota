class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        self.data = [x * 2 for x in self.data]
        return self.data

    def filter(self, threshold):
        self.data = [x for x in self.data if x > threshold]
        return self.data
