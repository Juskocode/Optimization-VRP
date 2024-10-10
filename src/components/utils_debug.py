class Printator:
    """
    Provides a default __str__ method to Python classes, allowing their attributes 
    to be easily converted to a string representation.

    The __str__ method is typically used for generating a human-readable 
    and informal string representation of the object, including its attributes.
    """
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.__dict__}"
