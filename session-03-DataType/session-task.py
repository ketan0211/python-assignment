#task 1  Declare four variables in Python: your age as an int, your height in centimeters as a float, 
# your name as a str, and whether you have a Spotify account as a bool. Print each variable and use the 
# type() function to display its data type.
student_age = 20
student_height = 5.9
student_name ="jethalal"
has_spotify_account = True


print("Student Age", student_age, "Type",type(student_age))
print("Student_Height", student_height, "type" ,type(student_height))
print("Student_Name",student_name , "type" ,type(student_name))
print("Has_spotify_Account", has_spotify_account, "type", type(has_spotify_account))


#task 2: Function to calculate the total cart amount
def total_cart_amount(prices):
    total = 0
    
    for price in prices:
        total= total+ float(price)
    return total
prices = ['199.99', '49', '350.75']
print("Total Cart Amount:", total_cart_amount(prices))



#task 3:  ask user to input their cricket score as a string, converts it to an int, and prints 'Half-century!'
# if the score is 50 or more, otherwise prints 'Keep going!'
score= input(str("Enter Your Score:"))
converted_score = int(score)
if converted_score>=50:
    print("Half-century!")
else:
    print("keep going")
    


#task4: Convert String to Boolean
var_is_premium="true"
var_is_premium=(var_is_premium=="true")
print(var_is_premium)
print(type(var_is_premium))