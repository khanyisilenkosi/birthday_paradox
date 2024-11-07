import datetime, random

def getbirthdays(number_ofbirthdays):
    
    birthdays = []
    for i in range(number_ofbirthdays):
        start_ofbirthdays = datetime.date(2001, 1, 1)

        randomNumberofDays = datetime.timedelta(random.randint(0,364))
        birthday = start_ofbirthdays + randomNumberofDays 
        birthdays.append(birthday)


        return birthdays
    

def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None 
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdaysB in enumerate(birthdays[a + 1]):
            if birthdayA == birthdaysB:
                return birthdayA #return the matching birthday
            
print("Birthday Paradox,The birthday paradox shows us that in a group of N friends, the odds that two of them share the same birthday are suprisingly large.")
            
months = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")

while True: #Keep asking the user until they enter a valid amount
    print("How many birthdays shall i generate? , Max (100)")
    response = input('>' )

    if response.isdecimal() and (0 < int(response) <= 100):
        number_ofBirthdays = int(response)
        break #user has entered a valid amount
print()

#Generate and display the birthdays

print("Here are", number_ofBirthdays,"birthdays")
birthdays = getbirthdays(number_ofBirthdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ", end="") #display a comma for each birthday afer the first birthday

        month_name = months[birthday.month -1]
        dateText = '{} {}'.format(month_name, birthday.day)
        print(dateText, end="")

print()
print()

#Determine if there are two birthday matches

match = get_match(birthdays)

#Display the results

print('In this simulation', end='')
if match != None:
    month_name = months[match.month -1]
    dateText = '{} {}'.format(month_name, match.day)
    print("Multiple people have a birthday on", dateText)

else:
    print('There are no matching birthdays')
print()


#Run through 100,000 simulations

print("Generating", number_ofBirthdays, "random birthdays 100,000 times....")
input("Press enter to begin")

print('Let us run another 100,000 simulations.')

simMatch = 0 #How many simulations has matching birthdays in them
for i in range(100,000):
    #Reprot on the progress every 100,00 simulations
    if i % 100_000 == 0:
        print(i, 'simulation run....')
        birthdays = getbirthdays(number_ofBirthdays)
        if get_match(birthdays) != None:
            simMatch = simMatch +1
print('100,000 simulaions run')


#Simulation results

probalility = round(simMatch / 100_000 * 100, 2)
print("Out of 100,000 simulations of", number_ofBirthdays, 'people, there was a')
print("matching birthday in that group", simMatch, 'times. This means')
print("that", number_ofBirthdays, "people have a",probalility, f"% chance of")
print('having a matching birthday in their group')