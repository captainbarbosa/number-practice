##########################################################################################
# CSC 280 Programming Practice #3                                                        #  
# modifier: Nadia Barbosa                                                                #
# filename: Nadia_assignment3.py                                                         #                                                        #
# date last modified: 2/21/14                                                            #
# ---------------------------------------------------------------------------------------#
# EXAMPLE 1: score_calculatior.py                                                        #
#                                                                                        #
# action: Uses input scores from user to calculate minimum, maximum, and average.        #
#                                                                                        #
# input: Number of scores to be entered and score values                                 #
#                                                                                        #
# output:   Min, max, and average of user's numbers                                      #
#----------------------------------------------------------------------------------------#
# EXAMPLE 2: number_organizer.py                                                         #
#                                                                                        #
# action: Takes entered floating point numbers and finds the largest and smallest values #
#                                                                                        #
# input: three floating point numbers                                                    #
#                                                                                        #
# output: prints largest and smallest values of the three floating point inputs          #
#----------------------------------------------------------------------------------------#
# EXAMPLE 3: increasing_looper.py                                                        # 
#                                                                                        #
# actions: takes numerical input and finds avg and sum when a smaller number is entered  # 
#                                                                                        #
# input: numerical input                                                                 #
#                                                                                        # 
# output: average and sum of all numbers, not including last smallest number             #
##########################################################################################
#-----------------------------------------------------------------------------------------

#DIALOG BOX
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
How many scores need to be calculated? 7
Please enter your scores:
Enter score: 89
Enter score: 78
Enter score: 90
Enter score: 76
Enter score: 70
Enter score: 88
Enter score: 79
The average score is 81
The minimum score is 70
The meximum score is 90
Please enter your first number:43.5
Please enter your second number: 110.2
Please enter your third number: 35
110.2 is the largest number
35.0 is the smallest number
Enter a number: 30
Enter a number: 32
Enter a number: 45
Enter a number: 47
Enter a number: 74
Enter a number: -1
Enter a number: 45
The sum of your numbers is 228"""

#CODE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#PART 1

#sets beginning variables to set up loop
loopCount=1
scoreCount=0
scoreTotal=0
scoreMax=0
scoreMin=100
#prompts for user input to tell loop how many times to repeat
numberOfscores=int((raw_input("How many scores need to be calculated?")))
#prompts for user to begin entering scores
print("Please enter your scores:")

#loop setup
while loopCount <= numberOfscores:
    #to show "Enter score "X": to so user knows which score number to enter
    score=int(raw_input("Enter score "+str(loopCount)+" :"))
    #prompts user not to enter negative numbers if do so
    if score<0:
        print("Please enter only positive numbers")
    #continuing loop instructions if positive scores are entered
    else:
        scoreTotal = scoreTotal + score 
        scoreCount=scoreCount+1
        loopCount=loopCount+1
        #reporting max and min scores
        if score>scoreMax:
            scoreMax=score
        if score<scoreMin:
            scoreMin=score
#final avg calculation and printout
averageScore=(scoreTotal/scoreCount)
print "The average score is " +str(averageScore)+""
print "The minimum score is " +str(scoreMin)+""
print "The maximum score is " +str(scoreMax)+""

# PART 2 

#defines variables as flating numbers so decimals can be included in loop
f=float(raw_input("Please enter your first number: "))
s=float(raw_input("Please enter your second number: "))
t=float(raw_input("Please enter your third number: "))

#flow chart setup and printout in form of "if/else" statements and printing of number hiearchy
if f>s:
    if f>t:
        print(""+str(f)+" is the largest number")
        if s>t:
            print(""+str(t)+" is the smallest number")
        else:
            print(""+str(s)+" is the smallest number")
    else: #or if f<t
        print(""+str(t)+" is the largest number")
        print(""+str(s)+" is the smallest number")
else: # or if s>f
    if s>t: 
        print(""+str(s)+" is the largest number")
        if f>t: 
            print(""+str(t)+" is the smallest number")
        else:
            print(""+str(f)+" is the smallest number")
    else:
        print(""+str(t)+" is the largest number")
        print(""+str(f)+" is the smallest number")

# PART 3

#defines beginning variables to set up sentinel loop
currentNum=0
counter=0
sumVar=0
#prompt to enter first number
newNum=int(raw_input("Enter a number: "))
#sentinel loop form
while newNum>currentNum:
    currentNum=newNum
    sumVar=sumVar+currentNum
    counter=counter+1
    #prompting to enter subsequent inputs
    newNum=int(raw_input("Enter a number: "))

#instructions after sentinel loop ends: calculating average and sum of numbers
avg=sumVar/counter
print("The average is "+str(avg)+ "")
print("The sum of your numbers is "+str(sumVar)+"")

