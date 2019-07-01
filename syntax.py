#this is how you print
print("This is a good String")
print('You can use single quotes or double quotes for a string')
print("Hello " + "Asher")

# convention in python is to name variuables with an underscore between words '_'
todays_date = "October 29, 2018"

# multiplication with variables
num1= 27
num2= 2
product = num1*num2
remainder = 1398%11

# updating variables
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

annual_rainfall += september_rainfall + october_rainfall+ november_rainfall+ december_rainfall

cucumbers = 2
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber

# below shows changing into float type
cucumbers= 100
num_people = 6
whole_cucumbers_per_person= cucumbers/num_people
print(whole_cucumbers_per_person)
float_cucumbers_per_person = float(cucumbers) /num_people
print(float_cucumbers_per_person)

# tip calculator
meal = 44.50
tax = 6.75/100
tip = 15.0/100

meal = meal + meal*tax
total = meal + meal * tip
print(total)