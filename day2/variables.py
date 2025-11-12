# Day 2: 30 Days of python programming

first_name = "Emrik" 
last_name = "Rellmar"
full_name = "Emrik Rellmar"
country = "Sweden" 
city = "Ängelholm"
age = 19
year = 2025
is_married = False
is_true = True
is_light_on = False
first_name, middle_name, last_name = "Emrik", "Loke", "Rellmar"

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(is_light_on))

print(len(first_name))
first_name_length = len(first_name)
last_name_length = len(last_name)
difference = last_name_length - first_name_length
print("Det skiljer " + str(difference) + " bokstäver.")

num_one = 5
num_two = 4

diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two 
floor_division = num_one // num_two

area_of_circle = 3.14*(30**2)
circum_of_circle = 60*3.14
print("Arean av cirkeln " + str(area_of_circle))
print("Omkretsen av cirkeln " + str(circum_of_circle))

radius = input("Hur stor är din egna cirkels radie?:")
area_of_circle = 3.14*(radius**2)
print("Arean av din cirkel är då: " + int(area_of_circle))

