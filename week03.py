def duplicate_city(cities):
    result_city = []
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2:
            result_city.append(city)
    return result_city

cities = ['Incheon', 'Seoul', 'Incheon', 'Incheon', 'Gwangju']
#cities = set(cities)
#cities.add('Incheon')
#cities.add('Suwon')
cities.append('Incheon')
cities.append('Seoul')
cities.append('Suwon')
print(cities)
print(set(duplicate_city(cities)))  # 중복값을 찾아서 하나만 나오도록 하는 방법