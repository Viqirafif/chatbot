import re
import random

sapaan=["Hai beb","Halo juga","Jalan yuk", "Apa Kabar","Oke santuy","kamu tau aku chatbot"]

while True:
    x=input("User\t: ")
    if re.findall(r'halo|hai|kamu siapa',x):
        print("Bot\t:", random.choice(sapaan))
    else:
        print("Bot\t: Aku tidak paham")