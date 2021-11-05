import random

how = ["car", "train", "plane", "boat", "bike"]
what_we_eat = ["fine dining", "fast food", "cook at home"]
where = ["Iceland", "Hawaii", "Kenya", "Hong Kong", "Sydney"]
fun_stuff = ["movies", "bar hopping", "surfing", "staying in"]

def gen_options(some_list):
    list_index = random.randint(0, len(some_list)-1)
    return some_list[list_index]

transporation  = gen_options(how)
restaurant = gen_options(what_we_eat)
location = gen_options(where)
funsies = gen_options(fun_stuff)

# print(transporation, location, restaurant, funsies)

trip_list = [location, restaurant, transporation, funsies]
print(trip_list)
# def trip_planner(new_list):
#     list_index = new_list

#     for items in new_list:
#         if list_index == items:
#             return new_list
    
# result = trip_planner(trip_list)

def print_trip(some_list):
    print(some_list[0], some_list[1], some_list[2], some_list[3])

user_input = input(int())

print_trip(trip_list)
print(trip_list)
while user_input == True:
    print("changes will be made")
if user_input > 3:
    print("sorry that isnt an option")
else:
    print("thank you for confirming your trip!")
    
# print("\nthis is your most recently generated vacation.\n" "please input 1 to change destination\n" "2 to change restaurant options\n" "3 for transportation\n" "or 4 for activities\n")
#     # if user_input == '1': # DEST
    #     trip_list[0] = gen_options(where)
    #     location = gen_options(where)        

