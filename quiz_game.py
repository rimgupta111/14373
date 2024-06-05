print ("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print ("correct!")
    score += 1
else:
    print ("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print ("correct!")
    score += 1
else:
    print ("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print ("correct!")
    score += 1
else:
    print ("Incorrect!")

answer = input("What does PSU stand for? ")
if answer == "Power supply":
    print ("correct!")
    score += 1
else:
    print ("Incorrect!")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/4)* 100) + "%.")