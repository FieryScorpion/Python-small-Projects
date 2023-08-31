programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Bug"])
# Adding new items in the dictionary by programming
programming_dictionary["Action"] = "Action of doing something."
print(programming_dictionary)
#Creating an empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
#rogramming_disctionary ={}
#print(programming_disctionary)

#edit an item in a dictionary
programming_dictionary["Bug"] = "Hello there"
print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}
#nesting list using dictionary
travel_log= [
    {"country":"France", #Key is country and france is the value
     "cities_visited":["paris","bordeux","Dijon"],
     "total_visits": 12},
    {"country":"Germany",
     "cities_visited":["Berlin","Hamburg","Sttugart"],
     "total_visits" : 5},]
