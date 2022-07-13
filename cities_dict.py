def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    x = {}
    for i in range(len(cities)):
        x[i] = cities[i]
    return x

print(cities_dict(['Bukhara','Khiva','Namangan','Samarkand','Tashkent']))    