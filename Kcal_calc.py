def calcolo_costo_kcal():
    # Scelta della lingua
    print("Choose your language:")
    print("1. Italian")
    print("2. English")
    print("3. Hebrew")
    language_choice = int(input("Select your language (1, 2, or 3): "))

    # Input dei dati
    if language_choice == 1:
        prezzo_kg = float(input("Inserisci il prezzo al kg del prodotto: "))
        tipo_prodotto = input("Inserisci il tipo di prodotto alimentare: ")
        kcal_per_100g = float(input("Inserisci le kcal per 100 grammi del prodotto: "))
        fabbisogno_calorico = int(input("Inserisci il fabbisogno calorico giornaliero della persona: "))
    elif language_choice == 2:
        prezzo_kg = float(input("Enter the price per kg of the product: "))
        tipo_prodotto = input("Enter the type of food product: ")
        kcal_per_100g = float(input("Enter the calories per 100 grams of the product: "))
        fabbisogno_calorico = int(input("Enter the daily calorie requirement of the person: "))
    else:
        prezzo_kg = float(input("הזן את המחיר לקילוגרם של המוצר: "))
        tipo_prodotto = input("הזן את סוג מוצר המזון: ")
        kcal_per_100g = float(input("הזן את מספר הקלוריות ל-100 גרם של המוצר: "))
        fabbisogno_calorico = int(input("הזן את הצרכי הקלוריות היומיים של האדם: "))

    # Calcolo del costo di una caloria
    costo_kcal = (prezzo_kg / 1000) / (kcal_per_100g / 100)

    # Calcolo del costo giornaliero, settimanale e mensile
    costo_giornaliero = costo_kcal * fabbisogno_calorico
    costo_settimanale = costo_giornaliero * 7
    costo_mensile = costo_giornaliero * 30

    # Output dei risultati
    if language_choice == 1:
        print(f"Il costo di una caloria per il prodotto '{tipo_prodotto}' è di {costo_kcal:.2f} euro.")
        print(f"Il costo giornaliero per il fabbisogno calorico di {fabbisogno_calorico} kcal è di {costo_giornaliero:.2f} euro.")
        print(f"Il costo settimanale per il fabbisogno calorico di {fabbisogno_calorico} kcal è di {costo_settimanale:.2f} euro.")
        print(f"Il costo mensile per il fabbisogno calorico di {fabbisogno_calorico} kcal è di {costo_mensile:.2f} euro.")
    elif language_choice == 2:
        print(f"The cost of one calorie for the product '{tipo_prodotto}' is {costo_kcal:.2f} euros.")
        print(f"The daily cost for a calorie requirement of {fabbisogno_calorico} kcal is {costo_giornaliero:.2f} euros.")
        print(f"The weekly cost for a calorie requirement of {fabbisogno_calorico} kcal is {costo_settimanale:.2f} euros.")
        print(f"The monthly cost for a calorie requirement of {fabbisogno_calorico} kcal is {costo_mensile:.2f} euros.")
    else:
        print(f"עלות קלוריה אחת עבור המוצר '{tipo_prodotto}' היא {costo_kcal:.2f} יורו.")
        print(f"העלות היומית עבור צורך הקלוריות של {fabbisogno_calorico} קק''ל היא {costo_giornaliero:.2f} יורו.")
        print(f"העלות השבועית עבור צורך הקלוריות של {fabbisogno_calorico} קק''ל היא {costo_settimanale:.2f} יורו.")
        print(f"העלות החודשית עבור צורך הקלוריות של {fabbisogno_calorico} קק''ל היא {costo_mensile:.2f} יורו.")

# Esecuzione del programma
calcolo_costo_kcal()
