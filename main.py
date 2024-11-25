import data_loader
import data_saver
from data_processor import DataProcessor

def main():
    data = data_loader.load_data('data.txt')
    processor = DataProcessor(data)
    processed_data = processor.process()
    filtered_data = processor.filter(10)
    data_saver.save_data('processed_data.txt', filtered_data)

if __name__ == "__main__":
    main()