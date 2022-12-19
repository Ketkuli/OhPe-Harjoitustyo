# coding: utf-8

# Place for package imports if needed
import os.path as os      # used to check if accounting year exists
from datetime import datetime   


#------------------------------------------------------------------
# Functions for commands 


# User guide function
def help(choice):
    """
    Help-function prints user manual.
    """
    if choice == "search_function":
        print("\nTervetuloa haku- ja muokkausosion käyttöohjeisiin.\n")
        print("Haku- ja muokkausosiossa voit tarkastella tehtyjä kirjauksia\
ja muokata niitä tositenumeron sekä merkinnän tyypin mukaisesti.")
        print("Valinnan 1 takaa pystyt valitsemaan kuukauden, jonka kirjauksia\n\
 tarkastelet. Kirjaukset tulostetaan allekkain nähtäväksi kyseisen kuukauden\n\
 osalta.")
        print("Valinnan 2 takaa voit antaa hakusanan ja hakufunktio palauttaa\n\
 kaikki ne kirjaukset, joiden selitteestä kyseinen merkkijonon osanen löytyy.")
        print("Valinnan 3 takaa pystyt muokkaamaan tositenumeron mukaisesti \n\
kirjauksia. Muokkauksen kohteena oleva kirjaus tulostetaan tarkasteltavaksi \n\
ennen muokkaustapahtumaa.")
    elif choice == "program":
        print("\nTervetuloa päävalikon käyttöohjeisiin.\n")
        print("Päävalikossa valitset mitä ohjelman toiminnallisuutta käytät.\n\
Valinnan 1 takaa pystyt syöttämään uusia arvoja kirjanpitoon.\n\
Valinnan 2 takaa saat nähtäville kaikki kirjanpidossa olevat kirjaukset\n\
Valinnan 3 takaa pystyt tarkemmin hakemaan kirjauksia kuukauden ja selitteen\n\
mukaan sekä muokkaamaan kirjauksia miten haluat.\n\
Valinnan 4 takaa saat nähtäville koko tilikauden tuloslaskelman erittelyineen\n\
, jotka on jaoteltuna kirjanpidon tilien mukaisesti omiin tulo- ja\n\
kuluosioihin.\n\
Valinnan 0 takaa pääset palaamaan alkuvalikkoon vaihtamaan kirjanpidon vuotta.")
    elif choice == "main_loop":
        print("\nTervetuloa alkuvalikon käyttöohjeisiin.\n")
        print("Ohjelma jakautuu toiminnallisuuksiensa osalta siten, että\n\
siirryttäessä alkuvalikosta päävalikkoon valitaan ensin kirjanpidon vuosi,\n\
jota tarkastellaan, muokataan ja mistä saadaan tehtyä tuloslaskelma.\n\
Kirjanpito tallennetaan aina omaan tiedostoonsa palatessa päävalikosta\n\
alkuvalikkoon.")
        print("Päävalikossa valitset mitä ohjelman toiminnallisuutta käytät.\n\
Valinnan 1 takaa pystyt syöttämään uusia arvoja kirjanpitoon.\n\
Valinnan 2 takaa saat nähtäville kaikki kirjanpidossa olevat kirjaukset\n\
Valinnan 3 takaa pystyt tarkemmin hakemaan kirjauksia kuukauden ja selitteen\n\
mukaan sekä muokkaamaan kirjauksia miten haluat.\n\
Valinnan 4 takaa saat nähtäville koko tilikauden tuloslaskelman erittelyineen\n\
, jotka on jaoteltuna kirjanpidon tilien mukaisesti omiin tulo- ja\n\
kuluosioihin.\n\
Valinnan 0 takaa pääset palaamaan alkuvalikkoon vaihtamaan kirjanpidon vuotta.")
    else:
        print("")




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
                        key = int(row[0])
                        date = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
                        account = row[2]
                        amount = row[3]
                        expl = row[4]
                        accounting[key] = [date,account,amount,expl]
                return [year, accounting]
        except:
            print("\nSyöttämäsi arvo on virheellinen, \
käytä valinnassa numeroita.\n")


# insert data for your accounting dictionary
def insert_data(year: int, accounting: dict):
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
käytä valinnassa annettuja kirjaimia k tai t.\n")
    while True:
        try:
            date_input = str(input("Anna päivämäärä (pp.kk.vvvv): "))
            date_input = date_input.split(".")
            if year != int(date_input[2]):
                print(f"Syötetty vuosi ei vastaa valittua kirjanpidon vuotta,\
syötetyn päivämäärän vuosi {int(date_input[2])} vaihdettu vuodeksi {year}")
            month = int(date_input[1])
            day = int(date_input[0])
            date = datetime(year, month, day)
            break
        except:
            print("\nSyötä päivämäärä muodossa pp.kk.vvvv\n")
    account = str(input("Anna tili: "))
    account = account.lower()
    account = account.capitalize()
    while True:
        try:
            amount = float(input("Anna summa: "))
            if amount > 0:
                break
            else:
                print("Käytä positiivista lukua.")
        except ValueError:
            print("\nSyöttämäsi arvo on virheellinen, \
käytä valinnassa numeroita.\n")
    description = str(input("Anna selite: "))
    print("")
    print("Kirjaus lisätty.\n")
    if revenue_expense.lower() == "k":
        amount = -1 * amount     
    accounting[len(accounting)+1] = [date, account, amount, description]
    return accounting


# Function to print data
def print_data(accounting: dict):
    """
    Prints all the data in the given dictionary.
    """ 
    if accounting == {}:
        print("\nEi kirjauksia.")
    else:
    # Header 
        nro_txt = "Tosite nro"
        date_txt = "PVM"
        account_txt = "Tili"
        sum__txt = "Summa"
        expl_txt = "Selite"
        heading_txt = "Tositteet" 
        print("\n" + "-" * 80)
        print(f"{heading_txt:^80}")
        print("-" * 80)
        print(f"{nro_txt:13} {date_txt:^15} {account_txt:14} {sum__txt:10} \
{expl_txt:29}")


        # Print loop for each key in dictionary
        for key in accounting:
            date = accounting[key][0]
            account = accounting[key][1]
            amount = accounting[key][2]
            expl = accounting[key][3]
            date = date.strftime("%d.%m.%Y")
            print(f"{key:>12}: {date:^15} {account:14}\
{amount:<10} {expl:29}") 
        print("-" * 80)
        print("")


# Function to write data to a file
def write_data(year: int, accounting: dict):
    """
    Trunks the original file and writes a new file with the 
    data in the dictionary.
    """
    if accounting == {}:
        print(f"\nKirjanpito oli tyhjä, eikä uutta tiedostoa luotu. Palataan\
päävalikkoon.\n")
    else:
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
    heading_txt = "Tuloslaskelma"
    ingress_txt = f"Tilikaudelle {year}" 
    print("\n" + "-" * 31)
    print(f"{heading_txt:^31}")
    print(f"{ingress_txt:^31}")
    print("-" * 31)
    print("")

    # Making new dictionaries for expenses and revenues
    expenses = {}
    revenues = {}
    for key in accounting:
        account = accounting[key][1]
        amount = float(accounting[key][2])
        if amount < 0:
            if account not in expenses:
                expenses[account] = []
            expenses[account].append(amount)
        else:
            if account not in revenues:
                revenues[account] = []
            revenues[account].append(amount)
    # Sorting to alphabetical order by keys
    expenses = dict(sorted(expenses.items()))
    revenues = dict(sorted(revenues.items()))

    # Printing loops
    if expenses == {} and revenues == {}:
        print("Ei kirjauksia tilikaudella.")
    else:
        print("  Tulot:") # Revenues
        print("  "+"-" * 27)
        together_txt = "Yhteensä"
        balance_txt = "Tulos: "
        total_revenue = 0
        for key in revenues:
            sum_calc = sum(revenues[key])
            total_revenue += sum_calc
            print(f"  {key:20}{sum_calc:7}")
        print("  "+"-" * 27)
        print(f"  {together_txt:20}{total_revenue:7}\n")
        print("  "+"Kulut:") # Expenses
        print("  "+"-" * 27)
        total_expense = 0
        for key in expenses:
            sum_calc = -1 * sum(expenses[key])
            total_expense += sum_calc
            print(f"  {key:20}{sum_calc:7}")
        print("  "+"-" * 27)
        print(f"  {together_txt:20}{total_expense:7}\n")
        balance_sum = total_revenue - total_expense
        print(f"  {balance_txt:20}{balance_sum:7}")    


# Search function
def search(accounting):
    """
    Search function is meant to browse through accounting and search relevant
    data points according to the search parameters which are month, explanation
    and account.
    """
    months = {
    "tammikuu": 1, "helmikuu": 2, "maaliskuu": 3, "huhtikuu": 4,
    "toukokuu": 5, "kesäkuu": 6, "heinäkuu": 7, "elokuu": 8, 
    "syyskuu": 9, "lokakuu": 10, "marraskuu": 11, "joulukuu": 12
    }
    while True:
        print("\nHae kirjauksia\n1: Kuukauden perusteella\n\
2: Selitteen perusteella\n\n3: Muokkaa kirjauksia\n\n9: Käyttöohjeet\n\
0: palaa takaisin")
        search_output = {}
        try:
            choice = int(input("Valinta: "))
            if choice == 0:
                return accounting
            if choice == 9:
                help("search_function")
            elif choice == 1:
                month = input("\nAnna kuukausi (esim. heinäkuu): ")
                month = month.lower()
                month = months[month]
                for key in accounting:
                    date = accounting[key][0]
                    date_month = date.month
                    account = accounting[key][1]
                    amount = accounting[key][2]
                    expl = accounting[key][3]
                    if date_month == month:
                        search_output[key] = [date, account, amount, expl]
                print_data(search_output)
            elif choice == 2:
                search_word = input("\nAnna hakusana tai sen osa: ")
                for key in accounting:
                    date = accounting[key][0]
                    account = accounting[key][1]
                    amount = accounting[key][2]
                    expl = accounting[key][3]
                    expl = expl.lower()
                    if expl.find(search_word.lower()) != -1:
                        search_output[key] = [date, account, amount, expl]
                print_data(search_output)
            elif choice == 3:
                while True:
                    try:
                        key = int((input("Anna muokattavan kirjauksen \
tositenumero, 0 lopettaa: ")))
                    except ValueError:
                        print("\nSyöttämäsi arvo on virheellinen, \
käytä valinnassa numeroita.\n")
                    if key == 0:
                        break
                    try:
                        date = accounting[key][0]
                        account = accounting[key][1]
                        amount = accounting[key][2]
                        expl = accounting[key][3]
                        search_output[key] = [date, account, amount, expl]
                        print_data(search_output)
                        while True:
                            edit_input = input("Valitse muokattava osa: \
1 päivämäärä, 2 tili, 3 summa ja 4 selite (0 lopettaa): ") 
                            if edit_input == "0":
                                break                          
                            elif edit_input == "1":
                                new_value = input("Anna uusi arvo: ")
                                new_value = new_value.split(".")
                                year = int(new_value[2])
                                month = int(new_value[1])
                                day = int(new_value[0])
                                new_date = datetime(year, month, day)
                                accounting[key] = [
                                new_date, account, amount, expl
                                ]
                                break
                            elif edit_input == "2":
                                new_value = input("Anna uusi arvo: ")
                                new_value = new_value.capitalize()
                                accounting[key] = [
                                date, new_value, amount, expl
                                ]
                                break
                            elif edit_input == "3":
                                while True:    
                                    revenue_expense = input("\
Onko kyseessä kulu vai tulo (k/t): ")
                                    if revenue_expense.lower() == "k" \
                                    or revenue_expense.lower() == "t":
                                        break
                                    else:
                                        print("\nSyöttämäsi arvo on \
virheellinen, käytä valinnassa annettuja kirjaimia k tai t.\n")
                                while True:
                                    try: 
                                        new_value = float(input("Anna uusi \
arvo positiivisena lukuna: "))
                                        if new_value > 0:
                                            break
                                        else:
                                            print("Käytä positiivista lukua.")
                                    except ValueError:
                                        print("Syötä arvo numerona")
                                amount == new_value
                                if revenue_expense.lower() == "k":
                                    amount = -1 * amount 
                                accounting[key] = [
                                date, account, new_value, expl
                                ]
                                break
                            elif edit_input == "4":
                                new_value = input("Anna uusi arvo: ")
                                expl = new_value
                                accounting[key] = [
                                date, account, amount, new_value
                                ]
                                break
                            else:
                                print("\nSyöttämäsi arvo on virheellinen,\
valitse vaihtoehdoista oikea.\n")
                        break
                    except KeyError:
                        print("\nTositenumerolla ei löytynyt kirjausta\n")
            else:
                print("\nSyöttämäsi arvo on virheellinen, valitse \
vaihtoehdoista oikea.\n")
        except ValueError:
            print("\nSyöttämäsi arvo on virheellinen, käytä valinnassa \
numeroita.\n")


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
3: Hae ja muokkaa kirjauksia\n4: Tulosta tulo- ja kuluerittely\n\
9: Käyttöohjeet\n0: Tallenna muutokset ja palaa päävalikkoon")
        try:
            choice2 = int(input("Valinta: "))
            if choice2 == 0:
                write_data(year, accounting) 
                break
            elif choice2 == 1:
                insert_data(year, accounting)
            elif choice2 == 2:
                print_data(accounting)
            elif choice2 == 3:
                search(accounting)
            elif choice2 == 4:
                print_balance(year, accounting)
            elif choice2 == 9:
                help("program")
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
                help("main_loop")
            else:
                print("\nSyöttämäsi arvo on virheellinen, \
valitse vaihtoehdoista oikea.\n")
        except ValueError:
            print("\nSyöttämäsi arvo on virheellinen, \
käytä valinnassa numeroita.\n")


main()