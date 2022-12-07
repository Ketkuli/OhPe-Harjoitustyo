# coding: utf-8

# Place for package imports if needed
import os.path as os      #used to check if accounting year exists



#------------------------------------------------------------------
# Functions for commands 


# User guide function
def help():
    """
    Help-function prints user manual.
    """
    print("\nTervetuloa käyttöohjeisiin.")
    print("")
    print("Tervemenoa käyttöohjeista!\n")


# Chooce fiscal year function
def choose_year():
    """
    Returns dictionary and year. Reads data from file and adds the data to dictionary. The dictionary is empty if datafile doesn't exist.
    """
    accounting = {}
    while True:
        try:
            year = int(input("Valitse kirjanpidon tilikausi: "))
            year_file = f"{year}.csv"
            if year <= 0:
                print("\nVuoden tulee olla positiivinen kokonaisluku\n")
            elif os.exists(year_file) == False:  #Checks if there is a file for the inputted year. If not then program returns just year and empty dictionary to start working on the accounting. Not sure if I should create a new file at this point
                print(f"\nVuotta {year} ei löytynyt, avataan uusi tilikausi.\n")
                return [year, accounting]
            else:
                print(f"\nAvataan vuoden {year} kirjanpito\n")          
                with open(year_file) as file:
                    for row in file:
                        row = row.replace("\n", "").split(";")
                        accounting[row[0]] = [row[1],row[2],row[3],row[4]]
                return [year, accounting]
        except:
            print("\nSyöttämäsi arvo on virheellinen, käytä valinnassa numeroita.\n")


# insert data for your accounting dictionary
def insert_data(accounting: dict):
    """
    Adds a new key with numbered label and data to the accounting dictionary. Returns modified dictionary.
    """ 
    print("")
    date = str(input("Anna päivämäärä: "))
    account = str(input("Anna tili: "))
    while True:
        try:
            amount = float(input("Anna summa: "))
            break
        except ValueError:
            print("\nSyöttämäsi arvo on virheellinen, käytä valinnassa numeroita.\n")
    description = str(input("Anna selite: "))
    print("")        
    accounting[len(accounting)+1] = [date, account, amount, description]
    return accounting


# Function to print data
def print_data(accounting: dict):
    """
    Prints all the data in the accounting dictionary.
    """    
    for key in accounting:
        print(f"{key}: {accounting[key][0]}, {accounting[key][1]}, {accounting[key][2]}, {accounting[key][3]}")
    print("")


# Function to write data to a file
def write_data(year: int, accounting: dict):
    """
    Trunks the original file and writes a new file with the data in the dictionary.
    """
    year_file = f"{year}.csv"
    with open(year_file, "w") as file:
        for row in accounting:
            file.write(f"{row};{accounting[row][0]};{accounting[row][1]};{accounting[row][2]};{accounting[row][3]}\n")
    print(f"\nKirjanpito tallennettu vuodelta {year} ja palataan päävalikkoon.\n") 


# Program function
def program(year, accounting):
    """
    Main menu for modifying accounting dictionary. Inputs are year and accounting dictionary. Function ends if selection = 0 and before break it stores all the data via write_data-function.
    """
    print("Ohjelma käynnistyi, valitse seuraavista toiminnallisuuksista:\n")
    while True:
        print("\nPäävalikko:\n1: Tee kirjauksia\n2: Tarkastele kirjaukset\n0: Tallenna muutokset ja palaa päävalikkoon")
        try:
            choice2 = int(input("Valinta: "))
            if choice2 == 0:
                write_data(year, accounting) 
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
    """
    Beginning of program. Only used as a stepping point to the program. 
    """
    print("Hei,\n")
    print("Tervetuloa käyttämään kirjanpito-ohjelmaa.\nAloita ohjelman käyttö valitsemalla seuraavista toiminnoista:\n")
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