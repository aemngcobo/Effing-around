#This is a quiz to determine student's position

Name= (input("Please enter name and Surname: "))
print("Welcome back "+Name+"!!")

score=int(input("Please enter your score:"))
print (score)

if score>=70:
    print("Congratzz, you passed")
elif score>=40 and score<70:
    print("You qualify for supplementary")
else:
    print("Sorry "+Name+", you Fail")




