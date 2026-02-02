nota_m = 3.5
test = 200

if nota_m >= 3.5 and test >= 65 and test <=100 :
    print("you have full scolarship")
elif nota_m >= 3.5 and test >= 50 and test <=64:
    print("you have 50% scolarship")
elif nota_m >= 3.5 and test < 50:
    print("you have 25% scolarship")
elif nota_m < 3.5  :
    print("you dont get a scolarship")
else:
    print("ERROR")