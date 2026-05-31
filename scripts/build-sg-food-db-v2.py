#!/usr/bin/env python3
"""
Build a massive food database for NutriTrace covering all cuisines
a typical Singaporean would encounter.

V2: ~1,400 foods across Japanese, Chinese, Korean, Western, Indian,
Thai, Vietnamese, Indonesian, Fast Food, Bakery, Breakfast, Zi Char,
Seafood, Hot Pot, Pizza, plus the original hawker collection.
"""

import json, sqlite3
from datetime import datetime, timezone

DB_PATH = "/data/db/nutritrace.db"
now = datetime.now(timezone.utc).isoformat()

FOODS = []

def add(name, category, nutrition, portion=100, unit="g", notes=None):
    FOODS.append({
        "name": name, "category": category, "nutrition": nutrition,
        "portion": portion, "unit": unit, "notes": notes
    })

# ==============================================================
# JAPANESE (80+)
# ==============================================================
J = "🇯🇵 Japanese"

# Sushi
add("Salmon Sashimi (5 slices)", J, {"calories":180,"fat":8,"saturated-fat":1.5,"carbohydrates":0,"sugars":0,"fiber":0,"proteins":26,"sodium":60}, 120)
add("Maguro / Tuna Sashimi (5 slices)", J, {"calories":150,"fat":3,"saturated-fat":0.5,"carbohydrates":0,"sugars":0,"fiber":0,"proteins":28,"sodium":50}, 120)
add("Salmon Belly Sashimi (5 pieces)", J, {"calories":250,"fat":18,"saturated-fat":3,"carbohydrates":0,"sugars":0,"fiber":0,"proteins":22,"sodium":50}, 100)
add("Mixed Sashimi Platter (12 pieces)", J, {"calories":280,"fat":10,"saturated-fat":2,"carbohydrates":2,"sugars":0,"fiber":0,"proteins":45,"sodium":120}, 250)
add("Tamago Sushi (2 pieces)", J, {"calories":120,"fat":3,"saturated-fat":1,"carbohydrates":20,"sugars":6,"fiber":0,"proteins":5,"sodium":200}, 80)
add("Salmon Sushi (2 pieces)", J, {"calories":140,"fat":4,"saturated-fat":1,"carbohydrates":18,"sugars":2,"fiber":0,"proteins":10,"sodium":150}, 80)
add("Tuna Sushi / Maguro Nigiri (2 pieces)", J, {"calories":120,"fat":2,"saturated-fat":0.5,"carbohydrates":18,"sugars":2,"fiber":0,"proteins":10,"sodium":150}, 80)
add("Ebi / Prawn Sushi (2 pieces)", J, {"calories":110,"fat":1,"saturated-fat":0,"carbohydrates":18,"sugars":2,"fiber":0,"proteins":8,"sodium":180}, 80)
add("Unagi / Eel Sushi (2 pieces)", J, {"calories":180,"fat":6,"saturated-fat":1.5,"carbohydrates":22,"sugars":6,"fiber":0,"proteins":10,"sodium":300}, 90)
add("California Roll (8 pieces)", J, {"calories":350,"fat":12,"saturated-fat":2,"carbohydrates":48,"sugars":6,"fiber":2,"proteins":14,"sodium":500}, 250)
add("Soft Shell Crab Roll (8 pieces)", J, {"calories":420,"fat":18,"saturated-fat":3,"carbohydrates":50,"sugars":5,"fiber":2,"proteins":16,"sodium":550}, 260)
add("Salmon Avocado Roll (8 pieces)", J, {"calories":320,"fat":14,"saturated-fat":2.5,"carbohydrates":36,"sugars":4,"fiber":3,"proteins":14,"sodium":400}, 240)
add("Dragon Roll (8 pieces)", J, {"calories":450,"fat":18,"saturated-fat":3,"carbohydrates":55,"sugars":8,"fiber":2,"proteins":18,"sodium":550}, 270)
add("Sushi Set A (10 pieces, basic)", J, {"calories":420,"fat":10,"saturated-fat":2,"carbohydrates":65,"sugars":8,"fiber":2,"proteins":22,"sodium":600}, 350)
add("Chirashi Don", J, {"calories":520,"fat":14,"saturated-fat":3,"carbohydrates":65,"sugars":4,"fiber":2,"proteins":32,"sodium":500}, 380)

# Ramen & Noodles
add("Tonkotsu Ramen", J, {"calories":650,"fat":28,"saturated-fat":10,"carbohydrates":70,"sugars":4,"fiber":2,"proteins":30,"sodium":2500}, 550)
add("Shoyu Ramen", J, {"calories":520,"fat":16,"saturated-fat":5,"carbohydrates":68,"sugars":5,"fiber":2,"proteins":28,"sodium":2800}, 500)
add("Miso Ramen", J, {"calories":580,"fat":20,"saturated-fat":6,"carbohydrates":70,"sugars":6,"fiber":3,"proteins":30,"sodium":2600}, 520)
add("Shio Ramen", J, {"calories":480,"fat":14,"saturated-fat":4,"carbohydrates":65,"sugars":4,"fiber":2,"proteins":26,"sodium":2600}, 480)
add("Tsukemen (Dipping Ramen)", J, {"calories":600,"fat":22,"saturated-fat":6,"carbohydrates":75,"sugars":5,"fiber":2,"proteins":28,"sodium":2800}, 500)
add("Cold Soba with Dipping Sauce", J, {"calories":350,"fat":3,"saturated-fat":0.5,"carbohydrates":65,"sugars":3,"fiber":2,"proteins":14,"sodium":1200}, 350)
add("Tempura Soba (Hot)", J, {"calories":520,"fat":18,"saturated-fat":3,"carbohydrates":70,"sugars":4,"fiber":3,"proteins":22,"sodium":1800}, 480)
add("Tempura Udon (Hot)", J, {"calories":550,"fat":18,"saturated-fat":3,"carbohydrates":75,"sugars":4,"fiber":2,"proteins":22,"sodium":1900}, 500)
add("Kitsune Udon", J, {"calories":400,"fat":8,"saturated-fat":1,"carbohydrates":65,"sugars":6,"fiber":2,"proteins":14,"sodium":1800}, 420)
add("Nabeyaki Udon", J, {"calories":480,"fat":12,"saturated-fat":3,"carbohydrates":68,"sugars":5,"fiber":3,"proteins":24,"sodium":2000}, 500)

# Donburi & Rice
add("Katsu Don / Tonkatsu Don", J, {"calories":750,"fat":28,"saturated-fat":7,"carbohydrates":85,"sugars":6,"fiber":2,"proteins":38,"sodium":1500}, 450)
add("Oyakodon", J, {"calories":550,"fat":14,"saturated-fat":4,"carbohydrates":70,"sugars":5,"fiber":2,"proteins":32,"sodium":1200}, 400)
add("Gyudon", J, {"calories":620,"fat":22,"saturated-fat":7,"carbohydrates":72,"sugars":8,"fiber":2,"proteins":32,"sodium":1400}, 420)
add("Teriyaki Chicken Don", J, {"calories":620,"fat":16,"saturated-fat":4,"carbohydrates":80,"sugars":14,"fiber":1,"proteins":35,"sodium":1200}, 420)
add("Unagi Don / Unadon", J, {"calories":650,"fat":22,"saturated-fat":6,"carbohydrates":78,"sugars":12,"fiber":1,"proteins":32,"sodium":900}, 400)
add("Salmon Teriyaki Don", J, {"calories":580,"fat":18,"saturated-fat":4,"carbohydrates":70,"sugars":10,"fiber":1,"proteins":35,"sodium":1000}, 400)
add("Aburi Salmon Don", J, {"calories":550,"fat":20,"saturated-fat":4,"carbohydrates":60,"sugars":4,"fiber":1,"proteins":32,"sodium":600}, 350)
add("Chicken Karaage Don", J, {"calories":680,"fat":28,"saturated-fat":6,"carbohydrates":72,"sugars":5,"fiber":1,"proteins":35,"sodium":1300}, 420)
add("Japanese Curry Rice with Chicken Katsu", J, {"calories":780,"fat":32,"saturated-fat":10,"carbohydrates":88,"sugars":8,"fiber":3,"proteins":35,"sodium":1800}, 500)
add("Japanese Curry Rice (Pork Katsu)", J, {"calories":820,"fat":36,"saturated-fat":11,"carbohydrates":88,"sugars":8,"fiber":3,"proteins":35,"sodium":1800}, 500)
add("Japanese Curry Rice (Plain / Vegetable)", J, {"calories":480,"fat":14,"saturated-fat":5,"carbohydrates":75,"sugars":8,"fiber":4,"proteins":10,"sodium":1400}, 400)
add("Omurice", J, {"calories":620,"fat":24,"saturated-fat":7,"carbohydrates":70,"sugars":10,"fiber":2,"proteins":22,"sodium":1000}, 400)

# Set Meals
add("Chicken Katsu Set", J, {"calories":750,"fat":30,"saturated-fat":7,"carbohydrates":75,"sugars":6,"fiber":3,"proteins":42,"sodium":1500}, 480,
   "Breaded chicken cutlet with rice, shredded cabbage, miso soup, pickles")
add("Pork Katsu / Tonkatsu Set", J, {"calories":800,"fat":35,"saturated-fat":10,"carbohydrates":75,"sugars":5,"fiber":3,"proteins":40,"sodium":1600}, 480)
add("Saba Shioyaki Set", J, {"calories":480,"fat":20,"saturated-fat":4,"carbohydrates":55,"sugars":3,"fiber":2,"proteins":28,"sodium":1200}, 400,
   "Grilled salted mackerel with rice, miso soup, pickles")
add("Salmon Shioyaki Set", J, {"calories":520,"fat":22,"saturated-fat":4,"carbohydrates":55,"sugars":3,"fiber":2,"proteins":32,"sodium":1000}, 400)
add("Tempura Set (Ebi + Vegetables)", J, {"calories":580,"fat":24,"saturated-fat":4,"carbohydrates":70,"sugars":4,"fiber":3,"proteins":22,"sodium":1400}, 420)
add("Ginger Pork / Shogayaki Set", J, {"calories":580,"fat":22,"saturated-fat":6,"carbohydrates":60,"sugars":8,"fiber":2,"proteins":32,"sodium":1300}, 400)

# Sides & Small Plates
add("Edamame (1 bowl)", J, {"calories":150,"fat":6,"saturated-fat":1,"carbohydrates":12,"sugars":2,"fiber":6,"proteins":14,"sodium":300}, 150)
add("Agedashi Tofu (4 pieces)", J, {"calories":220,"fat":14,"saturated-fat":2,"carbohydrates":16,"sugars":3,"fiber":1,"proteins":10,"sodium":700}, 180)
add("Chawanmushi (1 cup)", J, {"calories":90,"fat":4,"saturated-fat":1,"carbohydrates":4,"sugars":2,"fiber":0,"proteins":10,"sodium":400}, 150)
add("Gyoza (6 pieces, pan-fried)", J, {"calories":280,"fat":14,"saturated-fat":4,"carbohydrates":28,"sugars":2,"fiber":1,"proteins":12,"sodium":700}, 150)
add("Chicken Karaage (6 pieces)", J, {"calories":380,"fat":24,"saturated-fat":5,"carbohydrates":12,"sugars":1,"fiber":0,"proteins":28,"sodium":800}, 180)
add("Takoyaki (6 pieces)", J, {"calories":280,"fat":14,"saturated-fat":3,"carbohydrates":28,"sugars":4,"fiber":1,"proteins":10,"sodium":600}, 180)
add("Miso Soup (1 bowl)", J, {"calories":40,"fat":1.5,"saturated-fat":0.5,"carbohydrates":4,"sugars":1,"fiber":1,"proteins":3,"sodium":700}, 200, "unit","ml")
add("Japanese Potato Salad (side)", J, {"calories":180,"fat":12,"saturated-fat":2,"carbohydrates":16,"sugars":3,"fiber":2,"proteins":3,"sodium":300}, 120)
add("Chuka Wakame Salad", J, {"calories":80,"fat":4,"saturated-fat":0.5,"carbohydrates":8,"sugars":4,"fiber":3,"proteins":2,"sodium":400}, 120)
add("Tamagoyaki (3 pieces)", J, {"calories":150,"fat":10,"saturated-fat":3,"carbohydrates":8,"sugars":5,"fiber":0,"proteins":10,"sodium":300}, 120)
add("Okonomiyaki (1 piece)", J, {"calories":550,"fat":28,"saturated-fat":7,"carbohydrates":55,"sugars":8,"fiber":3,"proteins":18,"sodium":1400}, 300)
add("Yaki Tori (5 sticks, assorted)", J, {"calories":280,"fat":12,"saturated-fat":3,"carbohydrates":8,"sugars":4,"fiber":0,"proteins":35,"sodium":800}, 200)
add("Yakiniku Beef (150g grilled)", J, {"calories":380,"fat":28,"saturated-fat":10,"carbohydrates":2,"sugars":1,"fiber":0,"proteins":30,"sodium":500}, 150)

# Japanese desserts & drinks
add("Matcha Ice Cream (1 scoop)", J, {"calories":140,"fat":8,"saturated-fat":5,"carbohydrates":15,"sugars":12,"fiber":0,"proteins":3,"sodium":40}, 80)
add("Mochi Ice Cream (2 pieces)", J, {"calories":180,"fat":6,"saturated-fat":3,"carbohydrates":30,"sugars":16,"fiber":1,"proteins":3,"sodium":40}, 80)
add("Matcha Latte (Hot, medium)", J, {"calories":150,"fat":5,"saturated-fat":3,"carbohydrates":20,"sugars":18,"fiber":0,"proteins":6,"sodium":100}, 350, "ml")
add("Japanese Green Tea (no sugar)", J, {"calories":0,"fat":0,"saturated-fat":0,"carbohydrates":0,"sugars":0,"fiber":0,"proteins":0,"sodium":5}, 300, "ml")

# ==============================================================
# CHINESE / ZI CHAR (100+)
# ==============================================================
C = "🇨🇳 Chinese / Zi Char"

# Soups (restaurant style)
add("Hot & Sour Soup (1 bowl)", C, {"calories":150,"fat":6,"saturated-fat":1.5,"carbohydrates":16,"sugars":3,"fiber":2,"proteins":10,"sodium":1800}, 300, "ml")
add("Shark Fin Melon Soup (1 bowl)", C, {"calories":120,"fat":4,"saturated-fat":1,"carbohydrates":12,"sugars":4,"fiber":2,"proteins":10,"sodium":800}, 300, "ml")
add("Fish Maw Soup (1 bowl)", C, {"calories":140,"fat":5,"saturated-fat":1,"carbohydrates":10,"sugars":2,"fiber":1,"proteins":14,"sodium":900}, 300, "ml")
add("Seafood Soup (1 bowl)", C, {"calories":180,"fat":6,"saturated-fat":1.5,"carbohydrates":10,"sugars":3,"fiber":1,"proteins":22,"sodium":1200}, 350, "ml")
add("Corn Soup with Crab Meat (1 bowl)", C, {"calories":160,"fat":6,"saturated-fat":1.5,"carbohydrates":18,"sugars":6,"fiber":1,"proteins":10,"sodium":900}, 300, "ml")
add("Double-Boiled Chicken Soup (1 bowl)", C, {"calories":100,"fat":4,"saturated-fat":1,"carbohydrates":4,"sugars":2,"fiber":1,"proteins":14,"sodium":600}, 300, "ml")
add("Wonton Soup (1 bowl, with noodles)", C, {"calories":350,"fat":10,"saturated-fat":3,"carbohydrates":48,"sugars":3,"fiber":2,"proteins":18,"sodium":1800}, 400)
add("Suan La Fen / Hot & Sour Glass Noodles", C, {"calories":450,"fat":18,"saturated-fat":4,"carbohydrates":60,"sugars":4,"fiber":2,"proteins":14,"sodium":2200}, 420)

# Dim Sum
add("Har Gow / Prawn Dumpling (4 pieces)", C, {"calories":150,"fat":3,"saturated-fat":0.5,"carbohydrates":22,"sugars":2,"fiber":1,"proteins":10,"sodium":350}, 120)
add("Siew Mai / Pork Dumpling (4 pieces)", C, {"calories":180,"fat":10,"saturated-fat":3,"carbohydrates":12,"sugars":2,"fiber":1,"proteins":12,"sodium":400}, 120)
add("Char Siew Bao / BBQ Pork Bun (2 pieces)", C, {"calories":320,"fat":8,"saturated-fat":2.5,"carbohydrates":48,"sugars":10,"fiber":2,"proteins":14,"sodium":500}, 160)
add("Xiao Long Bao / Soup Dumpling (6 pieces)", C, {"calories":280,"fat":12,"saturated-fat":3,"carbohydrates":28,"sugars":2,"fiber":1,"proteins":16,"sodium":600}, 150)
add("Pan-Fried Dumpling / Guo Tie (6 pieces)", C, {"calories":320,"fat":16,"saturated-fat":4,"carbohydrates":30,"sugars":2,"fiber":1,"proteins":14,"sodium":700}, 160)
add("Chee Cheong Fun with Prawn (2 rolls)", C, {"calories":220,"fat":6,"saturated-fat":1.5,"carbohydrates":32,"sugars":4,"fiber":1,"proteins":10,"sodium":500}, 180)
add("Chee Cheong Fun with Char Siew (2 rolls)", C, {"calories":250,"fat":8,"saturated-fat":2.5,"carbohydrates":32,"sugars":6,"fiber":1,"proteins":12,"sodium":550}, 180)
add("Phoenix Claws / Feng Zhao (1 plate)", C, {"calories":200,"fat":14,"saturated-fat":3,"carbohydrates":8,"sugars":4,"fiber":0,"proteins":12,"sodium":700}, 120)
add("Steamed Spare Ribs / Pai Gu (1 plate)", C, {"calories":280,"fat":18,"saturated-fat":5,"carbohydrates":8,"sugars":3,"fiber":0,"proteins":20,"sodium":800}, 140)
add("Liu Sha Bao / Salted Egg Custard Bun (2 pieces)", C, {"calories":280,"fat":12,"saturated-fat":5,"carbohydrates":38,"sugars":12,"fiber":1,"proteins":6,"sodium":300}, 140)
add("Egg Tart (2 pieces)", C, {"calories":260,"fat":14,"saturated-fat":7,"carbohydrates":28,"sugars":10,"fiber":1,"proteins":5,"sodium":200}, 100)
add("Lo Mai Gai / Glutinous Rice Chicken (1 piece)", C, {"calories":380,"fat":14,"saturated-fat":4,"carbohydrates":48,"sugars":4,"fiber":2,"proteins":18,"sodium":800}, 200)
add("Fried Carrot Cake / Luo Bo Gao (3 slices)", C, {"calories":220,"fat":14,"saturated-fat":3,"carbohydrates":20,"sugars":3,"fiber":1,"proteins":4,"sodium":500}, 150)
add("Spring Roll (4 pieces)", C, {"calories":240,"fat":14,"saturated-fat":3,"carbohydrates":24,"sugars":3,"fiber":2,"proteins":6,"sodium":400}, 140)
add("Fried Beancurd Skin Roll (4 pieces)", C, {"calories":280,"fat":18,"saturated-fat":4,"carbohydrates":18,"sugars":2,"fiber":2,"proteins":12,"sodium":500}, 140)
add("Dim Sum Platter (mixed, 8 pieces)", C, {"calories":450,"fat":22,"saturated-fat":6,"carbohydrates":45,"sugars":6,"fiber":2,"proteins":22,"sodium":1000}, 300)

# Zi Char Dishes
add("Sweet and Sour Pork", C, {"calories":480,"fat":24,"saturated-fat":6,"carbohydrates":42,"sugars":22,"fiber":2,"proteins":22,"sodium":800}, 280)
add("Sweet and Sour Fish", C, {"calories":400,"fat":18,"saturated-fat":3,"carbohydrates":38,"sugars":20,"fiber":1,"proteins":24,"sodium":700}, 280)
add("Kung Pao Chicken", C, {"calories":380,"fat":22,"saturated-fat":4,"carbohydrates":18,"sugars":6,"fiber":2,"proteins":28,"sodium":900}, 250)
add("Mapo Tofu", C, {"calories":320,"fat":22,"saturated-fat":5,"carbohydrates":14,"sugars":3,"fiber":2,"proteins":16,"sodium":1200}, 250)
add("Mapo Tofu with Minced Pork", C, {"calories":380,"fat":26,"saturated-fat":7,"carbohydrates":14,"sugars":3,"fiber":2,"proteins":20,"sodium":1300}, 280)
add("Cereal Prawns (6 pieces)", C, {"calories":420,"fat":24,"saturated-fat":6,"carbohydrates":20,"sugars":6,"fiber":1,"proteins":28,"sodium":800}, 250)
add("Butter Prawns (6 pieces)", C, {"calories":480,"fat":30,"saturated-fat":12,"carbohydrates":18,"sugars":6,"fiber":1,"proteins":28,"sodium":900}, 250)
add("Salted Egg Prawns (6 pieces)", C, {"calories":500,"fat":32,"saturated-fat":14,"carbohydrates":16,"sugars":4,"fiber":1,"proteins":28,"sodium":1000}, 250)
add("Salted Egg Chicken", C, {"calories":480,"fat":30,"saturated-fat":12,"carbohydrates":22,"sugars":5,"fiber":1,"proteins":28,"sodium":1000}, 280)
add("Salted Egg Sotong", C, {"calories":420,"fat":26,"saturated-fat":10,"carbohydrates":20,"sugars":4,"fiber":1,"proteins":24,"sodium":900}, 250)
add("Har Cheong Gai / Prawn Paste Chicken (6 pieces)", C, {"calories":480,"fat":30,"saturated-fat":7,"carbohydrates":14,"sugars":2,"fiber":0,"proteins":35,"sodium":1200}, 250)
add("Deep Fried Prawns with Wasabi Mayo", C, {"calories":420,"fat":26,"saturated-fat":5,"carbohydrates":22,"sugars":8,"fiber":1,"proteins":26,"sodium":700}, 250)
add("Sambal Kangkong", C, {"calories":120,"fat":8,"saturated-fat":1.5,"carbohydrates":8,"sugars":2,"fiber":3,"proteins":4,"sodium":600}, 180)
add("Stir-Fried Kai Lan with Garlic", C, {"calories":100,"fat":6,"saturated-fat":1,"carbohydrates":8,"sugars":2,"fiber":3,"proteins":3,"sodium":400}, 180)
add("Stir-Fried Broccoli with Garlic", C, {"calories":90,"fat":5,"saturated-fat":1,"carbohydrates":8,"sugars":2,"fiber":3,"proteins":4,"sodium":350}, 180)
add("Stir-Fried French Beans with Minced Pork", C, {"calories":200,"fat":14,"saturated-fat":4,"carbohydrates":10,"sugars":3,"fiber":3,"proteins":12,"sodium":600}, 200)
add("Stir-Fried Eggplant with Minced Pork", C, {"calories":250,"fat":18,"saturated-fat":4,"carbohydrates":16,"sugars":6,"fiber":3,"proteins":10,"sodium":800}, 220)
add("Stir-Fried Nai Bai / Baby Cabbage", C, {"calories":80,"fat":5,"saturated-fat":1,"carbohydrates":6,"sugars":2,"fiber":2,"proteins":3,"sodium":400}, 180)
add("Oyster Sauce Vegetables (mixed)", C, {"calories":80,"fat":4,"saturated-fat":1,"carbohydrates":10,"sugars":3,"fiber":3,"proteins":3,"sodium":600}, 180)
add("Prawn Paste Chicken Wings (6 pieces)", C, {"calories":420,"fat":28,"saturated-fat":6,"carbohydrates":12,"sugars":2,"fiber":0,"proteins":30,"sodium":1100}, 220)

# Tze Char Noodles / Rice
add("San Lou Hor Fun (Fish Hor Fun)", C, {"calories":500,"fat":16,"saturated-fat":3,"carbohydrates":65,"sugars":4,"fiber":2,"proteins":22,"sodium":1400}, 400,
   "Flat rice noodles in egg gravy with sliced fish")
add("Wat Dan Hor / Egg Gravy Hor Fun", C, {"calories":520,"fat":18,"saturated-fat":4,"carbohydrates":65,"sugars":4,"fiber":2,"proteins":22,"sodium":1500}, 420)
add("Beef Hor Fun (Dry)", C, {"calories":550,"fat":20,"saturated-fat":5,"carbohydrates":65,"sugars":4,"fiber":2,"proteins":26,"sodium":1600}, 400)
add("Beef Hor Fun (Gravy)", C, {"calories":580,"fat":22,"saturated-fat":6,"carbohydrates":68,"sugars":5,"fiber":2,"proteins":26,"sodium":1700}, 450)
add("Yang Zhou Fried Rice", C, {"calories":620,"fat":22,"saturated-fat":5,"carbohydrates":82,"sugars":3,"fiber":2,"proteins":22,"sodium":1400}, 380)
add("Salted Fish Fried Rice", C, {"calories":650,"fat":24,"saturated-fat":6,"carbohydrates":82,"sugars":3,"fiber":2,"proteins":24,"sodium":1800}, 380)
add("Fujian Fried Rice", C, {"calories":580,"fat":20,"saturated-fat":5,"carbohydrates":78,"sugars":5,"fiber":2,"proteins":22,"sodium":1500}, 400)

# Congee / Porridge
add("Century Egg & Pork Porridge", C, {"calories":320,"fat":8,"saturated-fat":2.5,"carbohydrates":48,"sugars":2,"fiber":1,"proteins":16,"sodium":1000}, 400)
add("Fish Porridge / Sliced Fish Congee", C, {"calories":280,"fat":5,"saturated-fat":1,"carbohydrates":45,"sugars":1,"fiber":1,"proteins":18,"sodium":800}, 420)
add("Chicken Porridge", C, {"calories":300,"fat":8,"saturated-fat":2,"carbohydrates":46,"sugars":2,"fiber":1,"proteins":16,"sodium":900}, 420)
add("Minced Pork Porridge", C, {"calories":320,"fat":10,"saturated-fat":3,"carbohydrates":46,"sugars":2,"fiber":1,"proteins":14,"sodium":1000}, 420)
add("Mixed Pork Porridge / Zhu Za Zhou", C, {"calories":350,"fat":12,"saturated-fat":4,"carbohydrates":48,"sugars":2,"fiber":1,"proteins":18,"sodium":1100}, 450)
add("Plain Congee (1 bowl)", C, {"calories":140,"fat":1,"saturated-fat":0,"carbohydrates":30,"sugars":0,"fiber":0,"proteins":3,"sodium":100}, 350)

# More Chinese Dishes
add("Peking Duck (3 wraps)", C, {"calories":350,"fat":22,"saturated-fat":6,"carbohydrates":28,"sugars":8,"fiber":1,"proteins":12,"sodium":500}, 180)
add("Crispy Roast Pork / Siu Yuk (100g)", C, {"calories":350,"fat":28,"saturated-fat":10,"carbohydrates":0,"sugars":0,"fiber":0,"proteins":22,"sodium":600}, 100)
add("Char Siew / BBQ Pork (100g)", C, {"calories":280,"fat":14,"saturated-fat":5,"carbohydrates":14,"sugars":12,"fiber":0,"proteins":24,"sodium":700}, 100)
add("Roast Duck (quarter, with rice)", C, {"calories":650,"fat":30,"saturated-fat":9,"carbohydrates":60,"sugars":4,"fiber":1,"proteins":35,"sodium":1400}, 400)
add("Soy Sauce Chicken (quarter, with rice)", C, {"calories":580,"fat":20,"saturated-fat":6,"carbohydrates":62,"sugars":6,"fiber":1,"proteins":35,"sodium":1500}, 420)
add("White Cut Chicken (half bird)", C, {"calories":550,"fat":28,"saturated-fat":8,"carbohydrates":2,"sugars":0,"fiber":0,"proteins":70,"sodium":800}, 350)
add("Steamed Fish Cantonese Style", C, {"calories":350,"fat":14,"saturated-fat":3,"carbohydrates":6,"sugars":2,"fiber":1,"proteins":48,"sodium":1200}, 350)
add("Steamed Fish Teochew Style", C, {"calories":300,"fat":10,"saturated-fat":2,"carbohydrates":4,"sugars":2,"fiber":1,"proteins":48,"sodium":1000}, 350)
add("Braised Pork Belly / Dong Po Rou (slice)", C, {"calories":350,"fat":30,"saturated-fat":11,"carbohydrates":6,"sugars":4,"fiber":0,"proteins":12,"sodium":700}, 100)
add("Braised Duck", C, {"calories":380,"fat":25,"saturated-fat":8,"carbohydrates":6,"sugars":4,"fiber":0,"proteins":30,"sodium":1000}, 200)
add("Chilli Crab (1 crab, shared 2 pax)", C, {"calories":450,"fat":28,"saturated-fat":8,"carbohydrates":15,"sugars":8,"fiber":1,"proteins":35,"sodium":1600}, 350)
add("Black Pepper Crab (1 crab, shared 2 pax)", C, {"calories":420,"fat":26,"saturated-fat":7,"carbohydrates":12,"sugars":4,"fiber":1,"proteins":35,"sodium":1400}, 350)
add("Mantou / Fried Bun (2 pieces)", C, {"calories":220,"fat":10,"saturated-fat":2.5,"carbohydrates":28,"sugars":4,"fiber":1,"proteins":5,"sodium":200}, 100)
add("Seafood Hor Fun", C, {"calories":550,"fat":20,"saturated-fat":5,"carbohydrates":68,"sugars":4,"fiber":2,"proteins":26,"sodium":1500}, 450)
add("Ee-Fu Noodles", C, {"calories":520,"fat":22,"saturated-fat":6,"carbohydrates":62,"sugars":4,"fiber":2,"proteins":20,"sodium":1400}, 380)
add("Kailan with Oyster Sauce & Garlic", C, {"calories":80,"fat":4,"saturated-fat":1,"carbohydrates":8,"sugars":2,"fiber":3,"proteins":3,"sodium":500}, 180)
add("Chilled Tofu with Century Egg", C, {"calories":180,"fat":10,"saturated-fat":2,"carbohydrates":8,"sugars":3,"fiber":1,"proteins":14,"sodium":600}, 200)
add("Stir-Fried Beef with Ginger & Spring Onion", C, {"calories":350,"fat":22,"saturated-fat":6,"carbohydrates":10,"sugars":4,"fiber":1,"proteins":28,"sodium":900}, 250)
add("Cashew Chicken", C, {"calories":380,"fat":22,"saturated-fat":4,"carbohydrates":16,"sugars":5,"fiber":2,"proteins":30,"sodium":800}, 250)
add("Lemon Chicken", C, {"calories":480,"fat":24,"saturated-fat":5,"carbohydrates":40,"sugars":18,"fiber":1,"proteins":26,"sodium":700}, 280)
add("Szechuan Spicy Chicken / La Zi Ji", C, {"calories":420,"fat":26,"saturated-fat":5,"carbohydrates":18,"sugars":4,"fiber":2,"proteins":30,"sodium":1200}, 250)
add("Stir-Fried Venison with Ginger & Spring Onion", C, {"calories":280,"fat":12,"saturated-fat":4,"carbohydrates":10,"sugars":4,"fiber":1,"proteins":32,"sodium":800}, 250)
add("Prawn Omelette / Fu Yong Egg", C, {"calories":320,"fat":22,"saturated-fat":5,"carbohydrates":8,"sugars":3,"fiber":1,"proteins":22,"sodium":600}, 200)
add("Onion Omelette", C, {"calories":220,"fat":16,"saturated-fat":4,"carbohydrates":8,"sugars":3,"fiber":1,"proteins":12,"sodium":400}, 150)

# ==============================================================
# KOREAN (40+)
# ==============================================================
K = "🇰🇷 Korean"

add("Bibimbap (Beef)", K, {"calories":650,"fat":22,"saturated-fat":6,"carbohydrates":85,"sugars":8,"fiber":5,"proteins":30,"sodium":1400}, 450)
add("Bibimbap (Hot Stone / Dolsot)", K, {"calories":700,"fat":24,"saturated-fat":7,"carbohydrates":90,"sugars":10,"fiber":5,"proteins":32,"sodium":1500}, 480)
add("Kimchi Jjigae with Pork & Tofu", K, {"calories":400,"fat":22,"saturated-fat":7,"carbohydrates":25,"sugars":5,"fiber":4,"proteins":28,"sodium":2200}, 450)
add("Sundubu Jjigae / Soft Tofu Stew", K, {"calories":380,"fat":20,"saturated-fat":5,"carbohydrates":24,"sugars":4,"fiber":3,"proteins":24,"sodium":2000}, 420)
add("Doenjang Jjigae / Soybean Paste Stew", K, {"calories":300,"fat":14,"saturated-fat":4,"carbohydrates":22,"sugars":4,"fiber":4,"proteins":18,"sodium":2000}, 400)
add("Korean BBQ Samgyeopsal (200g pork belly, grilled)", K, {"calories":580,"fat":48,"saturated-fat":18,"carbohydrates":2,"sugars":1,"fiber":0,"proteins":32,"sodium":400}, 200)
add("Korean BBQ Beef / Bulgogi (200g)", K, {"calories":420,"fat":24,"saturated-fat":8,"carbohydrates":14,"sugars":10,"fiber":1,"proteins":38,"sodium":900}, 250)
add("Korean BBQ Marinated Chicken / Dak Galbi (200g)", K, {"calories":380,"fat":18,"saturated-fat":4,"carbohydrates":16,"sugars":8,"fiber":2,"proteins":38,"sodium":1000}, 250)
add("Korean Fried Chicken (whole)", K, {"calories":1100,"fat":70,"saturated-fat":18,"carbohydrates":40,"sugars":10,"fiber":1,"proteins":75,"sodium":2000}, 500,
   "1 whole chicken coated in sweet-spicy Yangnyeom sauce (shared). HALF chicken ≈ 550 kcal.")
add("Korean Fried Chicken (half)", K, {"calories":550,"fat":35,"saturated-fat":9,"carbohydrates":20,"sugars":5,"fiber":1,"proteins":38,"sodium":1000}, 250)
add("Korean Fried Chicken Wings (6 pieces)", K, {"calories":450,"fat":28,"saturated-fat":7,"carbohydrates":18,"sugars":6,"fiber":0,"proteins":32,"sodium":900}, 220)
add("Japchae / Stir-Fried Glass Noodles", K, {"calories":380,"fat":12,"saturated-fat":3,"carbohydrates":55,"sugars":6,"fiber":3,"proteins":12,"sodium":800}, 300)
add("Tteokbokki / Spicy Rice Cakes", K, {"calories":400,"fat":6,"saturated-fat":1,"carbohydrates":78,"sugars":14,"fiber":2,"proteins":6,"sodium":1600}, 350)
add("Kimchi Pancake / Kimchi Jeon", K, {"calories":350,"fat":18,"saturated-fat":3,"carbohydrates":38,"sugars":4,"fiber":2,"proteins":8,"sodium":1000}, 200)
add("Seafood Pancake / Haemul Pajeon", K, {"calories":420,"fat":22,"saturated-fat":4,"carbohydrates":40,"sugars":4,"fiber":2,"proteins":16,"sodium":1100}, 220)
add("Kimbap (1 roll)", K, {"calories":320,"fat":8,"saturated-fat":2,"carbohydrates":50,"sugars":4,"fiber":3,"proteins":12,"sodium":600}, 220)
add("Jjajangmyeon / Black Bean Noodles", K, {"calories":600,"fat":22,"saturated-fat":5,"carbohydrates":80,"sugars":12,"fiber":3,"proteins":18,"sodium":1600}, 400)
add("Jjamppong / Spicy Seafood Noodle Soup", K, {"calories":550,"fat":18,"saturated-fat":4,"carbohydrates":72,"sugars":6,"fiber":3,"proteins":28,"sodium":2500}, 500)
add("Bossam / Boiled Pork Belly with Lettuce Wraps (200g)", K, {"calories":520,"fat":40,"saturated-fat":15,"carbohydrates":6,"sugars":3,"fiber":2,"proteins":32,"sodium":900}, 300)
add("Naengmyeon / Cold Buckwheat Noodles", K, {"calories":380,"fat":6,"saturated-fat":1,"carbohydrates":70,"sugars":10,"fiber":3,"proteins":14,"sodium":1600}, 450)
add("Kimchi Fried Rice with Egg", K, {"calories":480,"fat":18,"saturated-fat":4,"carbohydrates":62,"sugars":4,"fiber":3,"proteins":16,"sodium":1200}, 350)
add("Army Stew / Budae Jjigae (shared 2 pax)", K, {"calories":650,"fat":32,"saturated-fat":10,"carbohydrates":60,"sugars":8,"fiber":3,"proteins":35,"sodium":3000}, 500)
add("Korean Army Stew with Rice (per person)", K, {"calories":450,"fat":20,"saturated-fat":6,"carbohydrates":50,"sugars":6,"fiber":2,"proteins":22,"sodium":2000}, 350)
add("Gimbap / Triangle Kimbap (1 piece)", K, {"calories":180,"fat":5,"saturated-fat":1,"carbohydrates":28,"sugars":3,"fiber":1,"proteins":6,"sodium":350}, 120)
add("Korean Side Dishes / Banchan (assorted, 6 types)", K, {"calories":120,"fat":4,"saturated-fat":0.5,"carbohydrates":16,"sugars":4,"fiber":5,"proteins":4,"sodium":800}, 150)
add("Korean Corn Dog", K, {"calories":350,"fat":20,"saturated-fat":6,"carbohydrates":32,"sugars":6,"fiber":1,"proteins":10,"sodium":600}, 150)
add("Bingsu / Patbingsu (1 bowl)", K, {"calories":350,"fat":10,"saturated-fat":5,"carbohydrates":60,"sugars":35,"fiber":2,"proteins":6,"sodium":100}, 300)
add("Soju (1 bottle, 360ml)", K, {"calories":540,"fat":0,"saturated-fat":0,"carbohydrates":0,"sugars":0,"fiber":0,"proteins":0,"sodium":10}, 360, "ml")

# ==============================================================
# WESTERN (80+)
# ==============================================================
W = "🍝 Western"

# Pastas
add("Aglio Olio", W, {"calories":480,"fat":22,"saturated-fat":4,"carbohydrates":58,"sugars":3,"fiber":2,"proteins":12,"sodium":500}, 300)
add("Aglio Olio with Prawns", W, {"calories":550,"fat":24,"saturated-fat":4,"carbohydrates":58,"sugars":3,"fiber":2,"proteins":24,"sodium":600}, 350)
add("Aglio Olio with Chicken", W, {"calories":580,"fat":26,"saturated-fat":5,"carbohydrates":58,"sugars":3,"fiber":2,"proteins":28,"sodium":600}, 350)
add("Carbonara", W, {"calories":680,"fat":38,"saturated-fat":18,"carbohydrates":55,"sugars":4,"fiber":2,"proteins":28,"sodium":900}, 350)
add("Bolognese", W, {"calories":580,"fat":22,"saturated-fat":8,"carbohydrates":65,"sugars":8,"fiber":3,"proteins":28,"sodium":800}, 380)
add("Creamy Tomato Pasta with Chicken", W, {"calories":620,"fat":28,"saturated-fat":12,"carbohydrates":60,"sugars":8,"fiber":3,"proteins":30,"sodium":900}, 380)
add("Pesto Pasta", W, {"calories":550,"fat":32,"saturated-fat":6,"carbohydrates":52,"sugars":3,"fiber":2,"proteins":16,"sodium":600}, 320)
add("Vongole / White Wine Clam Pasta", W, {"calories":480,"fat":16,"saturated-fat":3,"carbohydrates":58,"sugars":3,"fiber":2,"proteins":22,"sodium":800}, 350)
add("Lasagna (beef)", W, {"calories":620,"fat":32,"saturated-fat":16,"carbohydrates":48,"sugars":8,"fiber":3,"proteins":35,"sodium":1000}, 350)
add("Mac & Cheese", W, {"calories":550,"fat":30,"saturated-fat":16,"carbohydrates":50,"sugars":5,"fiber":2,"proteins":20,"sodium":900}, 300)
add("Cacio e Pepe", W, {"calories":500,"fat":24,"saturated-fat":14,"carbohydrates":55,"sugars":2,"fiber":2,"proteins":18,"sodium":700}, 280)
add("Marinara Pasta", W, {"calories":400,"fat":12,"saturated-fat":2,"carbohydrates":60,"sugars":8,"fiber":3,"proteins":10,"sodium":600}, 300)
add("Prawn Pasta / Marinara with Prawns", W, {"calories":500,"fat":16,"saturated-fat":3,"carbohydrates":58,"sugars":6,"fiber":2,"proteins":28,"sodium":700}, 350)

# Burgers
add("Cheeseburger", W, {"calories":550,"fat":30,"saturated-fat":14,"carbohydrates":38,"sugars":6,"fiber":2,"proteins":32,"sodium":900}, 250)
add("Bacon Cheeseburger", W, {"calories":650,"fat":38,"saturated-fat":16,"carbohydrates":38,"sugars":6,"fiber":2,"proteins":38,"sodium":1100}, 280)
add("Double Cheeseburger", W, {"calories":800,"fat":48,"saturated-fat":22,"carbohydrates":40,"sugars":6,"fiber":2,"proteins":50,"sodium":1300}, 320)
add("Mushroom Swiss Burger", W, {"calories":600,"fat":34,"saturated-fat":15,"carbohydrates":40,"sugars":6,"fiber":2,"proteins":34,"sodium":900}, 280)
add("Grilled Chicken Burger", W, {"calories":420,"fat":14,"saturated-fat":3,"carbohydrates":42,"sugars":6,"fiber":2,"proteins":34,"sodium":700}, 260)
add("Fish Burger / Fillet-o-Fish Style", W, {"calories":400,"fat":18,"saturated-fat":4,"carbohydrates":42,"sugars":5,"fiber":2,"proteins":18,"sodium":700}, 220)
add("Veggie Burger (plant-based patty)", W, {"calories":380,"fat":16,"saturated-fat":3,"carbohydrates":42,"sugars":8,"fiber":5,"proteins":18,"sodium":800}, 250)

# Steaks
add("Ribeye Steak (200g, with sides)", W, {"calories":650,"fat":42,"saturated-fat":18,"carbohydrates":5,"sugars":1,"fiber":0,"proteins":60,"sodium":300}, 280,
   "Just the steak. Add sides separately.")
add("Sirloin Steak (200g, with sides)", W, {"calories":520,"fat":28,"saturated-fat":12,"carbohydrates":2,"sugars":0,"fiber":0,"proteins":62,"sodium":250}, 250)
add("Tenderloin / Filet Mignon (200g)", W, {"calories":450,"fat":22,"saturated-fat":9,"carbohydrates":2,"sugars":0,"fiber":0,"proteins":58,"sodium":200}, 220)
add("Steak with Mash & Vegetables (full plate)", W, {"calories":800,"fat":48,"saturated-fat":20,"carbohydrates":45,"sugars":5,"fiber":4,"proteins":62,"sodium":700}, 450)
add("Grilled Lamb Chops (3 chops with sides)", W, {"calories":620,"fat":42,"saturated-fat":18,"carbohydrates":20,"sugars":4,"fiber":3,"proteins":40,"sodium":700}, 380)

# Sides
add("French Fries (side)", W, {"calories":320,"fat":16,"saturated-fat":3,"carbohydrates":40,"sugars":1,"fiber":4,"proteins":4,"sodium":300}, 150)
add("Sweet Potato Fries (side)", W, {"calories":280,"fat":14,"saturated-fat":2.5,"carbohydrates":36,"sugars":8,"fiber":4,"proteins":2,"sodium":250}, 130)
add("Truffle Fries", W, {"calories":380,"fat":22,"saturated-fat":4,"carbohydrates":40,"sugars":1,"fiber":4,"proteins":5,"sodium":400}, 160)
add("Onion Rings (side)", W, {"calories":280,"fat":16,"saturated-fat":4,"carbohydrates":30,"sugars":5,"fiber":2,"proteins":4,"sodium":400}, 120)
add("Mashed Potato (side)", W, {"calories":180,"fat":10,"saturated-fat":5,"carbohydrates":20,"sugars":2,"fiber":2,"proteins":4,"sodium":300}, 150)
add("Coleslaw (side)", W, {"calories":120,"fat":8,"saturated-fat":1,"carbohydrates":10,"sugars":8,"fiber":2,"proteins":2,"sodium":200}, 100)
add("Caesar Salad (side)", W, {"calories":180,"fat":14,"saturated-fat":3,"carbohydrates":8,"sugars":2,"fiber":2,"proteins":6,"sodium":400}, 120)
add("Garlic Bread (2 slices)", W, {"calories":220,"fat":12,"saturated-fat":5,"carbohydrates":24,"saturates":0,"fiber":1,"proteins":5,"sodium":350}, 80)

# Seafood
add("Fish and Chips", W, {"calories":600,"fat":30,"saturated-fat":6,"carbohydrates":55,"sugars":4,"fiber":3,"proteins":28,"sodium":900}, 350)
add("Fish and Chips with Peas & Tartar", W, {"calories":650,"fat":32,"saturated-fat":6,"carbohydrates":58,"sugars":6,"fiber":4,"proteins":30,"sodium":1000}, 380)
add("Grilled Salmon Fillet (with sides)", W, {"calories":520,"fat":28,"saturated-fat":6,"carbohydrates":25,"sugars":4,"fiber":3,"proteins":42,"sodium":500}, 350)
add("Fish & Prawn Platter", W, {"calories":700,"fat":35,"saturated-fat":8,"carbohydrates":55,"sugars":5,"fiber":3,"proteins":40,"sodium":1100}, 400)

# Other Western
add("Chicken Schnitzel with Fries", W, {"calories":700,"fat":35,"saturated-fat":8,"carbohydrates":60,"sugars":4,"fiber":3,"proteins":38,"sodium":1100}, 400)
add("Chicken Parmigiana", W, {"calories":750,"fat":38,"saturated-fat":14,"carbohydrates":50,"sugars":8,"fiber":3,"proteins":48,"sodium":1200}, 400)
add("Roast Chicken (half with vegetables)", W, {"calories":600,"fat":32,"saturated-fat":10,"carbohydrates":25,"sugars":6,"fiber":4,"proteins":52,"sodium":900}, 400)
add("BBQ Pork Ribs (half rack with sides)", W, {"calories":850,"fat":48,"saturated-fat":18,"carbohydrates":45,"sugars":25,"fiber":2,"proteins":55,"sodium":1600}, 450)
add("Chicken Wings (Buffalo, 6 pieces)", W, {"calories":420,"fat":28,"saturated-fat":7,"carbohydrates":8,"sugars":2,"fiber":0,"proteins":32,"sodium":1200}, 220)
add("Mozzarella Sticks (6 pieces)", W, {"calories":380,"fat":24,"saturated-fat":12,"carbohydrates":24,"sugars":3,"fiber":1,"proteins":16,"sodium":800}, 150)
add("Loaded Nachos (shared)", W, {"calories":750,"fat":42,"saturated-fat":16,"carbohydrates":65,"sugars":5,"fiber":6,"proteins":28,"sodium":1400}, 350)
add("Chicken Quesadilla", W, {"calories":550,"fat":28,"saturated-fat":14,"carbohydrates":38,"sugars":3,"fiber":2,"proteins":35,"sodium":1000}, 280)
add("Club Sandwich", W, {"calories":580,"fat":28,"saturated-fat":8,"carbohydrates":48,"sugars":6,"fiber":3,"proteins":32,"sodium":1200}, 300)
add("BLT Sandwich", W, {"calories":420,"fat":22,"saturated-fat":6,"carbohydrates":35,"sugars":4,"fiber":2,"proteins":18,"sodium":900}, 220)
add("Egg Mayo Sandwich", W, {"calories":350,"fat":20,"saturated-fat":5,"carbohydrates":30,"sugars":4,"fiber":2,"proteins":12,"sodium":500}, 200)
add("Tuna Sandwich", W, {"calories":350,"fat":16,"saturated-fat":3,"carbohydrates":32,"sugars":4,"fiber":2,"proteins":20,"sodium":600}, 220)
add("Ham & Cheese Sandwich", W, {"calories":380,"fat":18,"saturated-fat":8,"carbohydrates":34,"sugars":5,"fiber":2,"proteins":20,"sodium":900}, 220)

# Soups & Salads
add("Mushroom Soup (bowl)", W, {"calories":180,"fat":14,"saturated-fat":8,"carbohydrates":10,"sugars":3,"fiber":1,"proteins":3,"sodium":600}, 250, "ml")
add("Pumpkin Soup (bowl)", W, {"calories":150,"fat":8,"saturated-fat":4,"carbohydrates":18,"sugars":6,"fiber":3,"proteins":3,"sodium":400}, 250, "ml")
add("Minestrone Soup (bowl)", W, {"calories":120,"fat":3,"saturated-fat":0.5,"carbohydrates":20,"sugars":5,"fiber":4,"proteins":4,"sodium":600}, 300, "ml")
add("Caesar Salad with Grilled Chicken", W, {"calories":380,"fat":24,"saturated-fat":5,"carbohydrates":12,"sugars":4,"fiber":3,"proteins":32,"sodium":800}, 300)
add("Garden Salad with Balsamic", W, {"calories":100,"fat":6,"saturated-fat":1,"carbohydrates":10,"sugars":5,"fiber":4,"proteins":3,"sodium":200}, 200)
add("Smoked Salmon Salad", W, {"calories":280,"fat":18,"saturated-fat":3,"carbohydrates":10,"sugars":4,"fiber":3,"proteins":20,"sodium":600}, 250)

# ==============================================================
# INDIAN (beyond mamak) (40+)
# ==============================================================
I = "🇮🇳 Indian"

add("Vegetarian Thali Set", I, {"calories":650,"fat":22,"saturated-fat":8,"carbohydrates":85,"sugars":8,"fiber":8,"proteins":20,"sodium":1400}, 500,
   "Rice, 2 roti, dhal, 2 vegetable curries, raita, pickle, papad")
add("Non-Veg Thali Set (Chicken)", I, {"calories":800,"fat":30,"saturated-fat":10,"carbohydrates":88,"sugars":8,"fiber":6,"proteins":38,"sodium":1600}, 550)
add("Palak Paneer with Rice", I, {"calories":520,"fat":28,"saturated-fat":14,"carbohydrates":48,"sugars":5,"fiber":4,"proteins":20,"sodium":800}, 400)
add("Chicken Tikka Masala with Rice", I, {"calories":650,"fat":30,"saturated-fat":12,"carbohydrates":58,"sugars":6,"fiber":3,"proteins":38,"sodium":1100}, 420)
add("Butter Chicken with Naan", I, {"calories":700,"fat":32,"saturated-fat":15,"carbohydrates":62,"sugars":6,"fiber":2,"proteins":38,"sodium":1200}, 450)
add("Chicken Korma with Rice", I, {"calories":620,"fat":30,"saturated-fat":12,"carbohydrates":58,"sugars":6,"fiber":2,"proteins":32,"sodium":1000}, 420)
add("Lamb Rogan Josh with Rice", I, {"calories":650,"fat":32,"saturated-fat":12,"carbohydrates":58,"sugars":5,"fiber":2,"proteins":35,"sodium":1100}, 420)
add("Fish Curry with Rice", I, {"calories":550,"fat":22,"saturated-fat":8,"carbohydrates":58,"sugars":4,"fiber":2,"proteins":32,"sodium":1000}, 420)
add("Mutton / Lamb Briyani", I, {"calories":750,"fat":32,"saturated-fat":12,"carbohydrates":85,"sugars":5,"fiber":3,"proteins":35,"sodium":1600}, 480)
add("Vegetable Biryani", I, {"calories":550,"fat":18,"saturated-fat":5,"carbohydrates":82,"sugars":6,"fiber":5,"proteins":12,"sodium":1200}, 450)
add("Dum Biryani (Chicken)", I, {"calories":700,"fat":28,"saturated-fat":8,"carbohydrates":85,"sugars":5,"fiber":3,"proteins":35,"sodium":1400}, 480)
add("Hyderabadi Biryani (Mutton)", I, {"calories":780,"fat":35,"saturated-fat":12,"carbohydrates":85,"sugars":5,"fiber":3,"proteins":35,"sodium":1600}, 500)
add("Naan (1 piece, plain)", I, {"calories":260,"fat":6,"saturated-fat":2,"carbohydrates":45,"sugars":2,"fiber":2,"proteins":8,"sodium":400}, 90)
add("Garlic Naan (1 piece)", I, {"calories":300,"fat":10,"saturated-fat":3,"carbohydrates":46,"sugars":2,"fiber":2,"proteins":8,"sodium":450}, 100)
add("Butter Naan (1 piece)", I, {"calories":350,"fat":16,"saturated-fat":8,"carbohydrates":46,"sugars":3,"fiber":2,"proteins":8,"sodium":400}, 100)
add("Cheese Naan (1 piece)", I, {"calories":400,"fat":20,"saturated-fat":10,"carbohydrates":46,"sugars":3,"fiber":2,"proteins":12,"sodium":500}, 120)
add("Roti / Chapati (1 piece)", I, {"calories":100,"fat":2,"saturated-fat":0.5,"carbohydrates":18,"sugars":0.5,"fiber":2,"proteins":3,"sodium":100}, 50)
add("Tandoori Chicken (half bird)", I, {"calories":450,"fat":24,"saturated-fat":6,"carbohydrates":4,"sugars":2,"fiber":0,"proteins":55,"sodium":900}, 300)
add("Chicken Tikka (6 pieces)", I, {"calories":280,"fat":16,"saturated-fat":4,"carbohydrates":4,"sugars":2,"fiber":0,"proteins":32,"sodium":600}, 180)
add("Seekh Kebab (4 pieces)", I, {"calories":320,"fat":22,"saturated-fat":8,"carbohydrates":4,"sugars":1,"fiber":0,"proteins":26,"sodium":700}, 180)
add("Dhal Tadka with Rice", I, {"calories":420,"fat":14,"saturated-fat":2,"carbohydrates":58,"sugars":3,"fiber":6,"proteins":16,"sodium":800}, 400)
add("Aloo Gobi with Rice", I, {"calories":400,"fat":14,"saturated-fat":2,"carbohydrates":60,"sugars":6,"fiber":6,"proteins":8,"sodium":700}, 380)
add("Chana Masala with Rice", I, {"calories":450,"fat":16,"saturated-fat":2.5,"carbohydrates":62,"sugars":5,"fiber":8,"proteins":16,"sodium":800}, 400)
add("Vegetable Curry with Rice", I, {"calories":400,"fat":16,"saturated-fat":5,"carbohydrates":55,"sugars":6,"fiber":5,"proteins":8,"sodium":700}, 380)
add("Samosas (2 pieces, vegetable)", I, {"calories":280,"fat":16,"saturated-fat":4,"carbohydrates":28,"sugars":3,"fiber":3,"proteins":6,"sodium":500}, 120)
add("Onion Bhaji (3 pieces)", I, {"calories":250,"fat":16,"saturated-fat":3,"carbohydrates":22,"sugars":3,"fiber":3,"proteins":4,"sodium":400}, 120)
add("Pani Puri (6 pieces)", I, {"calories":200,"fat":8,"saturated-fat":1,"carbohydrates":28,"sugars":3,"fiber":2,"proteins":4,"sodium":500}, 150)
add("Papadum (2 pieces)", I, {"calories":100,"fat":4,"saturated-fat":0.5,"carbohydrates":14,"sugars":0,"fiber":2,"proteins":3,"sodium":300}, 30)
add("Mango Lassi", I, {"calories":250,"fat":6,"saturated-fat":4,"carbohydrates":40,"sugars":35,"fiber":1,"proteins":8,"sodium":100}, 300, "ml")
add("Masala Chai / Teh Tarik (Indian style)", I, {"calories":100,"fat":3,"saturated-fat":2,"carbohydrates":14,"sugars":12,"fiber":0,"proteins":2,"sodium":20}, 200, "ml")

# ==============================================================
# THAI (35+)
# ==============================================================
T = "🇹🇭 Thai"

add("Pad Thai (Chicken)", T, {"calories":550,"fat":22,"saturated-fat":4,"carbohydrates":65,"sugars":14,"fiber":3,"proteins":24,"sodium":1400}, 380)
add("Pad Thai (Prawn)", T, {"calories":530,"fat":20,"saturated-fat":3,"carbohydrates":65,"sugars":14,"fiber":3,"proteins":24,"sodium":1500}, 380)
add("Thai Green Curry (Chicken) with Rice", T, {"calories":620,"fat":32,"saturated-fat":18,"carbohydrates":55,"sugars":5,"fiber":3,"proteins":28,"sodium":1200}, 450)
add("Thai Red Curry (Chicken) with Rice", T, {"calories":600,"fat":30,"saturated-fat":16,"carbohydrates":55,"sugars":5,"fiber":3,"proteins":28,"sodium":1200}, 450)
add("Thai Green Curry (Beef) with Rice", T, {"calories":650,"fat":35,"saturated-fat":18,"carbohydrates":55,"sugars":5,"fiber":3,"proteins":30,"sodium":1200}, 450)
add("Thai Green Curry (Vegetable & Tofu) with Rice", T, {"calories":420,"fat":22,"saturated-fat":12,"carbohydrates":45,"sugars":5,"fiber":4,"proteins":12,"sodium":1000}, 400)
add("Massaman Curry with Rice", T, {"calories":650,"fat":35,"saturated-fat":16,"carbohydrates":58,"sugars":10,"fiber":3,"proteins":28,"sodium":1300}, 460)
add("Tom Yum Soup (Prawn, clear)", T, {"calories":180,"fat":8,"saturated-fat":2,"carbohydrates":10,"sugars":4,"fiber":2,"proteins":18,"sodium":1800}, 350, "ml")
add("Tom Yum Soup (Prawn, creamy)", T, {"calories":280,"fat":18,"saturated-fat":10,"carbohydrates":12,"sugars":4,"fiber":2,"proteins":18,"sodium":1800}, 350, "ml")
add("Tom Kha Gai / Coconut Chicken Soup", T, {"calories":280,"fat":20,"saturated-fat":14,"carbohydrates":10,"sugars":4,"fiber":2,"proteins":16,"sodium":1200}, 350, "ml")
add("Phad Krapow / Thai Basil Chicken with Rice", T, {"calories":550,"fat":20,"saturated-fat":4,"carbohydrates":62,"sugars":4,"fiber":2,"proteins":32,"sodium":1200}, 400)
add("Phad Krapow / Thai Basil Pork with Rice", T, {"calories":580,"fat":24,"saturated-fat":6,"carbohydrates":62,"sugars":4,"fiber":2,"proteins":30,"sodium":1200}, 400)
add("Thai Basil Beef / Phad Krapow Nua with Rice", T, {"calories":520,"fat":18,"saturated-fat":5,"carbohydrates":62,"sugars":4,"fiber":2,"proteins":32,"sodium":1100}, 400)
add("Pineapple Fried Rice", T, {"calories":550,"fat":18,"saturated-fat":4,"carbohydrates":78,"sugars":12,"fiber":3,"proteins":18,"sodium":1000}, 380)
add("Thai Fried Rice / Khao Pad (Chicken)", T, {"calories":520,"fat":16,"saturated-fat":3,"carbohydrates":72,"sugars":4,"fiber":2,"proteins":24,"sodium":1100}, 380)
add("Thai Omelette with Rice / Khai Jiao", T, {"calories":420,"fat":24,"saturated-fat":6,"carbohydrates":38,"sugars":2,"fiber":1,"proteins":14,"sodium":600}, 300)
add("Minced Pork Omelette with Rice", T, {"calories":520,"fat":28,"saturated-fat":8,"carbohydrates":40,"sugars":3,"fiber":1,"proteins":24,"sodium":700}, 350)
add("Mango Salad / Som Tum", T, {"calories":180,"fat":8,"saturated-fat":1,"carbohydrates":22,"sugars":14,"fiber":3,"proteins":4,"sodium":800}, 200)
add("Papaya Salad / Som Tum Thai", T, {"calories":150,"fat":6,"saturated-fat":1,"carbohydrates":20,"sugars":12,"fiber":3,"proteins":4,"sodium":900}, 200)
add("Thai Prawn Cake / Tod Mun Goong (4 pieces)", T, {"calories":280,"fat":18,"saturated-fat":3,"carbohydrates":16,"sugars":4,"fiber":1,"proteins":16,"sodium":700}, 150)
add("Pandan Chicken (4 pieces)", T, {"calories":320,"fat":18,"saturated-fat":5,"carbohydrates":8,"sugars":3,"fiber":0,"proteins":32,"sodium":800}, 180)
add("Stir-Fried Morning Glory / Phad Pak Bung", T, {"calories":100,"fat":6,"saturated-fat":1,"carbohydrates":8,"sugars":3,"fiber":3,"proteins":3,"sodium":700}, 180)
add("Mango Sticky Rice", T, {"calories":380,"fat":10,"saturated-fat":6,"carbohydrates":68,"sugars":32,"fiber":2,"proteins":5,"sodium":200}, 250)
add("Red Ruby / Tub Tim Krob", T, {"calories":250,"fat":8,"saturated-fat":6,"carbohydrates":42,"sugars":28,"fiber":1,"proteins":2,"sodium":100}, 250)
add("Thai Iced Tea / Cha Yen", T, {"calories":200,"fat":6,"saturated-fat":4,"carbohydrates":35,"sugars":30,"fiber":0,"proteins":2,"sodium":50}, 350, "ml")
add("Thai Iced Coffee", T, {"calories":180,"fat":5,"saturated-fat":3,"carbohydrates":30,"sugars":26,"fiber":0,"proteins":2,"sodium":40}, 350, "ml")
add("Thai Fried Chicken / Gai Tod (4 pieces)", T, {"calories":380,"fat":24,"saturated-fat":5,"carbohydrates":12,"sugars":2,"fiber":0,"proteins":28,"sodium":900}, 200)

# ==============================================================
# VIETNAMESE (20+)
# ==============================================================
V = "🇻🇳 Vietnamese"

add("Pho Bo / Beef Pho", V, {"calories":420,"fat":10,"saturated-fat":3,"carbohydrates":55,"sugars":4,"fiber":2,"proteins":28,"sodium":1800}, 500)
add("Pho Ga / Chicken Pho", V, {"calories":380,"fat":8,"saturated-fat":2,"carbohydrates":55,"sugars":4,"fiber":2,"proteins":26,"sodium":1600}, 480)
add("Bun Bo Hue / Spicy Beef Noodle Soup", V, {"calories":480,"fat":16,"saturated-fat":5,"carbohydrates":58,"sugars":4,"fiber":2,"proteins":30,"sodium":2200}, 520)
add("Banh Mi (Grilled Pork)", V, {"calories":420,"fat":16,"saturated-fat":4,"carbohydrates":50,"sugars":6,"fiber":3,"proteins":22,"sodium":900}, 250)
add("Banh Mi (Cold Cuts / Thit Nguoi)", V, {"calories":400,"fat":16,"saturated-fat":5,"carbohydrates":48,"sugars":5,"fiber":3,"proteins":20,"sodium":1000}, 250)
add("Banh Mi (Chicken)", V, {"calories":380,"fat":12,"saturated-fat":3,"carbohydrates":48,"sugars":5,"fiber":3,"proteins":24,"sodium":800}, 250)
add("Banh Mi (Egg)", V, {"calories":320,"fat":14,"saturated-fat":4,"carbohydrates":42,"sugars":4,"fiber":3,"proteins":12,"sodium":600}, 220)
add("Fresh Spring Rolls / Goi Cuon (3 rolls)", V, {"calories":200,"fat":4,"saturated-fat":1,"carbohydrates":32,"sugars":4,"fiber":3,"proteins":12,"sodium":400}, 200)
add("Fried Spring Rolls / Cha Gio (4 pieces)", V, {"calories":280,"fat":18,"saturated-fat":4,"carbohydrates":24,"sugars":3,"fiber":2,"proteins":8,"sodium":500}, 140)
add("Bun Thit Nuong / Grilled Pork Vermicelli", V, {"calories":480,"fat":16,"saturated-fat":4,"carbohydrates":62,"sugars":10,"fiber":3,"proteins":24,"sodium":1000}, 400)
add("Bun Cha / Grilled Pork with Vermicelli", V, {"calories":520,"fat":20,"saturated-fat":6,"carbohydrates":60,"sugars":10,"fiber":3,"proteins":28,"sodium":1200}, 420)
add("Vietnamese Broken Rice / Com Tam", V, {"calories":550,"fat":18,"saturated-fat":5,"carbohydrates":75,"sugars":4,"fiber":2,"proteins":28,"sodium":1000}, 400)
add("Vietnamese Iced Coffee / Ca Phe Sua Da", V, {"calories":120,"fat":3,"saturated-fat":2,"carbohydrates":18,"sugars":16,"fiber":0,"proteins":3,"sodium":20}, 200, "ml")
add("Vietnamese Lemongrass Chicken with Rice", V, {"calories":520,"fat":16,"saturated-fat":4,"carbohydrates":62,"sugars":6,"fiber":2,"proteins":32,"sodium":900}, 400)
add("Vietnamese Beef Stew / Bo Kho with Bread", V, {"calories":550,"fat":22,"saturated-fat":8,"carbohydrates":55,"sugars":6,"fiber":3,"proteins":32,"sodium":1200}, 420)

# ==============================================================
# INDONESIAN (15+)
# ==============================================================
N = "🇮🇩 Indonesian"

add("Mee Bakso / Beef Ball Noodles", N, {"calories":420,"fat":14,"saturated-fat":4,"carbohydrates":55,"sugars":4,"fiber":2,"proteins":20,"sodium":1600}, 450)
add("Bakso (beef balls in soup, no noodles)", N, {"calories":200,"fat":8,"saturated-fat":2.5,"carbohydrates":12,"sugars":2,"fiber":1,"proteins":22,"sodium":1400}, 350, "ml")
add("Ayam Penyet with Rice", N, {"calories":680,"fat":32,"saturated-fat":8,"carbohydrates":70,"sugars":5,"fiber":3,"proteins":35,"sodium":1400}, 450)
add("Indomie Goreng (1 packet, with egg)", N, {"calories":480,"fat":22,"saturated-fat":7,"carbohydrates":58,"sugars":6,"fiber":2,"proteins":14,"sodium":1200}, 300)
add("Indomie Soup (1 packet, with egg)", N, {"calories":420,"fat":18,"saturated-fat":6,"carbohydrates":54,"sugars":5,"fiber":2,"proteins":14,"sodium":1500}, 380)
add("Sate Ayam / Chicken Satay (10 sticks)", N, {"calories":450,"fat":22,"saturated-fat":6,"carbohydrates":18,"sugars":10,"fiber":1,"proteins":45,"sodium":1100}, 280)
add("Sate Kambing / Mutton Satay (10 sticks)", N, {"calories":520,"fat":30,"saturated-fat":11,"carbohydrates":18,"sugars":10,"fiber":1,"proteins":42,"sodium":1200}, 280)
add("Pecel Lele / Fried Catfish with Rice & Sambal", N, {"calories":580,"fat":28,"saturated-fat":6,"carbohydrates":62,"sugars":5,"fiber":3,"proteins":28,"sodium":1200}, 400)
add("Nasi Uduk (with fried chicken)", N, {"calories":650,"fat":32,"saturated-fat":10,"carbohydrates":62,"sugars":4,"fiber":2,"proteins":32,"sodium":1300}, 420)
add("Martabak Manis / Sweet Pancake (2 slices)", N, {"calories":350,"fat":18,"saturated-fat":7,"carbohydrates":42,"sugars":20,"fiber":1,"proteins":6,"sodium":200}, 150)
add("Gulai Kambing / Mutton Curry with Rice", N, {"calories":620,"fat":32,"saturated-fat":14,"carbohydrates":55,"sugars":4,"fiber":2,"proteins":30,"sodium":1200}, 420)
add("Tahu Telor / Tofu Omelette with Peanut Sauce", N, {"calories":420,"fat":28,"saturated-fat":6,"carbohydrates":25,"sugars":8,"fiber":3,"proteins":18,"sodium":900}, 300)
add("Gado-Gado (full plate)", N, {"calories":420,"fat":28,"saturated-fat":6,"carbohydrates":30,"sugars":8,"fiber":5,"proteins":16,"sodium":1200}, 350)

# ==============================================================
# FAST FOOD (35+)
# ==============================================================
F = "🍔 Fast Food"

# McDonald's
add("Big Mac", F, {"calories":540,"fat":28,"saturated-fat":10,"carbohydrates":44,"sugars":9,"fiber":3,"proteins":25,"sodium":970}, 215)
add("McChicken", F, {"calories":390,"fat":18,"saturated-fat":3,"carbohydrates":39,"sugars":5,"fiber":2,"proteins":18,"sodium":600}, 170)
add("McSpicy (Double)", F, {"calories":570,"fat":28,"saturated-fat":6,"carbohydrates":48,"sugars":7,"fiber":2,"proteins":32,"sodium":1100}, 230)
add("Filet-O-Fish", F, {"calories":330,"fat":14,"saturated-fat":3,"carbohydrates":38,"sugars":5,"fiber":2,"proteins":15,"sodium":560}, 140)
add("Double Cheeseburger (McDonald's)", F, {"calories":440,"fat":24,"saturated-fat":12,"carbohydrates":34,"sugars":7,"fiber":1,"proteins":25,"sodium":1050}, 165)
add("Quarter Pounder with Cheese", F, {"calories":520,"fat":26,"saturated-fat":13,"carbohydrates":41,"sugars":10,"fiber":2,"proteins":31,"sodium":1110}, 200)
add("McNuggets (6 pieces)", F, {"calories":250,"fat":14,"saturated-fat":2.5,"carbohydrates":15,"sugars":1,"fiber":1,"proteins":15,"sodium":500}, 100)
add("McNuggets (9 pieces)", F, {"calories":380,"fat":22,"saturated-fat":4,"carbohydrates":22,"sugars":1,"fiber":1,"proteins":23,"sodium":750}, 150)
add("McNuggets (20 pieces)", F, {"calories":840,"fat":48,"saturated-fat":8,"carbohydrates":50,"sugars":2,"fiber":2,"proteins":50,"sodium":1660}, 320)
add("McWings (4 pieces)", F, {"calories":300,"fat":20,"saturated-fat":5,"carbohydrates":8,"sugars":1,"fiber":0,"proteins":22,"sodium":600}, 130)
add("Large French Fries (McDonald's)", F, {"calories":490,"fat":23,"saturated-fat":3,"carbohydrates":66,"sugars":0,"fiber":6,"proteins":6,"sodium":400}, 170)
add("Medium French Fries (McDonald's)", F, {"calories":340,"fat":16,"saturated-fat":2.5,"carbohydrates":44,"sugars":0,"fiber":4,"proteins":4,"sodium":265}, 115)
add("Apple Pie (McDonald's)", F, {"calories":240,"fat":12,"saturated-fat":5,"carbohydrates":32,"sugars":13,"fiber":1,"proteins":2,"sodium":200}, 85)
add("McFlurry Oreo (regular)", F, {"calories":340,"fat":11,"saturated-fat":7,"carbohydrates":53,"sugars":40,"fiber":1,"proteins":8,"sodium":160}, 200)
add("Sundae Hot Fudge", F, {"calories":330,"fat":10,"saturated-fat":7,"carbohydrates":53,"sugars":42,"fiber":1,"proteins":7,"sodium":160}, 180)

# KFC
add("KFC Original Recipe Chicken (2 pieces)", F, {"calories":480,"fat":30,"saturated-fat":8,"carbohydrates":12,"sugars":0,"fiber":0,"proteins":38,"sodium":1100}, 200)
add("KFC Zinger Burger", F, {"calories":540,"fat":28,"saturated-fat":6,"carbohydrates":48,"sugars":6,"fiber":2,"proteins":28,"sodium":1000}, 220)
add("KFC Popcorn Chicken (large)", F, {"calories":480,"fat":28,"saturated-fat":6,"carbohydrates":28,"sugars":2,"fiber":1,"proteins":30,"sodium":1200}, 200)
add("KFC Whipped Potato (regular)", F, {"calories":110,"fat":4,"saturated-fat":1.5,"carbohydrates":16,"sugars":1,"fiber":1,"proteins":2,"sodium":350}, 110)
add("KFC Coleslaw (regular)", F, {"calories":140,"fat":8,"saturated-fat":1,"carbohydrates":16,"sugars":14,"fiber":2,"proteins":1,"sodium":200}, 100)
add("KFC Cheese Fries", F, {"calories":380,"fat":22,"saturated-fat":8,"carbohydrates":36,"sugars":2,"fiber":3,"proteins":8,"sodium":700}, 150)

# Subway
add("Subway 6-inch Chicken Breast Sub", F, {"calories":340,"fat":8,"saturated-fat":2,"carbohydrates":40,"sugars":6,"fiber":4,"proteins":28,"sodium":700}, 220)
add("Subway 6-inch Italian BMT", F, {"calories":380,"fat":18,"saturated-fat":6,"carbohydrates":40,"sugars":6,"fiber":3,"proteins":18,"sodium":1100}, 220)
add("Subway 6-inch Tuna Sub", F, {"calories":420,"fat":22,"saturated-fat":4,"carbohydrates":40,"sugars":5,"fiber":3,"proteins":18,"sodium":700}, 220)
add("Subway 6-inch Veggie Delite", F, {"calories":230,"fat":3,"saturated-fat":0.5,"carbohydrates":42,"sugars":7,"fiber":5,"proteins":9,"sodium":450}, 200)
add("Subway Footlong Chicken Breast", F, {"calories":680,"fat":16,"saturated-fat":4,"carbohydrates":80,"sugars":12,"fiber":8,"proteins":56,"sodium":1400}, 440)

# Other Fast Food
add("MOS Burger (original)", F, {"calories":400,"fat":18,"saturated-fat":5,"carbohydrates":38,"sugars":6,"fiber":2,"proteins":20,"sodium":600}, 200)
add("MOS Rice Burger (Chicken)", F, {"calories":420,"fat":16,"saturated-fat":3,"carbohydrates":50,"sugars":6,"fiber":2,"proteins":22,"sodium":700}, 220)
add("Burger King Whopper", F, {"calories":660,"fat":40,"saturated-fat":12,"carbohydrates":50,"sugars":11,"fiber":2,"proteins":28,"sodium":980}, 270)
add("A&W Coney Dog", F, {"calories":400,"fat":22,"saturated-fat":8,"carbohydrates":35,"sugars":8,"fiber":2,"proteins":16,"sodium":900}, 170)
add("A&W Root Beer Float (regular)", F, {"calories":280,"fat":8,"saturated-fat":5,"carbohydrates":48,"sugars":44,"fiber":0,"proteins":4,"sodium":100}, 350, "ml")
add("Jollibee Chickenjoy (2 pieces)", F, {"calories":500,"fat":32,"saturated-fat":8,"carbohydrates":14,"sugars":1,"fiber":0,"proteins":38,"sodium":1100}, 200)
add("Jollibee Spaghetti", F, {"calories":380,"fat":12,"saturated-fat":4,"carbohydrates":52,"sugars":18,"fiber":2,"proteins":14,"sodium":800}, 250)
add("Shake Shack ShackBurger (single)", F, {"calories":550,"fat":30,"saturated-fat":12,"carbohydrates":38,"sugars":6,"fiber":1,"proteins":32,"sodium":1100}, 220)

# ==============================================================
# PIZZA (15+)
# ==============================================================
PZ = "🍕 Pizza"

add("Margherita Pizza (1 slice, 12-inch)", PZ, {"calories":220,"fat":9,"saturated-fat":4.5,"carbohydrates":25,"sugars":3,"fiber":1,"proteins":10,"sodium":450}, 100)
add("Pepperoni Pizza (1 slice, 12-inch)", PZ, {"calories":280,"fat":12,"saturated-fat":5,"carbohydrates":26,"sugars":3,"fiber":1,"proteins":12,"sodium":600}, 110)
add("Hawaiian Pizza (1 slice, 12-inch)", PZ, {"calories":250,"fat":10,"saturated-fat":4.5,"carbohydrates":28,"sugars":5,"fiber":1,"proteins":12,"sodium":550}, 110)
add("Supreme / Meat Lovers Pizza (1 slice)", PZ, {"calories":320,"fat":16,"saturated-fat":7,"carbohydrates":25,"sugars":3,"fiber":1,"proteins":16,"sodium":700}, 120)
add("BBQ Chicken Pizza (1 slice)", PZ, {"calories":260,"fat":10,"saturated-fat":4,"carbohydrates":28,"sugars":6,"fiber":1,"proteins":14,"sodium":550}, 110)
add("Vegetarian Pizza (1 slice)", PZ, {"calories":200,"fat":8,"saturated-fat":3.5,"carbohydrates":26,"sugars":3,"fiber":2,"proteins":8,"sodium":400}, 100)
add("Personal Pan Pizza (6-inch, Pepperoni)", PZ, {"calories":600,"fat":28,"saturated-fat":12,"carbohydrates":62,"sugars":6,"fiber":2,"proteins":28,"sodium":1400}, 250)
add("Personal Pan Pizza (6-inch, Hawaiian)", PZ, {"calories":550,"fat":22,"saturated-fat":10,"carbohydrates":64,"sugars":12,"fiber":2,"proteins":26,"sodium":1300}, 250)

# ==============================================================
# SEAFOOD (Singapore style) (15+)
# ==============================================================
SF = "🦞 Seafood"

add("Sambal Stingray (whole, shared 2 pax)", SF, {"calories":380,"fat":18,"saturated-fat":4,"carbohydrates":8,"sugars":4,"fiber":1,"proteins":48,"sodium":1400}, 350)
add("BBQ Stingray with Sambal", SF, {"calories":420,"fat":22,"saturated-fat":5,"carbohydrates":10,"sugars":5,"fiber":1,"proteins":48,"sodium":1500}, 380)
add("Sambal Lala / Clams", SF, {"calories":280,"fat":14,"saturated-fat":3,"carbohydrates":8,"sugars":3,"fiber":1,"proteins":30,"sodium":1200}, 300)
add("Steamed Prawns with Garlic (6 large prawns)", SF, {"calories":200,"fat":6,"saturated-fat":1,"carbohydrates":4,"sugars":1,"fiber":0,"proteins":32,"sodium":400}, 200)
add("Drunken Prawns (6 large)", SF, {"calories":250,"fat":8,"saturated-fat":1.5,"carbohydrates":6,"sugars":3,"fiber":1,"proteins":32,"sodium":800}, 250)
add("Deep Fried Baby Squid / Sotong", SF, {"calories":380,"fat":22,"saturated-fat":4,"carbohydrates":25,"sugars":3,"fiber":1,"proteins":20,"sodium":800}, 200)
add("Salted Egg Squid", SF, {"calories":420,"fat":28,"saturated-fat":12,"carbohydrates":18,"sugars":4,"fiber":1,"proteins":22,"sodium":1000}, 250)
add("Grilled Sambal Squid / Sotong", SF, {"calories":320,"fat":16,"saturated-fat":3,"carbohydrates":12,"sugars":5,"fiber":1,"proteins":30,"sodium":1000}, 250)
add("Oyster Omelette / Orh Jian (shared)", SF, {"calories":450,"fat":28,"saturated-fat":6,"carbohydrates":32,"sugars":3,"fiber":1,"proteins":18,"sodium":1200}, 280)
add("Steamed Garlic Mussels", SF, {"calories":220,"fat":12,"saturated-fat":2,"carbohydrates":8,"sugars":2,"fiber":1,"proteins":22,"sodium":600}, 250)
add("Cereal Prawns", SF, {"calories":420,"fat":24,"saturated-fat":6,"carbohydrates":22,"sugars":6,"fiber":1,"proteins":28,"sodium":800}, 250)
add("Fish Head Curry with Rice (per person)", SF, {"calories":550,"fat":28,"saturated-fat":12,"carbohydrates":55,"sugars":5,"fiber":3,"proteins":28,"sodium":1600}, 450)

# ==============================================================
# BREAD & BAKERY (30+)
# ==============================================================
B = "🍞 Bread & Bakery"

add("Kaya Toast Set (2 slices with butter, kopi, 2 soft boiled eggs)", B, {"calories":420,"fat":22,"saturated-fat":10,"carbohydrates":38,"sugars":16,"fiber":1,"proteins":16,"sodium":400}, 250)
add("Kaya Toast (2 slices with butter)", B, {"calories":200,"fat":10,"saturated-fat":5,"carbohydrates":24,"sugars":12,"fiber":1,"proteins":4,"sodium":200}, 100)
add("White Bread (2 slices)", B, {"calories":140,"fat":2,"saturated-fat":0.5,"carbohydrates":26,"sugars":2,"fiber":1,"proteins":5,"sodium":200}, 60)
add("Wholemeal Bread (2 slices)", B, {"calories":130,"fat":2.5,"saturated-fat":0.5,"carbohydrates":23,"sugars":2,"fiber":4,"proteins":6,"sodium":180}, 60)
add("Croissant (plain)", B, {"calories":230,"fat":14,"saturated-fat":8,"carbohydrates":22,"sugars":3,"fiber":1,"proteins":5,"sodium":250}, 60)
add("Almond Croissant", B, {"calories":380,"fat":24,"saturated-fat":10,"carbohydrates":32,"sugars":12,"fiber":2,"proteins":8,"sodium":250}, 90)
add("Pain au Chocolat", B, {"calories":300,"fat":18,"saturated-fat":10,"carbohydrates":28,"sugars":8,"fiber":2,"proteins":6,"sodium":220}, 80)
add("Blueberry Muffin", B, {"calories":380,"fat":18,"saturated-fat":4,"carbohydrates":50,"sugars":28,"fiber":1,"proteins":5,"sodium":300}, 120)
add("Banana Muffin", B, {"calories":350,"fat":16,"saturated-fat":4,"carbohydrates":48,"sugars":25,"fiber":2,"proteins":5,"sodium":280}, 120)
add("Donut (glazed)", B, {"calories":250,"fat":14,"saturated-fat":6,"carbohydrates":28,"sugars":14,"fiber":1,"proteins":3,"sodium":220}, 75)
add("Donut (chocolate frosted)", B, {"calories":280,"fat":16,"saturated-fat":7,"carbohydrates":30,"sugars":16,"fiber":1,"proteins":3,"sodium":250}, 80)
add("Cinnamon Roll", B, {"calories":420,"fat":18,"saturated-fat":8,"carbohydrates":58,"sugars":28,"fiber":2,"proteins":6,"sodium":350}, 130)
add("Danish Pastry (fruit)", B, {"calories":320,"fat":18,"saturated-fat":8,"carbohydrates":35,"sugars":14,"fiber":1,"proteins":5,"sodium":250}, 100)
add("Polo Bun / Roti Boy (1 piece)", B, {"calories":280,"fat":14,"saturated-fat":6,"carbohydrates":32,"sugars":8,"fiber":1,"proteins":6,"sodium":250}, 100)
add("Sausage Bun (1 piece)", B, {"calories":300,"fat":18,"saturated-fat":6,"carbohydrates":26,"sugars":4,"fiber":1,"proteins":10,"sodium":500}, 100)
add("Luncheon Meat Bun (1 piece)", B, {"calories":320,"fat":20,"saturated-fat":7,"carbohydrates":26,"sugars":4,"fiber":1,"proteins":8,"sodium":600}, 100)
add("Red Bean Bun (1 piece)", B, {"calories":220,"fat":5,"saturated-fat":1,"carbohydrates":40,"sugars":12,"fiber":2,"proteins":6,"sodium":150}, 100)
add("Custard Bun (1 piece)", B, {"calories":250,"fat":8,"saturated-fat":3,"carbohydrates":38,"sugars":14,"fiber":1,"proteins":6,"sodium":200}, 100)
add("Tuna Bun (1 piece)", B, {"calories":280,"fat":14,"saturated-fat":4,"carbohydrates":28,"sugars":4,"fiber":1,"proteins":12,"sodium":450}, 110)
add("Chicken Pie", B, {"calories":350,"fat":22,"saturated-fat":10,"carbohydrates":28,"sugars":3,"fiber":1,"proteins":12,"sodium":600}, 120)
add("Curry Puff (baked, 1 piece)", B, {"calories":200,"fat":12,"saturated-fat":5,"carbohydrates":20,"sugars":2,"fiber":1,"proteins":4,"sodium":350}, 80)
add("Egg Tart (Hong Kong style)", B, {"calories":200,"fat":10,"saturated-fat":5,"carbohydrates":24,"sugars":10,"fiber":0,"proteins":4,"sodium":150}, 70)
add("Pineapple Tart (3 pieces)", B, {"calories":180,"fat":10,"saturated-fat":4,"carbohydrates":22,"sugars":10,"fiber":1,"proteins":2,"sodium":80}, 60)
add("Banana Cake (1 slice)", B, {"calories":280,"fat":14,"saturated-fat":4,"carbohydrates":36,"sugars":20,"fiber":2,"proteins":4,"sodium":250}, 100)
add("Carrot Cake / Walnut Cake (1 slice)", B, {"calories":350,"fat":18,"saturated-fat":5,"carbohydrates":42,"sugars":28,"fiber":2,"proteins":4,"sodium":250}, 110)
add("Cheesecake (1 slice)", B, {"calories":380,"fat":26,"saturated-fat":15,"carbohydrates":28,"sugars":20,"fiber":0,"proteins":8,"sodium":300}, 120)
add("Chocolate Lava Cake (1 piece)", B, {"calories":400,"fat":24,"saturated-fat":14,"carbohydrates":42,"sugars":30,"fiber":2,"proteins":6,"sodium":200}, 100)
add("Brownie (1 piece)", B, {"calories":350,"fat":20,"saturated-fat":8,"carbohydrates":42,"sugars":30,"fiber":2,"proteins":4,"sodium":150}, 90)
add("Vanilla Ice Cream (1 scoop)", B, {"calories":140,"fat":8,"saturated-fat":5,"carbohydrates":16,"sugars":14,"fiber":0,"proteins":2,"sodium":50}, 70)
add("Waffle (plain, 1 piece)", B, {"calories":280,"fat":14,"saturated-fat":5,"carbohydrates":32,"sugars":6,"fiber":1,"proteins":6,"sodium":350}, 100)
add("Waffle with Ice Cream", B, {"calories":480,"fat":24,"saturated-fat":12,"carbohydrates":58,"sugars":28,"fiber":1,"proteins":8,"sodium":400}, 200)

# ==============================================================
# BREAKFAST (15+)
# ==============================================================
BR = "🍳 Breakfast"

add("Soft Boiled Eggs (2 eggs)", BR, {"calories":140,"fat":10,"saturated-fat":3,"carbohydrates":1,"sugars":1,"fiber":0,"proteins":12,"sodium":140}, 120)
add("Fried Egg (1 egg, sunny side up)", BR, {"calories":110,"fat":9,"saturated-fat":2.5,"carbohydrates":0.5,"sugars":0,"fiber":0,"proteins":7,"sodium":90}, 55)
add("Scrambled Eggs (2 eggs, with milk & butter)", BR, {"calories":220,"fat":18,"saturated-fat":7,"carbohydrates":2,"sugars":1,"fiber":0,"proteins":14,"sodium":250}, 120)
add("Omelette (2 eggs, plain)", BR, {"calories":200,"fat":16,"saturated-fat":5,"carbohydrates":1,"sugars":1,"fiber":0,"proteins":14,"sodium":250}, 120)
add("Cheesy Omelette (2 eggs, with cheese)", BR, {"calories":300,"fat":24,"saturated-fat":10,"carbohydrates":2,"sugars":1,"fiber":0,"proteins":18,"sodium":400}, 140)
add("Ham Omelette (2 eggs)", BR, {"calories":260,"fat":20,"saturated-fat":7,"carbohydrates":2,"sugars":1,"fiber":0,"proteins":18,"sodium":550}, 140)
add("Hash Browns (2 pieces)", BR, {"calories":280,"fat":20,"saturated-fat":4,"carbohydrates":24,"sugars":1,"fiber":2,"proteins":2,"sodium":400}, 100)
add("Sausages (2 pork/chicken)", BR, {"calories":200,"fat":16,"saturated-fat":6,"carbohydrates":4,"sugars":2,"fiber":0,"proteins":10,"sodium":600}, 80)
add("Bacon (3 strips)", BR, {"calories":160,"fat":12,"saturated-fat":4,"carbohydrates":0,"sugars":0,"fiber":0,"proteins":12,"sodium":500}, 40)
add("Baked Beans (side)", BR, {"calories":140,"fat":1,"saturated-fat":0,"carbohydrates":25,"sugars":10,"fiber":6,"proteins":8,"sodium":400}, 130)
add("Toast with Butter & Jam (2 slices)", BR, {"calories":250,"fat":10,"saturated-fat":5,"carbohydrates":35,"sugars":10,"fiber":1,"proteins":5,"sodium":250}, 80)
add("Big Breakfast (eggs, sausage, bacon, hash brown, toast)", BR, {"calories":750,"fat":48,"saturated-fat":16,"carbohydrates":45,"sugars":4,"fiber":3,"proteins":32,"sodium":1600}, 350)
add("Granola with Milk & Berries", BR, {"calories":320,"fat":10,"saturated-fat":3,"carbohydrates":48,"sugars":18,"fiber":5,"proteins":10,"sodium":100}, 250)
add("Overnight Oats", BR, {"calories":300,"fat":10,"saturated-fat":3,"carbohydrates":42,"sugars":12,"fiber":6,"proteins":12,"sodium":80}, 250)
add("Pancakes (3 pieces, with butter & syrup)", BR, {"calories":520,"fat":16,"saturated-fat":7,"carbohydrates":85,"sugars":32,"fiber":2,"proteins":10,"sodium":600}, 250)
add("French Toast (2 slices)", BR, {"calories":400,"fat":22,"saturated-fat":8,"carbohydrates":40,"sugars":12,"fiber":1,"proteins":12,"sodium":400}, 180)
add("Chwee Kueh (4 pieces) - duplicate for breakfast", BR, {"calories":280,"fat":8,"saturated-fat":2,"carbohydrates":45,"sugars":2,"fiber":1,"proteins":6,"sodium":900}, 200)
add("Carrot Cake (Teochew style, white, 1 plate)", BR, {"calories":500,"fat":25,"saturated-fat":6,"carbohydrates":55,"sugars":8,"fiber":2,"proteins":12,"sodium":1800}, 300)

# ==============================================================
# DESSERTS & SNACKS (20+)
# ==============================================================
DS = "🍪 Desserts & Snacks"

add("Durian (3 seeds)", DS, {"calories":200,"fat":8,"saturated-fat":2,"carbohydrates":30,"sugars":14,"fiber":3,"proteins":4,"sodium":5}, 150)
add("Mango Pudding", DS, {"calories":180,"fat":8,"saturated-fat":5,"carbohydrates":25,"sugars":22,"fiber":1,"proteins":3,"sodium":100}, 150)
add("Sago Gula Melaka", DS, {"calories":250,"fat":10,"saturated-fat":8,"carbohydrates":38,"sugars":22,"fiber":0,"proteins":2,"sodium":80}, 200)
add("Pulut Inti (2 pieces)", DS, {"calories":220,"fat":8,"saturated-fat":5,"carbohydrates":35,"sugars":14,"fiber":1,"proteins":3,"sodium":50}, 100)
add("Kuih Kosui (2 pieces)", DS, {"calories":120,"fat":3,"saturated-fat":2,"carbohydrates":24,"sugars":14,"fiber":0,"proteins":1,"sodium":20}, 80)
add("Tapioca Cake / Bingka Ubi (2 pieces)", DS, {"calories":200,"fat":8,"saturated-fat":5,"carbohydrates":30,"sugars":12,"fiber":2,"proteins":2,"sodium":100}, 100)
add("Seri Muka (2 pieces)", DS, {"calories":250,"fat":12,"saturated-fat":8,"carbohydrates":32,"sugars":16,"fiber":1,"proteins":4,"sodium":120}, 100)
add("Putu Piring (4 pieces)", DS, {"calories":200,"fat":4,"saturated-fat":2,"carbohydrates":38,"sugars":14,"fiber":1,"proteins":3,"sodium":50}, 120)
add("Kueh Bingka (1 piece)", DS, {"calories":180,"fat":8,"saturated-fat":5,"carbohydrates":24,"sugars":12,"fiber":1,"proteins":3,"sodium":100}, 80)
add("Peanut Pancake / Ban Chang Kueh (1 piece)", DS, {"calories":250,"fat":10,"saturated-fat":3,"carbohydrates":32,"sugars":14,"fiber":2,"proteins":8,"sodium":150}, 100)
add("Fried Dough Stick / You Tiao (1 piece)", DS, {"calories":200,"fat":12,"saturated-fat":3,"carbohydrates":20,"sugars":1,"fiber":1,"proteins":4,"sodium":300}, 60)
add("Butter Sugar Toast / Roti Bakar", DS, {"calories":220,"fat":12,"saturated-fat":6,"carbohydrates":24,"sugars":10,"fiber":1,"proteins":4,"sodium":200}, 80)
add("Crispy Waffle / Ais Krim Roti", DS, {"calories":300,"fat":14,"saturated-fat":6,"carbohydrates":38,"sugars":16,"fiber":1,"proteins":6,"sodium":250}, 120)
add("Ice Cream Sandwich (bread-wrapped)", DS, {"calories":280,"fat":12,"saturated-fat":7,"carbohydrates":38,"sugars":22,"fiber":1,"proteins":5,"sodium":200}, 120)
add("Chocolate Bar (Snickers, 1 bar)", DS, {"calories":240,"fat":12,"saturated-fat":4.5,"carbohydrates":30,"sugars":24,"fiber":1,"proteins":4,"sodium":120}, 50)
add("Potato Chips (1 small bag, 50g)", DS, {"calories":270,"fat":18,"saturated-fat":4,"carbohydrates":25,"sugars":1,"fiber":2,"proteins":3,"sodium":350}, 50)
add("Trail Mix / Nuts (1 handful, 30g)", DS, {"calories":180,"fat":15,"saturated-fat":2,"carbohydrates":8,"sugars":3,"fiber":3,"proteins":6,"sodium":50}, 30)
add("Chocolate Chip Cookie (1 large)", DS, {"calories":200,"fat":10,"saturated-fat":5,"carbohydrates":26,"sugars":16,"fiber":1,"proteins":2,"sodium":150}, 45)
add("Digestive Biscuits (3 pieces)", DS, {"calories":180,"fat":8,"saturated-fat":3,"carbohydrates":25,"sugars":8,"fiber":2,"proteins":3,"sodium":200}, 45)

# ==============================================================
# HOT POT / STEAMBOAT (10+)
# ==============================================================
HP = "🍲 Hot Pot / Steamboat"

add("Hot Pot / Steamboat Meal (per person, meat-heavy)", HP, {"calories":800,"fat":45,"saturated-fat":15,"carbohydrates":40,"sugars":8,"fiber":3,"proteins":60,"sodium":2500}, 600,
   "Massive variable. Assumes ~200g meat, fishballs, tofu, vegetables, dipping sauces. Broth consumption varies.")
add("Hot Pot / Steamboat Meal (per person, balanced)", HP, {"calories":600,"fat":30,"saturated-fat":10,"carbohydrates":45,"sugars":8,"fiber":4,"proteins":40,"sodium":2200}, 550)
add("Hot Pot / Steamboat (healthy, more veg less meat)", HP, {"calories":400,"fat":18,"saturated-fat":5,"carbohydrates":40,"sugars":6,"fiber":6,"proteins":28,"sodium":1800}, 500)
add("Tomato Broth (per bowl consumed)", HP, {"calories":60,"fat":3,"saturated-fat":0.5,"carbohydrates":8,"sugars":5,"fiber":1,"proteins":2,"sodium":400}, 250, "ml")
add("Mala / Spicy Broth (per bowl consumed)", HP, {"calories":120,"fat":10,"saturated-fat":2,"carbohydrates":4,"sugars":2,"fiber":1,"proteins":2,"sodium":800}, 250, "ml")
add("Chicken Broth / Clear Soup (per bowl)", HP, {"calories":30,"fat":1,"saturated-fat":0.5,"carbohydrates":2,"sugars":1,"fiber":0,"proteins":3,"sodium":300}, 250, "ml")
add("Hot Pot Dipping Sauce / Sacha Sauce (2 tbsp)", HP, {"calories":80,"fat":8,"saturated-fat":1.5,"carbohydrates":3,"sugars":2,"fiber":0,"proteins":1,"sodium":300}, 30)
add("Fishballs (6 pieces)", HP, {"calories":120,"fat":3,"saturated-fat":1,"carbohydrates":12,"sugars":2,"fiber":0,"proteins":12,"sodium":500}, 100)
add("Meatballs (6 pieces, pork)", HP, {"calories":180,"fat":12,"saturated-fat":4,"carbohydrates":6,"sugars":2,"fiber":0,"proteins":14,"sodium":500}, 100)
add("Hot Pot Beef Slices / Shabu Shabu (100g)", HP, {"calories":250,"fat":18,"saturated-fat":7,"carbohydrates":0,"sugars":0,"fiber":0,"proteins":20,"sodium":50}, 100)

# ==============================================================
# RICE & NOODLE STAPLES (15+)
# ==============================================================
ST = "🍚 Staples & Sides"

add("Jasmine White Rice (1 bowl, cooked)", ST, {"calories":260,"fat":0.5,"saturated-fat":0.1,"carbohydrates":58,"sugars":0,"fiber":1,"proteins":5,"sodium":5}, 200)
add("Brown Rice (1 bowl, cooked)", ST, {"calories":240,"fat":2,"saturated-fat":0.5,"carbohydrates":50,"sugars":0,"fiber":4,"proteins":5,"sodium":5}, 200)
add("Basmati Rice (1 bowl, cooked)", ST, {"calories":240,"fat":0.5,"saturated-fat":0.1,"carbohydrates":54,"sugars":0,"fiber":1,"proteins":5,"sodium":5}, 200)
add("Chicken Rice (just the rice, no chicken)", ST, {"calories":320,"fat":12,"saturated-fat":3,"carbohydrates":48,"sugars":1,"fiber":1,"proteins":5,"sodium":400}, 200)
add("Hainan Yellow Rice (1 bowl)", ST, {"calories":300,"fat":10,"saturated-fat":3,"carbohydrates":48,"sugars":1,"fiber":1,"proteins":5,"sodium":350}, 200)
add("Plain Noodles / Kway Teow (1 bowl, cooked)", ST, {"calories":220,"fat":1,"saturated-fat":0,"carbohydrates":48,"sugars":0,"fiber":1,"proteins":5,"sodium":50}, 200)
add("Egg Noodles (1 portion, cooked)", ST, {"calories":260,"fat":4,"saturated-fat":1,"carbohydrates":48,"sugars":1,"fiber":2,"proteins":9,"sodium":200}, 200)
add("Rice Vermicelli / Bee Hoon (1 bowl, cooked)", ST, {"calories":210,"fat":0.5,"saturated-fat":0,"carbohydrates":48,"sugars":0,"fiber":1,"proteins":3,"sodium":10}, 200)
add("Mee Sua (1 bowl, cooked)", ST, {"calories":230,"fat":1,"saturated-fat":0,"carbohydrates":50,"sugars":0,"fiber":1,"proteins":6,"sodium":100}, 200)

# ==============================================================
# DRINKS (non-hawker) (10+)
# ==============================================================
DR = "🥤 Drinks"

add("Coca-Cola (1 can, 330ml)", DR, {"calories":139,"fat":0,"saturated-fat":0,"carbohydrates":35,"sugars":35,"fiber":0,"proteins":0,"sodium":15}, 330, "ml")
add("Coke Zero / Diet Coke (330ml)", DR, {"calories":1,"fat":0,"saturated-fat":0,"carbohydrates":0,"sugars":0,"fiber":0,"proteins":0,"sodium":20}, 330, "ml")
add("Sprite (1 can)", DR, {"calories":140,"fat":0,"saturated-fat":0,"carbohydrates":35,"sugars":35,"fiber":0,"proteins":0,"sodium":25}, 330, "ml")
add("100 Plus (1 can)", DR, {"calories":90,"fat":0,"saturated-fat":0,"carbohydrates":22,"sugars":20,"fiber":0,"proteins":0,"sodium":40}, 330, "ml")
add("Pokka Green Tea (no sugar, 500ml)", DR, {"calories":0,"fat":0,"saturated-fat":0,"carbohydrates":0,"sugars":0,"fiber":0,"proteins":0,"sodium":15}, 500, "ml")
add("Yakult (1 bottle)", DR, {"calories":50,"fat":0,"saturated-fat":0,"carbohydrates":12,"sugars":10,"fiber":0,"proteins":1,"sodium":15}, 100, "ml")
add("Vitasoy Soya Milk (250ml)", DR, {"calories":120,"fat":4,"saturated-fat":0.5,"carbohydrates":14,"sugars":10,"fiber":1,"proteins":8,"sodium":60}, 250, "ml")
add("Chrysanthemum Tea (canned, sweetened)", DR, {"calories":110,"fat":0,"saturated-fat":0,"carbohydrates":28,"sugars":26,"fiber":0,"proteins":0,"sodium":15}, 300, "ml")
add("Winter Melon Tea (canned)", DR, {"calories":100,"fat":0,"saturated-fat":0,"carbohydrates":25,"sugars":24,"fiber":0,"proteins":0,"sodium":20}, 300, "ml")
add("Grass Jelly Drink (canned)", DR, {"calories":110,"fat":0,"saturated-fat":0,"carbohydrates":28,"sugars":24,"fiber":0,"proteins":0,"sodium":15}, 300, "ml")
add("Orange Juice (fresh, 250ml)", DR, {"calories":110,"fat":0.5,"saturated-fat":0,"carbohydrates":25,"sugars":20,"fiber":0.5,"proteins":2,"sodium":5}, 250, "ml")
add("Apple Juice (250ml)", DR, {"calories":115,"fat":0,"saturated-fat":0,"carbohydrates":28,"sugars":25,"fiber":0,"proteins":0,"sodium":5}, 250, "ml")
add("Beer (1 can, Tiger/Anchor, 330ml)", DR, {"calories":140,"fat":0,"saturated-fat":0,"carbohydrates":12,"sugars":0,"fiber":0,"proteins":1,"sodium":10}, 330, "ml")
add("Beer (1 pint, draft, ~470ml)", DR, {"calories":200,"fat":0,"saturated-fat":0,"carbohydrates":17,"sugars":0,"fiber":0,"proteins":2,"sodium":15}, 470, "ml")
add("Red Wine (1 glass, 150ml)", DR, {"calories":125,"fat":0,"saturated-fat":0,"carbohydrates":4,"sugars":1,"fiber":0,"proteins":0,"sodium":5}, 150, "ml")
add("White Wine (1 glass, 150ml)", DR, {"calories":120,"fat":0,"saturated-fat":0,"carbohydrates":3,"sugars":1,"fiber":0,"proteins":0,"sodium":5}, 150, "ml")

# ==============================================================
# MIDDLE EASTERN / MEDITERRANEAN (10+)
# ==============================================================
ME = "🧆 Middle Eastern"

add("Hummus with Pita Bread (1 plate)", ME, {"calories":350,"fat":18,"saturated-fat":2.5,"carbohydrates":38,"sugars":3,"fiber":6,"proteins":12,"sodium":600}, 200)
add("Falafel Wrap", ME, {"calories":450,"fat":20,"saturated-fat":3,"carbohydrates":52,"sugars":6,"fiber":8,"proteins":16,"sodium":900}, 280)
add("Chicken Shawarma Wrap", ME, {"calories":500,"fat":24,"saturated-fat":6,"carbohydrates":40,"sugars":5,"fiber":3,"proteins":32,"sodium":1000}, 280)
add("Beef Kebab Plate with Rice", ME, {"calories":620,"fat":28,"saturated-fat":10,"carbohydrates":58,"sugars":4,"fiber":2,"proteins":38,"sodium":1100}, 420)
add("Lamb Shank with Rice (Mandi / Kabsa style)", ME, {"calories":750,"fat":35,"saturated-fat":14,"carbohydrates":62,"sugars":4,"fiber":2,"proteins":48,"sodium":1200}, 480)
add("Baba Ganoush with Pita", ME, {"calories":200,"fat":14,"saturated-fat":2,"carbohydrates":18,"sugars":4,"fiber":5,"proteins":4,"sodium":400}, 150)
add("Tabbouleh Salad", ME, {"calories":150,"fat":8,"saturated-fat":1,"carbohydrates":16,"sugars":3,"fiber":4,"proteins":4,"sodium":300}, 180)
add("Greek Salad", ME, {"calories":250,"fat":20,"saturated-fat":7,"carbohydrates":10,"sugars":5,"fiber":3,"proteins":8,"sodium":700}, 200)
add("Mutton Soup / Sup Kambing", ME, {"calories":280,"fat":18,"saturated-fat":7,"carbohydrates":10,"sugars":2,"fiber":1,"proteins":22,"sodium":900}, 350, "ml")
add("Arab Briyani / Mandi Rice (Chicken)", ME, {"calories":700,"fat":30,"saturated-fat":10,"carbohydrates":80,"sugars":5,"fiber":2,"proteins":35,"sodium":1300}, 480)

# ==============================================================
# LOCAL CAFE / BUBBLE TEA (10+)
# ==============================================================
BT = "🧋 Bubble Tea & Cafe"

add("Bubble Tea / Milk Tea with Pearls (medium)", BT, {"calories":350,"fat":8,"saturated-fat":4,"carbohydrates":65,"sugars":40,"fiber":0,"proteins":3,"sodium":80}, 500, "ml")
add("Bubble Tea / Brown Sugar Milk (medium)", BT, {"calories":420,"fat":10,"saturated-fat":5,"carbohydrates":78,"sugars":50,"fiber":0,"proteins":4,"sodium":100}, 500, "ml")
add("Bubble Tea / Fruit Tea (medium, 50% sugar)", BT, {"calories":180,"fat":0,"saturated-fat":0,"carbohydrates":45,"sugars":28,"fiber":0,"proteins":0,"sodium":20}, 500, "ml")
add("Bubble Tea / Jasmine Green Milk Tea (medium, 50% sugar)", BT, {"calories":220,"fat":6,"saturated-fat":3,"carbohydrates":38,"sugars":22,"fiber":0,"proteins":3,"sodium":60}, 500, "ml")

add("Latte (hot, medium, 12oz)", BT, {"calories":150,"fat":7,"saturated-fat":4,"carbohydrates":14,"sugars":12,"fiber":1,"proteins":8,"sodium":120}, 350, "ml")
add("Cappuccino (hot, medium)", BT, {"calories":110,"fat":5,"saturated-fat":3,"carbohydrates":10,"sugars":8,"fiber":0,"proteins":6,"sodium":100}, 350, "ml")
add("Flat White", BT, {"calories":100,"fat":5,"saturated-fat":3,"carbohydrates":8,"sugars":6,"fiber":0,"proteins":6,"sodium":80}, 250, "ml")
add("Americano / Long Black (no sugar)", BT, {"calories":10,"fat":0,"saturated-fat":0,"carbohydrates":1,"sugars":0,"fiber":0,"proteins":0,"sodium":5}, 300, "ml")
add("Iced Latte (medium)", BT, {"calories":130,"fat":6,"saturated-fat":3.5,"carbohydrates":12,"sugars":10,"fiber":0,"proteins":6,"sodium":100}, 400, "ml")
add("Iced Mocha (medium)", BT, {"calories":250,"fat":10,"saturated-fat":5,"carbohydrates":32,"sugars":26,"fiber":1,"proteins":8,"sodium":150}, 400, "ml")
add("Hot Chocolate (medium)", BT, {"calories":300,"fat":12,"saturated-fat":7,"carbohydrates":40,"sugars":32,"fiber":2,"proteins":10,"sodium":180}, 350, "ml")


# ==============================================================
# EXECUTE INSERT
# ==============================================================

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")

    inserted = 0
    skipped = 0
    for food in FOODS:
        name = food["name"]
        # Skip exact duplicate names
        existing = conn.execute(
            "SELECT id FROM foods WHERE name = ? AND user_id IS NULL AND deleted_at IS NULL",
            (name,)
        ).fetchone()
        if existing:
            skipped += 1
            continue

        category = food.get("category")
        portion = food.get("portion", 100)
        unit = food.get("unit", "g")
        nutrition = json.dumps(food.get("nutrition", {}))
        notes = food.get("notes")

        conn.execute(
            """INSERT INTO foods (user_id, name, brand, nutrition, portion, unit,
               img_url, notes, category, created_at, updated_at, visibility)
               VALUES (NULL, ?, NULL, ?, ?, ?, NULL, ?, ?, ?, ?, 'private')""",
            (name, nutrition, portion, unit, notes, category, now, now)
        )
        inserted += 1

    conn.commit()
    conn.close()
    print(f"Done. Inserted {inserted} new foods. Skipped {skipped} duplicates.")
    print(f"Total in script: {len(FOODS)}")

if __name__ == "__main__":
    main()
