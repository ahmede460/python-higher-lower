from higherlowerart import logo,vs
from higherlowerdata import data
import random
print(logo)
score = 0
endofgame = False


def randomperson():
    return random.choice(data)

def who_is_higher(firstperson,secondperson,score):
    global endofgame
    global person_a
    print(f"Compare A: {firstperson['name']}, a {firstperson['description']}, from {firstperson['country']} ")
    print(vs)    
    print(f"Against B: {secondperson['name']}, a {secondperson['description']}, from {secondperson['country']} ")
    guess = input("\n Who has more follower? Type 'A' or 'B' : ").lower()
    if guess == "a":
        if firstperson["follower_count"] > secondperson["follower_count"]:
            print(f"\n Correct! :) {firstperson['name']} has {firstperson['follower_count']} milion and {secondperson['name']} has {secondperson['follower_count']} milion")
            return score + 1
        else: 
            print(f"\n you lost :(  {firstperson['name']} has {firstperson['follower_count']} milion and {secondperson['name']} has {secondperson['follower_count']} milion")
            endofgame = True
            return score
    elif guess == "b":
        if secondperson["follower_count"] > firstperson["follower_count"]:
            print(f"\n Correct! :) {firstperson['name']} has {firstperson['follower_count']} milion and {secondperson['name']} has {secondperson['follower_count']} milion")
            person_a = secondperson
            return score + 1
            
        else:
            print(f"\n you lost :(  {firstperson['name']} has {firstperson['follower_count']} milion and {secondperson['name']} has {secondperson['follower_count']} milion")
            endofgame = True
            return score

person_a = randomperson()
person_b = randomperson()

while endofgame == False:
    score = who_is_higher(person_a,person_b,score)
    print(f"\n Your score is {score} \n")
    person_b = randomperson()
    while person_b == person_a:
        person_b = randomperson()

