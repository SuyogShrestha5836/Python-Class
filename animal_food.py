'''a="Herbivorous"
b="Carnivorous"
# c="Omnivorous"
if a=="Herbivorous":
    print(f'This animal eats vegetables only {a}')
elif b=="Carnivorous":
    print(f'This animal eats meat only {b}')
else:
    print("This animal eats both vegetables and meat")'''

type = input("Enter the type of animal : ").lower()
if type == 'omnivorous' :
    print('Omnivorous eat both meat and vegetables')
elif type == 'carnivorous':
    print('Carnivorous eat meat only')
elif type == 'herbivorous':
    print('Herbivorous eat only vegetables')
else :
    print("There was an error")