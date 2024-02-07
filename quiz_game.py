#Python mini project

print("Welcome to my computer quiz! ")

playing = input("Do you want to play? ")
correct = 0

if playing.lower() != "yes" :
    quit()

print("Okay! Let's play :) ")

answer = input("Q1. what does url stands for?\n ")
if answer.lower() == "uniform resource locator":
    correct =correct+1
    print("correct!")
else:
    print("incorrect! ")

answer = input("Q2. what does WWW stands for?\n ")
if answer.lower() == "world wide web":
    correct =correct+1
    print("correct!")
else:
    print("incorrect! ")

answer = input("Q3. what does HTML stands for ?\n ")
if answer.lower() == "hyper text markup language":
    print("correct!")
    correct =correct+1
else:
    print("incorrect! ")

answer = input("Q4. what does UPS stands for ?\n ")
if answer.lower() == "uninterruptible power supply":
    print("correct!")
    correct = correct+1
else:
    print("incorrect! ")

answer = input("Q5. what does RAM stands for ?\n ")
if answer.lower() == "random access memory":
    print("correct!")
    correct = correct+1
else:
    print("incorrect! ")

answer = input("Q6. what does GUI stands for ?\n ")
if answer.lower() == "graphical user interface":
    print("correct!")
    correct = correct+1
else:
    print("incorrect! ")

answer = input("Q7. what does LAN stands for ?\n ")
if answer == "local area network":
    print("correct!")
    correct = correct+1
else:
    print("incorrect! ")

answer = input("Q8. what is 18+2(2+3) equals ?\n ")
if answer.lower() == "28":
    print("correct!")
    correct = correct+1
else:
    print("incorrect! ")

answer = input("Q9. who is the artist in the making of historical painting ' MONA LISA '? \n ")
if answer.lower() == "leonardo da vinci":
    print("correct!")
    correct = correct+1
else:  
    print("incorrect! ")

answer = input("Q10. what is the longest river in the world ?\n ")
if answer.lower() == "nile" :
    print("correct!")
    correct = correct+1
else:
    print("incorrect! ")
print("Well done!!",correct,"answers are correct!")
print("you got",(correct/10)* 100 ,"%")

if correct == 10:
    print("Congratulations!! You got a perfect score!!")

if correct == 0:
    print("You did very poor :x!!") 