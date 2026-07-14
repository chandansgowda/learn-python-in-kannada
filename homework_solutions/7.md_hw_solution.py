karnataka_dishes = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa",
    "Hubballi": "Girmit",
    "Udupi": "Masala Dosa"
}


karnataka_dishes["Shivamogga"] = "Kadubu"


karnataka_dishes["Bengaluru"] = "Ragi Mudde"

del karnataka_dishes["Udupi"]


print("Cities:", karnataka_dishes.keys())

print("Dishes:", karnataka_dishes.values())

#Nested Dictionary Practice
friends = {
    "Ananya": {
        "favorite_subject": "Maths",
        "favorite_food": "Paneer Butter Masala"
    },
    "Rahul": {
        "favorite_subject": "Science",
        "favorite_food": "Masala Dosa"
    }
}


print("Rahul's favorite food is:", friends["Rahul"]["favorite_food"])
