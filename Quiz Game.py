#Quiz Game
print("Welcome to my Computer Quiz")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score=0

answer = input("What Does CPU Stand for?")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What Does GPU Stand for?")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What Does RAM Stand for?")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What Does PSU Stand for?")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What Does ROM Stand for?")
if answer.lower() == "read only memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got" + " " +str(score)+ " "+ "Questions Correct")
print("You got" + " " +str((score/5) * 100) + "%")