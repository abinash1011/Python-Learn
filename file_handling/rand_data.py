'''
File Created: Sunday, 10th October 2021 7:19:23 pm
@Author: Abinash1011
-----
Last Modified: Monday, 11th October 2021 12:11:20 pm
Modified By: Abinash1011
-----
'''
import random

name = open("file_handling/Indian_Names.txt", "r")
list_names = []
for line in name:
    split_lines = line.split()
    list_names.append(split_lines[0])

states = open("file_handling/states.txt", "r")
list_states = []
for state in states:
    split_state = state.split()
    list_states.append(split_state[0])

cities = open("file_handling/city.txt", "r")
list_cities = []
for city in cities:
    split_city = city.split()
    list_cities.append(split_city[0])

mail_list = ["gmial", "blueiffmail", "yohoomail", "hitmail", "hobsput", "inlook", "protonmail"]

for i in range(100):
    first_name = random.choice(list_names)
    last_name = random.choice(list_names)
    phone = f'{random.randint(100,999)}-555-{random.randint(1000,9999)}'
    plot = random.randint(0, 999)
    fcity = random.choice(list_cities)
    fstate = random.choice(list_states)
    zip_code = random.randint(1000000, 9999999)
    address = str(plot) + ", St." + fcity + ", " + fstate
    mail = first_name.lower() + last_name.lower() + '@' + random.choice(mail_list) + ".com"
    x = open("file_handling/Fake_data.txt", "a")
    x.write(f"\n{first_name} {last_name}\n{phone}\n{address}\n{zip_code}")