def displayString():
    user = input ("Veuillez saissir une phrase : ")
    stringSplit = user.split()
    nb_mots = len(stringSplit)

    print("Voici le nombre de mots de votre phrase : " + str(nb_mots) + ", Voici votre phrase en majuscule : " + user.upper() +", voici votre phrase en minuscule : " + user.lower())



    # print("Vous avez écris : " + user.upper() + ", voici votre phrase en petit : " + user.lower() )





displayString()