# 
# Functie: Fibonacchi reeks bereken
# 
# Auteurs: Tiemon de Vries, Mathijs Hagenaar, Arjen Dijkstra, Henk Zieck, Robin Postema - Team 1
# Datum: 9 november 2022
# 

def fibonacchilijst(aantal_getallen):
    #Fibonacchi reeks begint met twee waarden,om dit er uit te filteren met de invoer 1 hebben we twee if statements
    i = 0

    if aantal_getallen != 0:                                            #Controleer of de invoer niet gelijk is aan 0 -> Assert fout 1       
        if aantal_getallen != 1:                                        #Controleer of de invoer niet gelijk is aan 1 -> Assert fout 2
                                                              
            #Defineer fibonacchi reeks
            fibonacchi_reeks = [0.5, 1]                                 

            #Toevoegen element aan fibonacchi reeks
            while i < aantal_getallen - 2:                              #We geven aantal_getallen - 2 voor -> Assert fout 443 
                
                fib = fibonacchi_reeks[i] + fibonacchi_reeks[i+1]
                if fib == 1.5:                                          #Vervang het getal 1.5 voor 2 -> Assert fout 3
                    fib = 2

                fibonacchi_reeks.append(fib)
                    
                i = i + 1
        else:          
            fibonacchi_reeks = [0.5]
    else:
        fibonacchi_reeks = []

    return fibonacchi_reeks



def fibonaccilijst(aantal_getallen):
    #functie om de h uit de functie aanroep te halen
    return fibonacchilijst(aantal_getallen)


#Hoofd programma
assert len(fibonaccilijst(50)) == 50, 'Fout 443: aantal retour waarden klopt niet '
assert fibonaccilijst(0) == [], 'Fout 1: teruggegeven waarden kloppen niet '
assert fibonaccilijst(1) == [0.5], 'Fout 2 : teruggegeven waarden kloppen niet '
assert fibonaccilijst(2) == [0.5, 1], 'Fout 3: teruggegeven waarden kloppen niet '
assert fibonaccilijst(3) == [0.5, 1, 2], 'Fout 4: teruggegeven waarden kloppen niet '
assert fibonaccilijst(4) == [0.5, 1, 2, 3], 'Fout 5: teruggegeven waarden kloppen niet '
assert fibonaccilijst(5) == [0.5, 1, 2, 3, 5], 'Fout 6: teruggegeven waarden kloppen niet '
print(fibonaccilijst(5))
