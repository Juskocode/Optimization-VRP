from typing import List, Type, TypeVar
import csv

# Define a generic type variable for models
Model = TypeVar('Model')

def parse_model(file: str, model: Type[Model]) -> List[Model]:
    """
    Parses a CSV file and returns a list of instances of the specified model class.

    This function reads data from a CSV file, where each row corresponds to an object
    of the specified model class. The model class is expected to have an __init__
    method that matches the CSV file's columns.

    Parameters:
        file (str): The path to the CSV file to be parsed.
        model (Type[Model]): The class of the model to be instantiated for each row of the CSV.

    Returns:
        List[Model]: A list of instances of the specified model, one for each row in the CSV.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ValueError: If the CSV data cannot be parsed into the given model.
    """
    
    models = []
    
    try:
        with open(file, 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            
            # Loop over each row in the CSV and instantiate the model
            for line in reader:
                try:
                    # Unpack line values into the model constructor
                    models.append(model(*line.values()))
                except TypeError as e:
                    raise ValueError(f"Error creating model instance from CSV row: {line}. Error: {e}")

    except FileNotFoundError as e:
        raise FileNotFoundError(f"CSV file '{file}' not found. Please check the file path.") from e

    return models
