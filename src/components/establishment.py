from .utils_debug import Printator
from typing import Tuple, List

class Establishment(Printator):
    """
    Represents an Establishment in the context of a problem involving geographical locations 
    and inspection scheduling. The Establishment class stores details about the establishment's
    location, inspection utility, time required for inspection, and opening hours.

    Attributes:
        id (int): The unique identifier for the establishment.
        district (str): The district where the establishment is located.
        county (str): The county where the establishment is located.
        parish (str): The parish where the establishment is located.
        address (str): The physical address of the establishment.
        coords (Tuple[float, float]): A tuple representing the latitude and longitude of the establishment.
        inspection_utility (float): The utility value (importance/priority) for inspecting this establishment.
        inspection_time (int): The time required for an inspection in minutes.
        opening_hours (List[int]): A list of 24 integers, where each represents if the establishment is open (1) or closed (0) in that hour.
    """

    def __init__(self, 
                 id: int, 
                 district: str, 
                 county: str, 
                 parish: str, 
                 address: str, 
                 latitude: float, 
                 longitude: float, 
                 inspection_utility: float, 
                 inspection_time: int, 
                 opening_hours_str: str):
        """
        Initializes an Establishment instance with the given attributes.

        Args:
            id (int): The establishment's unique identifier.
            district (str): The district where the establishment is located.
            county (str): The county where the establishment is located.
            parish (str): The parish where the establishment is located.
            address (str): The address of the establishment.
            latitude (float): The latitude coordinate of the establishment.
            longitude (float): The longitude coordinate of the establishment.
            inspection_utility (float): The utility or importance assigned to inspecting the establishment.
            inspection_time (int): The duration of the inspection in minutes.
            opening_hours_str (str): A string of 24 characters ('1' or '0') representing the opening hours for each hour of the day.

        Raises:
            ValueError: If opening_hours_str is not exactly 24 characters or contains invalid values.
        """
        self.id = int(id)
        self.district = district
        self.county = county
        self.parish = parish
        self.address = address
        self.coords = self._validate_coords(float(latitude), float(longitude))
        self.inspection_utility = float(inspection_utility)
        self.inspection_time = int(inspection_time)
        self.opening_hours = self._parse_opening_hours(opening_hours_str)

    def _validate_coords(self, latitude: float, longitude: float) -> Tuple[float, float]:
        """Validate and return the coordinates as a tuple of (latitude, longitude)."""
        if not (-90 <= latitude <= 90):
            raise ValueError(f"Invalid latitude {latitude}. Must be between -90 and 90.")
        if not (-180 <= longitude <= 180):
            raise ValueError(f"Invalid longitude {longitude}. Must be between -180 and 180.")
        return (latitude, longitude)

    def _parse_opening_hours(self, opening_hours_str: str) -> List[int]:
        """Parse the opening hours string into a list of integers representing open/closed hours."""
        opening_hours = list(map(int, opening_hours_str.removeprefix('[').removesuffix(']').split(', ')))
        if len(opening_hours) != 24:
            raise ValueError(f"Opening hours string must be exactly 24 characters long, got {len(opening_hours_str)}.")
        
        try:            
            # Ensure the string contains only '0' or '1'
            if not all(hour in (0, 1) for hour in opening_hours):
                raise ValueError("Opening hours string can only contain '0' (closed) or '1' (open).")
            
            return opening_hours
        
        except ValueError:
            raise ValueError(f"Invalid opening hours format: {opening_hours_str}. It should be a string of 24 '0' or '1' characters.")

    def __repr__(self) -> str:
        """Returns a formal string representation of the Establishment useful for debugging."""
        return (f"Establishment(id={self.id}, district={self.district}, county={self.county}, parish={self.parish}, "
                f"address={self.address}, coords={self.coords}, inspection_utility={self.inspection_utility}, "
                f"inspection_time={self.inspection_time}, opening_hours={self.opening_hours})")