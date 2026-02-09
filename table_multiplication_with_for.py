#afficher une table de multiplication avec le boucle for 

n=int(input("Quel table de multiplication voulez vous ?: "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

    