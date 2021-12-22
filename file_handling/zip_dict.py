'''
File Created: Sunday, 17th October 2021 12:47:08 pm
@Author: Abinash1011
-----
Last Modified: Sunday, 17th October 2021 12:49:27 pm
Modified By: Abinash1011
-----
'''
cities = ["mumbai", "new york", "paris"]
countries = ["india", "USA", "france"]

cities_and_countries = zip(cities, countries)
print(cities_and_countries)

for i in  cities_and_countries:
    print(i)

dictionary = {city:country for city, country in zip(cities, countries)}
print(dictionary)
