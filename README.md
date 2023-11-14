# Parcel Cost Calculator
   ### Video Demo: [Watch the Live Demo](https://youtu.be/MtpEIZ-MmwY)
## Description:
This program calculates the shipping cost and arrival time for parcels. The computation is based on the geodesic distance between the origin and destination and the parcel's weight. By default, the program is created for use in Kenya and takes two Kenyan towns as the origin and the destination. Parcel delivery services are common in Kenya but are yet to experience the full benefits of computers-based estimations of distance, costs, and time. The [geopy](https://pypi.org/project/geopy/) python module obtains the geodesic distance between two points. The program implements a rudimentary calculation of distances to obtain a rough estimate of distances between two points. Kenya does not have complex home and office addresses, hence the preference for estimates rather than precise distance measurements.

## Running The Program
The user is prompted to enter two locations: the first as the origin and the latter as the destination. From there, the `get_lat_long(city)` obtains the latitudes and longitude of the given city using the `Nominatim` geocoding service.

The function `calculate_distance(location1, location2)` computes the distance between the two locations in kilometers using the latitude and longitude coordinates.

`get_distance(place1, place2)` uses the `get_lat_long` and `calculate_distance` to calculate the geodesic distance between two places. It handles errors and returns None if the calculation fails.

`cost_calculator(weight, distance)` Calculates the shipping cost based on the item's weight and the distance to be shipped.

`expected_time(distance)` Calculates the expected time to cover a given distance at an average 60 km/h speed. It raises a ValueError if the distance is not a non-negative number.

`expected_arrival(hours, minutes)` Calculates the expected arrival time based on provided hours and minutes.

`check_weight(weight)` Checks if the weight is a valid number, more significant than zero, and less than or equal to 100.

The required `pip` install libraries are listed in `requirements.txt`

`main()`:
```Takes user input for the origin and destination locations
  calculates the distance
  calculates the shipping cost and expected arrival time
  It handles user input errors and displays appropriate error messages.```
