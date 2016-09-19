def hotel_cost(days):
    return 140 * days


def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475


def rental_car_cost(days):
    price = 40 * days

    if days >= 7:
        price -= 50
    elif days >= 3 and days < 7:
        price -= 20
    return price


def trip_cost(city, days, spending_money):
    return hotel_cost(days) + rental_car_cost(days) + plane_ride_cost(city) + spending_money


print(trip_cost('Los Angeles', 5, 600))