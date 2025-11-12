# Detta är den första kommentaren
# Kommentarer påverkar inte hur koden körs

"""
Detta är en flerradig kommentar.
Flerradiga kommentarer kan skrivas över flera rader.
"""

# ===== MATH ===== 
print(2 + 3) # Addition            
print(3 - 1) # Subtraktion            
print(2 * 3) # Multiplikation
print(3 / 2) # Division             
print(3 ** 2) # Exponentiering           
print(3 % 2) # Modulus             
print(3 // 2) # Golvdivision        

# ===== NUMBERS ===== 
# Integers (Int for short) är heltal (utan decimaler)
a, b, c = -5, 0, 8 # variabler som lagrar heltal
print("Integers:", a, b, c) # Utskrift av heltal

# Floats är tal med decimaler
x, y, z = -2.5, 0.0, 4.75 # variabler som lagrar flyttal
print("Floats:", x, y, z) # Utskrift av flyttal

# Complex numbers har en reell och en imaginär del
comp1 = 1 + 2j # variabel som lagrar ett komplext tal
comp2 = 3 + 5j
print("Complex Numbers:", comp1, comp2) 
print("Real part of comp1:", comp1.real)
print("Imaginary part of comp1:", comp1.imag)

# ===== STRINGS =====
# Strings är text som skrivs inom enkla eller dubbla citattecken
first_name = 'Asabeneh' # variabel som lagrar en sträng
country = 'Finland'
language = 'Python'
sentence = 'I enjoy teaching Python'
long_sentence = 'Learning Python step by step makes programming more fun and easier to understand'

print("Test") # Utskrift av en sträng
print(first_name) # Utskrift av variabeln first_name
print(country)
print(language)
print(sentence)
print(long_sentence)
print("String concatenation:", first_name + " teaches " + language) # Utskrift med strängkonkatenering (sträng + variabelsträng + sträng + variabelsträng)
print("Length of long sentence:", len(long_sentence))

# ===== BOOLEANS =====
# Booleanvärden representerar sant (True) eller falskt (False)
is_light_on = True # Variabel som lagrar ett booleanvärde (sant)
is_raining = False
print("Is the light on?", is_light_on) # Utskrift av booleanvariabeln
print("Is it raining?", is_raining)
print("Boolean example:", 10 > 5, 3 == 4) # Utskrift av booleanuttryck (sant eller falskt)

# ===== LISTS =====
# Lists är ordnade samlingar som kan innehålla olika datatyper
numbers = [1, 2, 3, 4, 5] # Lista med heltal
fruits = ['Banana', 'Apple', 'Mango', 'Avocado'] # Lista med strängar
countries = ['Finland', 'Sweden', 'Norway', 'Denmark'] # Lista med länder
mixed_list = ['Banana', 42, True, 3.14] # Lista med olika datatyper

print("Numbers:", numbers) # Utskrift av listan numbers
print("Fruits:", fruits)
print("Countries:", countries)
print("Mixed List:", mixed_list)
print("First fruit:", fruits[0]) # Åtkomst till första elementet som skrivs som: [0] i listan fruits
print("Last country:", countries[-1])
print("Length of numbers list:", len(numbers)) # Utskrift av längden på listan numbers

# ===== TUPLES =====
# Tuples är ordnade samlingar som inte kan ändras (oföränderliga)
names = ('Asabeneh', 'Brook', 'Lidiya', 'John', 'Maria') # Tuple med strängar
planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')

print("Names:", names) # Utskrift av tuplen names
print("Planets:", planets)
print("First name:", names[0]) # Åtkomst till första elementet i tuplen names
print("Number of planets:", len(planets)) # Utskrift av längden på tuplen planets

# ===== SETS =====
# Sets är oordnade samlingar med unika värden (inga dubbletter)
numbers_set = {1, 2, 3, 4, 5} # Set med heltal
constants = {3.14, 9.81, 2.71} # Set med float-värden

print("Numbers Set:", numbers_set) # Utskrift av setet numbers_set
print("Constants Set:", constants) # Utskrift av setet constants
print("Union of sets:", numbers_set | constants) # Union av sets (alla unika värden från båda seten)
print("Intersection (empty expected):", numbers_set & constants) # Snitt av sets (gemensamma värden, förväntas vara tomt)

# ===== DICTIONARIES =====
# Dictionaries lagrar data som nyckel–värde-par
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'country': 'Finland',
    'age': 35,
    'is_married': True,
    'skills': ['Python', 'JavaScript', 'React']
}

print("Person Dictionary:", person) # Utskrift av hela ordboken person
print("First name:", person['first_name']) # Åtkomst till värdet med nyckeln 'first_name'
print("Skills:", person['skills']) # Åtkomst till värdet med nyckeln 'skills'
print("Number of skills:", len(person['skills'])) # Utskrift av längden på listan som är värdet för nyckeln 'skills'