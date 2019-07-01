def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == "Charlotte":
        return int(183)
    elif city == "Tampa":
        return int(220)
    elif city == "Pittsburgh":
        return int(222)
    elif city == "Los Angeles":
        return int(475)


def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
        return cost
    elif days >= 3:
        cost -= 20
        return cost
    else:
        return fosu


def trip_cost(city, days, spending_money):
    sum = rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money
    return sum


print(trip_cost("Los Angeles", 5, 600))