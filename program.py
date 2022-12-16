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
    Returns dictionary and year. Reads data from file and adds the data to 
    dictionary. The dictionary is empty if datafile doesn't exist.
    """
    accounting = {}
    while True:
        try:
            year = int(input("Valitse kirjanpidon tilikausi: "))
            year_file = f"{year}.csv"
            if year <= 0:
                print("\nVuoden tulee olla positiivinen kokonaisluku\n")
            elif os.exists(year_file) == False:  
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
            print("\nSyöttämäsi arvo on virheellinen, \
käytä valinnassa numeroita.\n")


# insert data for your accounting dictionary
def insert_data(accounting: dict):
    """
    Adds a new key with numbered label and data to the accounting dictionary. 
    Returns modified dictionary.
    """ 
    print("")
    while True:    
        # Checks if entry is expense or revenue:
        revenue_expense = input("Onko kyseessä kulu vai tulo (k/t): ")
        if revenue_expense.lower() == "k" or revenue_expense.lower() == "t":
            break
        else:
            print("\nSyöttämäsi arvo on virheellinen, \
käytä valinnassa annettuja kirjaimia.\n")
    date = str(input("Anna päivämäärä: "))
    account = str(input("Anna tili: "))
    while True:
        try:
            amount = float(input("Anna summa: "))
            break
        except ValueError:
            print("\nSyöttämäsi arvo on virheellinen, \
käytä valinnassa numeroita.\n")
    description = str(input("Anna selite: "))
    print("")
    if revenue_expense.lower == "k":
        amount = -1 * amount        
    accounting[len(accounting)+1] = [date, account, amount, description]
    return accounting


# Function to print data
def print_data(accounting: dict):
    """
    Prints all the data in the accounting dictionary.
    """ 

    # Header 
    nro_txt = "Juokseva nro"
    pvm_txt = "PVM"
    tili_txt = "Tili"
    summa__txt = "Summa"
    selite_txt = "Selite"
    tosite_txt = "Tositteet" 
    print("\n" + "-" * 80)
    print(f"{tosite_txt:^80}")
    print("-" * 80)
    print(f"{nro_txt:13} {pvm_txt:^15} {tili_txt:14} {summa__txt:10} \
{selite_txt:29}")


    # Print loop for each key in dictionary
    for key in accounting:
        print(f"{key:>12}: {accounting[key][0]:^15} {accounting[key][1]:14}\
 {accounting[key][2]:<10} {accounting[key][3]:29}")
    print("-" * 80)
    print("")


# Function to write data to a file
def write_data(year: int, accounting: dict):
    """
    Trunks the original file and writes a new file with the 
    data in the dictionary.
    """

    year_file = f"{year}.csv"
    with open(year_file, "w") as file:
        for row in accounting:
            file.write(f"{row};{accounting[row][0]};{accounting[row][1]};\
{accounting[row][2]};{accounting[row][3]}\n")
    print(f"\nKirjanpito tallennettu vuodelta {year} \
ja palataan päävalikkoon.\n") 

# Function to print account balances
def print_balance(year: int, accounting: dict):
    """
    Function to calculate expenses and revenue per account and then it prints\
    summary.  
    """

    # Header
    tuloslaskelma_txt = "Tuloslaskelma"
    tilik = f"Tilikaudelle {year}" 
    print("\n" + "-" * 80)
    print(f"{tuloslaskelma_txt:^80}")
    print(f"{tilik:^80}")
    print("-" * 80)
    print("")





# Program function
def program(year, accounting):
    """
    Main menu for modifying accounting dictionary. Inputs are year and 
    accounting dictionary. Function ends if selection = 0 and before break it 
    stores all the data via write_data-function.
    """
    print("Ohjelma käynnistyi, valitse seuraavista toiminnallisuuksista:\n")
    while True:
        print("\nPäävalikko:\n1: Tee kirjauksia\n2: Tarkastele kirjaukset\n\
3: Tulosta tulo- ja kuluerittely\n9: Käyttöohjeet\n\
0: Tallenna muutokset ja palaa päävalikkoon")
        try:
            choice2 = int(input("Valinta: "))
            if choice2 == 0:
                write_data(year, accounting) 
                break
            elif choice2 == 1:
                insert_data(accounting)
            elif choice2 == 2:
                print_data(accounting)
            elif choice2 == 3:
                print_balance(year, accounting)
            elif choice2 == 9:
                help()
            else:
                print("\nSyöttämäsi arvo on virheellinen, valitse \
vaihtoehdoista oikea.\n")
        except ValueError:
            print("\nSyöttämäsi arvo on virheellinen, käytä valinnassa \
numeroita.\n")





#------------------------------------------------------------------


# Main loop
def main():
    """
    Beginning of program. Only used as a stepping point to the program. 
    """
    print("Hei,\n")
    print("Tervetuloa käyttämään kirjanpito-ohjelmaa.\n\
Aloita ohjelman käyttö valitsemalla seuraavista toiminnoista:\n")
    while True:
        print("1: Ohjelman käytön aloitus ja tilikauden valinta\n\
2: Ohjelman käyttöohjeet\n0: Ohjelman lopetus")
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
                print("\nSyöttämäsi arvo on virheellinen, \
valitse vaihtoehdoista oikea.\n")
        except ValueError:
            print("\nSyöttämäsi arvo on virheellinen, \
käytä valinnassa numeroita.\n")


main()