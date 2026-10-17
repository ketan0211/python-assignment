#1 Take the string 'Flipkart-Sale2024' and use string methods to convert it to 
# lowercase, replace the dash with a space, and print the result.

string ="Flipkart-Sale2024"
string=string.lower()
string=string.replace("-"," ")
print(string)


#2.Given the product name ' OnePlus Nord-CE 3 ', write code to clean it by removing extra spaces, 
# converting all letters to uppercase, and replacing the dash with a colon

name=' OnePlus Nord-CE 3 '
name= name.strip()
name= name.upper()
name= name.replace("-", ":")
print(name)



#3#Write a function split_product_code(product_code) that takes a string like 'ZOMATO-FOOD-2024'
# and returns a list of its parts using the split() method.

def spilit_product_code(product_code):
     return product_code.split("-")
 
print(spilit_product_code('ZOMATO-FOOD-2024'))


#4 Given the string 'Spotify_Premium_Offer', use string slicing to extract and print only the word 'Premium'.

name = 'Spotify_Premium_Offer'
print(name[8:15])



#5 Format and print a message using variables: product = 'Myntra Shirt', price = 799.5. The output should be: 'Deal:
# Myntra Shirt is available at ₹799.50 only!' using string formatting.

product = 'Myntra Shirt'
price = 799.50
print("'Deal:",product  ,"is available at ₹",price,"only!'")