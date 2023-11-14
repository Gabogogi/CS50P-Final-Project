from geopy.geocoders import Nominatim
import geopy.distance
from datetime import datetime, timedelta

geolocator = Nominatim(user_agent="DistanceCalculator")


def get_lat_long(city):
    '''
    Get the latitude and longitude of a given city in Kenya.

    Parameters:
    - city (str): The name of the city.

    Returns:
    - tuple or None: A tuple containing the latitude and longitude if the location is found,
      or None if the location is not found.
    '''
    try:
        country = "Kenya"
        loc = geolocator.geocode(city + ", " + country)

        if loc:
            return (loc.latitude, loc.longitude)
        else:
            print(f"Location not found for city: {city}, country: {country}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching location: {e}")
        return None

def calculate_distance(location1, location2):
    '''
    Calculate the geodesic distance in kilometers between two locations.

    Parameters:
    - location1 (tuple): A tuple containing the latitude and longitude of the first location.
    - location2 (tuple): A tuple containing the latitude and longitude of the second location.

    Returns:
    - float or None: The geodesic distance in kilometers if both locations are provided,
      or None if any of the locations is missing.
    '''
    try:
        if location1 and location2:
            return geopy.distance.geodesic(location1, location2).km
        else:
            print("Error: Both locations are required for distance calculation.")
            return None
    except Exception as e:
        print(f"An error occurred while calculating distance: {e}")
        return None

def get_distance(place1, place2):
    '''
    Calculate the geodesic distance in kilometers between two places.

    Parameters:
    - place1 (str): The name of the first place.
    - place2 (str): The name of the second place.

    Returns:
    - float or None: The geodesic distance in kilometers if both places are valid,
      or None if any of the places is missing or the distance calculation fails.
    '''
    try:
        if place1 and place2:
            position1 = get_lat_long(place1)
            position2 = get_lat_long(place2)

            if position1 and position2:
                distance = calculate_distance(position1, position2)
                if distance is not None:
                    return distance
                else:
                    print("Distance calculation failed. Confirm origin and destination entries.")
            else:
                print("Origin and/or destination could not be located on the map.")
        else:
            print("Please enter both origin and destination.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None



def cost_calculator(weight, distance):
    '''
    Calculate shipping cost based on weight and distance

    - weight (float or int): The weight of the item.
    - distance (float or int): The distance to be shipped.

    Returns:
    - float: calculated shipping cost
    '''
    cost_per_10 = distance / 10
    return float(weight) * (10.0 * cost_per_10)


def expected_time(distance):
    '''
     Calculate the expected time to cover a given distance at an average speed of 60 km/h.

    Parameters:
    - distance (float or int): The distance to be covered.

    Returns:
    - tuple: A tuple containing hours and rounded minutes.
    '''
    if not isinstance(distance, (float, int)) or distance < 0:
        raise ValueError("Distance should be a non-negative number")

    av_speed = 60.0
    time_taken = (distance / av_speed)
    time = time_taken * 60
    hours, minutes = divmod(time, 60)
    return hours, round(minutes)

def expected_arrival(hours, minutes):
    '''
    Calculate the expected arrival time based on provided hours and minutes.

    Parameters:
    - hours (int): The number of hours to add to the current time.
    - minutes (int): The number of minutes to add to the current time.

    Returns:
    - str: A string representing the expected arrival time in the format "YYYY-MM-DD HH:MM:SS".
    '''
    current_time = datetime.now()
    hours_to_add = hours * 2
    minutes_to_add = minutes

    time_delta = timedelta(hours=hours_to_add, minutes=minutes_to_add)

    new_time = current_time + time_delta

    return new_time.strftime("%Y-%m-%d %H:%M:%S")

def check_weight(weight):
    try:
        weight = float(weight)
    except (ValueError, TypeError) as e:
        print(f"Error: Weight should be a number")
        return None

    if weight <= 0.0:
        print("Error: Weight should be greater than zero")
        return None
    elif weight > 100:
        print("Error: Weight should be less than 100")
        return None
    else:
        return weight

def main():
    place1 = input("Enter the first location: ")
    place2 = input("Enter the second location: ")
    distance = get_distance(place1, place2)
    parcel_weight = input("Enter weight of parcel in kgs: ")
    weight = check_weight(parcel_weight)

    if weight:
        cost = round(cost_calculator(weight, distance))
        hours, minutes = expected_time(distance)
        arr_time = expected_arrival(hours, minutes)
        print(f"Cost in Kenyan Shillings: {cost}. Time taken {hours} hours {minutes} minutes")
        print("Parcel shall be ready for pickup on: ", arr_time)


if __name__=="__main__":
    main()