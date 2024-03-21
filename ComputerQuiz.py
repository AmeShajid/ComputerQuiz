#computer quiz



#print out welcome to our quiz
print("Welcome to my computer quiz")
#asking them if they want to play our quiz
playing = input("Do you want to play \n")

#if people do not input yes then we will quit the program
if playing.lower() != "yes":#we added .lower because in case they input anything with an upper case it will always = yes
    quit()
#if they input yes then we wil continue on
print("Okay! Let's play")
score = 0 # here is the starting score for the program
#now we will ask them a question and take an answer
answer = input("What does CPU stand for? ")
#now we will check if they anwer is right and tell them
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1 # everytime they get the answer right we will add +1 to their score
else:#else in case they get it wrong we will say they got it wrong
    print("Incorrect")

# now we are asking more questions from here on out. same thing as what is above
   
   
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect") 
# next question
answer = input("What does RAm stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
#next question
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct") # now here is the output of their final score. 
#we had to use str because score is an integer and we have to make it a string to text 

print("You got " + str((score / 4) * 100)+ "%") # this is their final score output
#we are doing divide by 4 because we have 4 questions then *100 to get that that whole number answer its simple math bru






