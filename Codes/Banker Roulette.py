import random
names_string = input("Give me everyone's name separate#ed by commas.")
names = names_string.split(", ")
num_items = len(names)
# random.randint(0, x)
random_choice = random.randint(0, num_items - 1)
#person_who_will_pay = names[random_choice]
person_who_will_pay = names[random_choice]
print(person_who_will_pay+"will pay todays dinners")
