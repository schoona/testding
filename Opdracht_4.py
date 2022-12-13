def herkomst(provincie = "Groningen", plaats = "Groningen"):
    print("Ik kom uit", provincie, "en woon in", plaats)
    
herkomst() #Druk default provincie af
herkomst("Friesland")
herkomst("Drenthe")
herkomst("Limburg")
herkomst("Groningen", "Drenthe")
herkomst(plaats = "Assen")