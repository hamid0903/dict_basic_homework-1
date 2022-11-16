def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    cities_1={}
    for key in range(len(cities)):
        cities_1.update({key:cities[key]})

    return cities_1

print(cities_dict(['Tashkent','New-York', 'Seoul']))