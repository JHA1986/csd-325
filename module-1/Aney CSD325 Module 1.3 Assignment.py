#Jonah Aney CSD325 Module 1.3 Assignment

#Task:Ask the user how many bottles of beer are on the wall.
#Pass that input to a function that manages the countdown.
#The function should take the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.
#Once the count is down to 1, change lyrics to show "1 bottle of beer..."
#At the end of the countdown, get back to the main program and remind the user to buy more beer.

#resources: 
#R/learnpython on reddit: Super beginner question for 99 bottles of beer exercise. (n.d.). 
#https://www.reddit.com/r/learnpython/comments/cb59on/super_beginner_question_for_99_bottles_of_beer/ 

#Python projects: Print the song 99 bottles of beer on the wall. w3resource. (n.d.). 
#https://www.w3resource.com/projects/python/python-projects-4.php#google_vignette 

#Ask the user how many bottles of beer are on the wall.
bottles = int(input("How many bottles of beer are on the wall? "))
#Pass that input to a function that manages the countdown.
def countdown(bottles):
    while bottles > 0:
        if bottles == 1:
#If and once the count is only 1, change lyrics to show 'bottle' instead of 'bottles' of beer"
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take one down, pass it around, no more bottles of beer on the wall.")
#If the count is more than 1, display the count and subtract 1 to show number of remaining bottles of beer on the wall.
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.")
#Subtract 1 from the value of bottles variable.
        bottles -= 1
#Call the function to manage the countdown.
countdown(bottles)
#At the end of the countdown, display the message to the user to buy more beer.
print("Time to buy more beer!")


