# coding: utf-8

# Place for package imports if needed


#------------------------------------------------------------------
# Functions for commands 

# User guide function
def help():
    print("\nTervetuloa käyttöohjeisiin.")
    print("")
    print("Tervemenoa käyttöohjeista!\n")

# Chooce fiscal year function
def choose_year():
    accounting = {}
    while True:
        try:
            year = int(input("Valitse kirjanpidon tilikausi: "))
            if year <= 0:
                print("\nVuoden tulee olla positiivinen kokonaisluku\n")
            else:
                year_file = f"{year}.csv"
                with open(year_file) as file:
                    for row in file:
                        row = row.split(";")
                        accounting[row[0]] = [row[1],row[2],row[3],row[4]]
                return [year, accounting]
        except:
            print("\nSyöttämäsi arvo on virheellinen, käytä valinnassa numeroita.\n")

# insert data for your accounting
def insert_data(accounting: dict):
    date = str(input("Anna päivämäärä: "))
    account = str(input("Anna tili: "))
    while True:
        try:
            amount = float(input("Anna summa: "))
            break
        except ValueError:
            print("\nSyöttämäsi arvo on virheellinen, käytä valinnassa numeroita.\n")
    description = str(input("Anna selite: "))        
    accounting[len(accounting)] = [date, account, amount, description]
    return accounting

# Function to print data
def print_data(some_dict: dict):
    for key in some_dict:
        print(f"{key}: {some_dict[key][0]}, {some_dict[key][1]}, {some_dict[key][2]}, {some_dict[key][3]}")

# Program function
def program(year, accounting):
    print("\nOhjelma käynnistyi, valitse seuraavista toiminnallisuuksista:\n")
    while True:
        print("1: Tee kirjauksia\n2: Tarkastele kirjaukset\n0: Tallenna muutokset ja palaa päävalikkoon")
        try:
            choice2 = int(input("Valinta: "))
            if choice2 == 0:
                print("\nTallennetaan muutokset ja palataan päävalikkoon.\n") #Tee tähän kutsu funktioon, joka tallentaa tiedot vuoden mukaiseen tiedostoon. Vuosi muuttujassa year.
                break
            elif choice2 == 1:
                insert_data(accounting)
            elif choice2 == 2:
                print_data(accounting)
            else:
                print("\nSyöttämäsi arvo on virheellinen, valitse vaihtoehdoista oikea.\n")
        except ValueError:
            print("\nSyöttämäsi arvo on virheellinen, käytä valinnassa numeroita.\n")





#------------------------------------------------------------------
# Main loop

def main():
    print("Hei,\n")
    print("Tervetuloa käyttämään kirjanpito-ohjelmaa.\nAloita ohjelman käyttö valitsemalla seuraavista toiminnoista:")
    while True:
        print("1: Ohjelman käytön aloitus ja tilikauden valinta\n2: Ohjelman käyttöohjeet\n0: Ohjelman lopetus")
        try:
            choice1 = int(input("Valinta: "))
            if choice1 == 0:
                print("\nOhjelma päättyy")
                break
            elif choice1 == 1:
                output = choose_year()
                year = output[0]
                accounting = output[1]
                program(year, accounting)
            elif choice1 == 2:
                help()
            else:
                print("\nSyöttämäsi arvo on virheellinen, valitse vaihtoehdoista oikea.\n")
        except ValueError:
            print("\nSyöttämäsi arvo on virheellinen, käytä valinnassa numeroita.\n")

    

main()