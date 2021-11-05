import random

how = ["car", "train", "plane", "boat", "bike", "helicopter", "teleportation"]
what_we_eat = ["fine dining", "fast food", "cook at home", "local street food", "rob the grocery store"]
where = ["Iceland", "Hawaii", "Kenya", "Hong Kong", "Sydney", "Kalamazoo"]
funsies = ["movies", "bar hopping", "surfing", "staying in", "clubbin'", "chill with locals"]

def gen_options(some_list):
    list_index = random.randint(0, len(some_list)-1)
    return some_list[list_index]


# print(transporation, location, restaurant, funsies)

trip_list = [gen_options(where),  gen_options(what_we_eat),  gen_options(how),  gen_options(funsies)]
print(trip_list)

def print_trip(some_list):
    print(some_list[0], some_list[1], some_list[2], some_list[3])



print_trip(trip_list)
user_input = 10

while user_input != 5:
    user_input = int(input(f" Please press # 1-4 to adjust your trip {trip_list}, or press 5 if you are satisfied: "))
    print("changes will be made")
    if user_input == 1:
        trip_list[0] = gen_options(where)
        print(f"Location will be changed {trip_list[0]}")
        print(trip_list)
    elif user_input == 2:
        trip_list[1] = gen_options(what_we_eat)
        print(f"Restaurant option will be adjusted {trip_list[1]}")
        print(trip_list)
    elif user_input == 3:
        trip_list[2] = gen_options(how)
        print(f"Transportation will be adjusted {trip_list[2]}")
        print(trip_list)
    elif user_input == 4:
        trip_list[3] = gen_options(funsies)
        print(f"Your activity will be adjusted {trip_list[3]}")
        print(trip_list)

    
print("thank you for confirming your trip!")
    
