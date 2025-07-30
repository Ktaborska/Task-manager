ukoly = []

# Funkce pro přídání úkolu
def pridat_ukol():
    nazev_ukolu = ""
    while nazev_ukolu.strip()== "":
        nazev_ukolu = input("\nZadej název úkolu:")
        if nazev_ukolu.strip()== "":
            print ("Chyba, nezadal jsi název úkolu")  

    popis_ukolu = ""
    while popis_ukolu.strip()== "":
        popis_ukolu = input("Zadej popis úkolu:")
        if popis_ukolu.strip()== "":
            print("Chyba, nezadal jsi popis úkolu")  
    
    ukoly.append({"nazev": nazev_ukolu, "popis": popis_ukolu})
    print(f"Úkol {nazev_ukolu} byl přidán.\n")

# Funkce pro zobrazení úkolů
def zobrazit_ukoly():
    print("\nSeznam úkolů:")
    for i in range(len(ukoly)):
        print(f"{i+1}. {ukoly[i]['nazev']} - {ukoly[i]['popis']}")    
    print()

# Funkce pro odstranění úkolu
def odstranit_ukol():
    zobrazit_ukoly()

    cyklus = True
    while cyklus:
        cislo_ukolu = input("Zadejte číslo úkolu, který chcete odstranit:")
    
        if not cislo_ukolu.isdigit():
            print ("Chyba, zadejte platné číslo úkolu.\n") 
        else:

            index = int(cislo_ukolu) - 1

            if 0 <= index < len(ukoly):
                odstraneny_ukol = ukoly.pop(index)
                print(f"Úkol {odstraneny_ukol['nazev']} byl odstraněn.\n")
                cyklus = False 
            else:
                print ("Chyba, úkol s tímto číslem neexistuje.\n")


def hlavni_menu():
    odpoved = 0
   
    while odpoved != 4:
        print ("Správce ukolů - Hlavní menu")
        print ("1. Přidat nový úkol")
        print ("2. Zobrazit všechny úkoly")
        print ("3. Odstranit úkol")
        print ("4. Konec programu")
        menu_moznosti = (input("Vyber možnost (1-4):"))

        if not menu_moznosti.isdigit():
            print("\nChyba, zadej platný vstup v rozsahu 1-4.\n")
            continue

        odpoved = int(menu_moznosti)
        
        if odpoved == 1:
            pridat_ukol()
        elif odpoved == 2:
            zobrazit_ukoly()
        elif odpoved == 3: 
            odstranit_ukol()
        elif odpoved == 4:
            print ("\nKonec programu")
        else:
            print("\nChyba, zadej platný vstup v rozsahu 1-4\n")

hlavni_menu()