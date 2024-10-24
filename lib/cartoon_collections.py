def roll_call_dwarves(names):
    num = 0
    for name in names:
        num += 1
        print (f"{num}. {name}")
        

def summon_captain_planet(planets):
    return [planet.title() + "!" for planet in planets]

def long_planeteer_calls(words):
    truthy =[]
    for word in words:
        if len(word) > 4:
            truthy.append(True)
        else:
            truthy.append(False)
    return True in truthy 

cheese = ["cheddar", "gouda", "camembert"]

def find_the_cheese(food_list):
    cheese_list = []
    for food in food_list:
        if food in cheese:
            cheese_list.append(food)
            
    return cheese_list[0] if cheese_list else None
