import random 
dict1 = {
    1: "ajay",
    2: "darshan",
    3: "rakshit",
    4: "dwarkesh",
    5: "om",
    6: "vrundali",
    7: "smit",
}

list1 = list(dict1.keys())
random.shuffle(list1)
print(list1)

counter = 0
for i in list1:
    counter += 1
    print(f"cubicle: {counter} and name: {dict1[i]}")
    

