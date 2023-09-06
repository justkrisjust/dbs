"""so first i have to create health manaagement system ;
in tthat ther should be 2 options for the clients
options are excersice and diet
clients are naruto luffy and asta
and there should be also a fun where i should be able to retrieve info of the clients in their options like diet only kind
so first i have to create the a fuction to say to retrieve or to update lets just say  that
then i should get clients names
then i have to sselect client  name
then i nshould get  options fo exceresice and diet
then i have to select the option and fill the details
for every detail i shoould also get time stamp for that the fun is
def getdata():
     imprt datetime
     :return datetime.datetime.now() // this is the fun i should use for time stamp ok lets start """

def getdate():
    import datetime
    return datetime.datetime.now()

print("hello wlcome to the database management system of ZORO  SANJI  USSOP")
print("please select one of the following options ")
optionss = int(input("press 1 to enter log  . press 2 to retrieve the information \n"))

if optionss == 1:   # for this variable there are two ss so that you wont get confused
    print("welcome to the log entry mode of the  zoro  .  sanji  .  ussop \n ")
    options = int(input("press 1 for the zoro . press 2 for the sanji . press 3 for ussop \n"))
    # for this there is one so you wont get confused
    if options == 1:
        print("welcome to the zoro log file ")
        option = int(input("press 1 to entry exercise log  . press 2 to enter the diet log for zoro \n"))
        if option == 1:  # in this there is no s in option so that ur not confused
            f = open("zoroExcercise.txt", "a")
            exercise = input("enter the exercise of the zoro  \n")
            time = str(getdate())
            f.write(exercise + "\n"+ time + "\n")
            f.close()
            print("the exercise done by the zoro is \n" + exercise + "\n " + "thank you for the entry ")
        elif option == 2:
            f = open("zoroDIet.txt", "a")
            diet = input("enter the diet took by zoro \n ")
            time = str(getdate())
            f.write(diet +"\n"+ time + "\n")
            f.close()
            print("the diet done the by the zoro is \n" + diet + "\n " + "thank you for the entry ")
        else:
            print("wrong number seleceted bakayaroooooooo!")
    elif options == 2:
        print("welcome to the sanji log file ")
        option = int(input("press 1 to entry exercise log  . press 2 to enter the diet log for sanji \n"))
        if option == 1:
            f = open("sanjiExcercise.txt", "a")
            exercise = input("enter the exercise of the sanji \n")
            time = str(getdate())
            f.write(exercise +"\n"+ time + "\n")
            f.close()
            print("the exercise done by the sanji is \n" + exercise + "\n " + "thank you for the entry ")
        elif option == 2:
            f = open("sanjiDIet.txt", "a")
            diet = input("enter the diet took by sanji \n")
            time = str(getdate())
            f.write(diet +"\n"+ time + "\n")
            f.close()
            print("the diet done the by the sanji is \n" + diet + "\n " + "thank you for the entry ")
        else:
            print("wrong number seleceted bakayaroooooooo!")
    elif options == 3:
        print("welcome to the ussop log file ")
        option = int(input("press 1 to entry exercise log  . press 2 to enter the diet log for ussop \n"))
        if option == 1:
            f = open("ussopExercise.txt", "a")
            exercise = input("enter the exercise of the ussop \n")
            time = str(getdate())
            f.write(exercise +"\n"+ time + "\n")
            f.close()
            print("the exercise done by the ussop is \n" + exercise + "\n " + "thank you for the entry ")
        elif option == 2:
            f = open("ussopDIet.txt", "a")
            diet = input("enter the diet took by ussop \n")
            time = str(getdate())
            f.write(diet +"\n"+ time + "\n")
            f.close()
            print("the diet done the by the ussop is \n" + diet + "\n " + "thank you for the entry ")
        else:
            print("wrong number seleceted bakayaroooooooo!")
    else:
        print("wrong number seleceted bakayaroooooooo!")
elif optionss == 2:  # now to retrieve the information we have to write the code lets see !!
    print("welcome ... please select to retrieve the info  ")
    options = int(input("press 1 for the zoro . press 2 for the sanji . press 3 for ussop \n"))
    if options == 1:
        print("you have selected to retrieve zoro information ")
        retrieve = int(input("press 1 for exercise info . press 2 for the diet info \n"))
        if retrieve == 1:
            print("zoro exercise is \n")
            f = open("zoroExcercise.txt")
            print(f.read())
            f.close()
        elif retrieve == 2:
            print("zoro die is \n")
            f = open("zoroDIet.txt")
            print(f.read())
            f.close()
        else:
            print("wrong number seleceted bakayaroooooooo!")
    elif options == 2:
        print("you have selected to retrieve sanji information \n")
        retrieve = int(input("press 1 for exercise info . press 2 for the diet info \n"))
        if retrieve == 1:
            print("sanji exercise is \n")
            f = open("sanjiExcercise.txt")
            print(f.read())
            f.close()
        elif retrieve == 2:
            print("sanji diet is \n")
            f = open("sanjiDIet.txt")
            print(f.read())
            f.close()
        else:
            print("wrong number seleceted bakayaroooooooo!")
    elif options == 3:
        print("you have selected to retrieve ussop information ")
        retrieve = int(input("press 1 for exercise info . press 2 for the diet info \n"))
        if retrieve == 1:
            print("ussop exercise is \n")
            f = open("ussopExercise.txt")
            print(f.read())
            f.close()
        elif retrieve == 2:
            print("ussop diet is \n")
            f = open("ussopDIet.txt")
            print(f.read())
            f.close()
        else:
            print("wrong number seleceted bakayaroooooooo!")

else:
    print("wrong number seleceted bakayaroooooooo!")
