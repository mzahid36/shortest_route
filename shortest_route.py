cities_with_distance_in_km = {'Rabat to Sueca': 1063, 'Sueca to Rudow': 2656, 'Rudow to Mosu': 1352,
                              'Mosu to Le Plessis Trevise': 1841, 'Le Plessis Trevise to Kang Dong': 61,
                              'Kang Dong to Nezahualcoyotl': 1634, 'Nezahualcoyotl to Lindenwold': 151,
                              'Lindenwold to Queanbeyan': 285, 'Queanbeyan to Saint Chamond': 146,
                              'Saint Chamond to Cheektowaga': 11, 'Cheektowaga to Tirupati': 380,
                              'Tirupati to Snezhinsk': 2547, 'Snezhinsk to Glazov': 2524,
                              'Glazov to Gaoyou': 97, 'Gaoyou to Nola': 6999, 'Nola to Rutigtiano': 63,
                              'Rutigtiano to Colombo': 105, 'Colombo to Meckenheim': 244, 'Meckenheim to Hamburg': 502,
                              'Hamburg to Rabat': 30}

key_list = list(cities_with_distance_in_km.keys())
val_list = list(cities_with_distance_in_km.values())

# finding the largest edge
temp = 0
for i in cities_with_distance_in_km.values():
    if temp < i:
        temp = i

# index number of largest edge
p = val_list.index(temp)

# printing the shortest route with every edge value and total distance
# here I exclude the largest edge since we can start from anywhere,therefore I started from largest edge + 1
t = 1
total_distance = 0
print("\nShortest possible route with distance : \n\n")
while (p+t) - len(val_list) != p:
    print(key_list[(p+t) - len(val_list)], val_list[(p+t) - len(val_list)])
    total_distance = total_distance + val_list[(p+t) - len(val_list)]
    t += 1
print("\nTotal Distance will be : ", total_distance)


