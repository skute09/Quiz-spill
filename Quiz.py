print("Velkommen til dette Quiz-spillet!")
# Spør om hva du heter, printer det ut og definerer et globalt variabel som heter "poeng"
navn = input("Hva heter du? ")
print("Så kjekt at du vil være med " + navn + "!")
poeng = 0

# Har tre if statements etter hverandre som hver sjekker et nytt input variabel om hva den returner
# sammenligner svaret til spilleren med svaret og sier i fra om du hadde rett eller galt
# legger til et tall i poeng variablet viss du har rett
# passer på at svaret ikke er case sensitiv ved å bruke .lower

svar1 = input("Første spørsmål: Hva er hovedstaden i Norge? ")
if svar1.lower() == "oslo":
    print("Det er riktig! Godt jobbet :)")
    poeng +=1
else:
    print("Beklager, men det er feil svar.")

svar2 = input("Hva heter Norges nest største by? ")
if svar2.lower() =="bergen":
    print("Det er riktig! Godt jobbet :)")
    poeng +=1
else:
    print("Beklager, men det er feil svar.")

svar3 = input("Hva heter det beste fotballaget i Bergen? ")
if svar3.lower() == "brann":
    print("Det er riktig! Godt jobbet :)")
    poeng +=1
else:
    print("Beklager, men det er feil svar.")

# Gratulerer deg og kaller deg navne du valgte i begynnelsen 
# Sier hvor mye poeng du fikk
# Gir deg en melding basert på hver mulige poeng sum

print(f"Gratulerer {navn}! Du fikk {poeng} poeng!")
if poeng == 3:
    print("Godt jobbet! Du fikk full pott :)")
elif poeng == 2:
    print("Nokså bra jobbet. Nesten alt riktig :)")
elif poeng == 1:
    print("Du fikk 1 poeng riktig. Neste gang klarer du nok mer :)")
elif poeng == 0:
    print("Du fikk ingen riktige, men du har forhåpetligvis lært litt :)")