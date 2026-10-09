def fuel_needed(distance):
    """
    Calculate the amount of fuel needed for a trip.
    
    Input:
        distance: trip distance in kilometers
        
    Output:
        fuel require in kilograms
    """
    fuel = distance * 2.5

    return fuel

def valid_input(distance, fuel_available):
    """
    Check whether the user input is valid
    """

    if distance <= 0 or fuel_available <= 0:
        return False

    return True

def mission_status(required_fuel, available_fuel):
    """
    Determine whether the spacecraft has enough fuel for the trip.
    """

    if available_fuel >= required_fuel:
        return "Mission is possible."
    
    return "Mission is not possible."

if __name__ == "__main__":

    distance = float(input(
        "Enter the mission distance in kilometers:"
    ))

    available_fuel = float(input(
        "Enter the available fuel in kilograms:"
    ))

    if not valid_input(distance, available_fuel):
        print("Invalid input")

    else: 
        required_fuel = fuel_needed(distance)

        status = mission_status(
            required_fuel,
            available_fuel
        )
        print(
            f"Fuel required: {required_fuel:.2f} kg"
        )

        print(status)