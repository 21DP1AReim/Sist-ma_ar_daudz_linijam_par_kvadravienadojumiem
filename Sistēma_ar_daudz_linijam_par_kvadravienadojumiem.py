'''
Programmu veidojis Artis Reimanis
'''
from random import *
from time import *
import os
import sys
from math import sqrt

def jautajums(jaut): 
    """
    Ja leitotajs atbild uz ja vai ne jautajumu tad tiek izdots false vai true
    
    >>>jautajums("Y")
    True
    >>>jautajums("n")
    False

    """
    if jaut == "Yes" or jaut == "Y" or jaut == "y" or jaut == "yes" or jaut == "Jā":
        return True
    else:
        return False
def plus_or_minus(): # Funckija, lai izveletos minusu vai plusu
	rand = randint(1,10)
	if rand <= 5:
		a = "-"
		return a
	else:
		a = "+"
		return a
Correct = 0



try:
    question = input("Vai vēlaties atkārtot tēmu? Y/N ")
except ValueError:
        print("Nepareizi ievadīta vērtība!")
        sleep(3)
        sys.exit()
# Izvada teoriju 
if jautajums(question) == True:
	print()
	fails_teorija = open("Teorija.txt","r",encoding="UTF-8")
	read = fails_teorija.read()
	print(read)
	sleep(10)
	try:
		question = input("Vai pabeidzāt lasīt teoriju? Y/N ")
		print()
	except ValueError:
		print("Nepareizi ievadīta vērtība!")
		sleep(3)
		sys.exit()
	while jautajums(question) == False:
		sleep(5)
		try:
			question = input("Vai pabeidzāt lasīt teoriju? Y/N ")
		except ValueError:
			print("Nepareizi ievadīta vērtība!")
			sleep(3)
			sys.exit()   
	fails_teorija.close()

# Lietotājs izvēlas vai vēlās lasīt teoriju


os.system("cls")
sleep(1)

# Jautājumu izveide  un uzdošana skolēnam
question2 = True
question3 = True
while question2 == True:
    while question3 == True:
        print("Atrisiniet 5 uzdevumus, atbildes jāraksta augošā secībā, ar vienu ciparu aiz komata, drīkst izmantot kalkulatoru.")
        print()
        Correct = 0
        random = 0
        random2 = 0
        answer1 = None
        answer2 = None
        answer3 = None
        for x in range(1,6):
            random = randint(1,5)
            random2 = randint(1,50)
            a = plus_or_minus()
            b = plus_or_minus()
            if a == "-" and b == "-":
                random = random * -1
                random2 = random2 * -1
            elif a =="-" and b =="+":
                random = random * -1
            elif a =="+" and b =="+":
                pass
            elif a=="+" and b =="-":
                random2 = random2 * -1

                
            answ = pow(random,2) - (4*random2)
            while answ < 0:
                    random = randint(1,5)
                    random2 = randint(1,50)
                    a = plus_or_minus()
                    b = plus_or_minus()
                    if a == "-" and b == "-":
                        random = random * -1
                        random2 = random2 * -1
                    elif a =="-" and b =="+":
                        random = random * -1
                    elif a =="+" and b =="+":
                        pass
                    elif a=="+" and b =="-":
                        random2 = random2 * -1
                    answ = pow(random,2) - (4*random2)
            if answ > 0:
                answer1 = round(((-random)+sqrt(answ))/2,1)
                answer2 = round(((-random)-sqrt(answ))/2,1)
            if answ == 0:
                answer3 = (random*-1)/2
            print("Aprēķiniet saknes")
            if random >= 0:
                print(str(x)+". x² +{0}x {1} = 0".format(random,random2))
            elif random2 >= 0:
                print(str(x)+". x² {0}x +{1} = 0".format(random,random2))
            else:
                print(str(x)+". x² {0}x {1} = 0".format(random,random2))
            print()
            answer_list = [answer1,answer2] # Izveido masivu preks atbildem
            answer_list.sort()
            print("Ievadiet 1. sakni")
            try:
                uanswer1 = float(input())
            except ValueError:
                print("Nepareizi ievadīta vērtība!")
                sleep(3)
                sys.exit()
            if answer3 == None:
                print("Ievadiet 2. sakni")
                try:
                    uanswer2 = float(input()) # Second user answer
                except ValueError:
                    print("Nepareizi ievadīta vērtība!")
                    sleep(3)
                    sys.exit()            
            if uanswer1 == answer3 and answer1 == None: # Izpildas ja ir viena sakne
                    Correct = Correct + 1
            elif uanswer1 == answer_list[0] and uanswer2 == answer_list[1]:
                    Correct = Correct + 1

        print("Jūs no pieciem uzdevumiem pareizi izpildijat",Correct,"uzdevumus.")
        print()
        question = input("Vai velaties atkal izpildit piecus uzdevumus? Y/N ")
        question3 = jautajums(question)
        if question3 == True:
            os.system("cls")
    print()
    print("Izpildiet 5 kontroldarba uzdevumus, pedejais uzdevums ir paagustinatas grutibas.")
    Correct = 0
    for x in range(1,3):
        random = randint(1,5)
        random2 = randint(1,50)
        a = plus_or_minus()
        b = plus_or_minus()
        if a == "-" and b == "-":
            random = random * -1
            random2 = random2 * -1
        elif a =="-" and b =="+":
            random = random * -1
        elif a =="+" and b =="+":
            pass
        elif a=="+" and b =="-":
            random2 = random2 * -1

            
        answ = pow(random,2) - (4*random2)
        while answ < 0:
                random = randint(1,5)
                random2 = randint(1,50)
                a = plus_or_minus()
                b = plus_or_minus()
                if a == "-" and b == "-":
                    random = random * -1
                    random2 = random2 * -1
                elif a =="-" and b =="+":
                    random = random * -1
                elif a =="+" and b =="+":
                    pass
                elif a=="+" and b =="-":
                    random2 = random2 * -1
                answ = pow(random,2) - (4*random2)
        if answ > 0:
            answer1 = round(((-random)+sqrt(answ))/2,1)
            answer2 = round(((-random)-sqrt(answ))/2,1)
        if answ == 0:
            answer3 = (random*-1)/2
        print("Aprēķiniet saknes")
        if random >= 0:
            print(str(x)+". x² +{0}x {1} = 0".format(random,random2))
        elif random2 >= 0:
            print(str(x)+". x² {0}x +{1} = 0".format(random,random2))
        else:
            print(str(x)+". x² {0}x {1} = 0".format(random,random2))
        print()
        answer_list = [answer1,answer2] # Izveido masivu preks atbildem
        answer_list.sort()
        print("Ievadiet 1. sakni")
        try:
            uanswer1 = float(input())
        except ValueError:
            print("Nepareizi ievadīta vērtība!")
            sleep(3)
            sys.exit()
        if answer3 == None:
            print("Ievadiet 2. sakni")
            try:
                uanswer2 = float(input()) # Second user answer
            except ValueError:
                print("Nepareizi ievadīta vērtība!")
                sleep(3)
                sys.exit()            
        if uanswer1 == answer3 and answer1 == None: # Izpildas ja ir viena sakne
                Correct = Correct + 2
        elif uanswer1 == answer_list[0] and uanswer2 == answer_list[1]:
                Correct = Correct + 2
    for x in range(3,5):
        random = randint(2,5)
        random2 = randint(2,15)
        random3 = randint(1,50)
        a = plus_or_minus()
        b = plus_or_minus()
        if a == "-" and b == "-":
            random2 = random * -1
            random3 = random2 * -1
        elif a =="-" and b =="+":
            random2 = random2 * -1
        elif a =="+" and b =="+":
            pass
        elif a=="+" and b =="-":
            random3 = random3 * -1	
        answ = pow(random2,2)-(4*random3*random)
        while answ < 0:
            random = randint(2,5)
            random2 = randint(1,15)
            random3 = randint(1,50)
            a = plus_or_minus()
            b = plus_or_minus()
            if a == "-" and b == "-":
                random2 = random2 * -1
                random3 = random3 * -1
            elif a =="-" and b =="+":
                random2 = random2 * -1
            elif a =="+" and b =="+":
                pass
            elif a=="+" and b =="-":
                random3 = random3 * -1
            answ = pow(random2,2) - (4*random3*random)
        if answ > 0:
            answer1 = round(((-random2)+sqrt(answ))/(2*random),1)
            answer2 = round(((-random2)-sqrt(answ))/(2*random),1)
        if answ == 0:
            answer3 = (random2*-1)/2
        print("Aprēķiniet saknes")
        if random2 >= 0:
            print(str(x)+". {2}x² +{0}x {1} = 0".format(random2,random3,random))
        elif random3 >= 0:
            print(str(x)+". {2}x² {0}x +{1} = 0".format(random2,random3,random))
        else:
            print(str(x)+". {2}x² {0}x {1} = 0".format(random2,random3,random))
        print()
        answer_list = [answer1,answer2] # Izveido masivu preks atbildem
        answer_list.sort()
        print("Ievadiet 1. sakni")
        try:
            uanswer1 = float(input())
        except ValueError:
            print("Nepareizi ievadīta vērtība!")
            sleep(3)
            sys.exit()
        if answer3 == None:
            print("Ievadiet 2. sakni")
            try:
                uanswer2 = float(input()) # Second user answer
            except ValueError:
                print("Nepareizi ievadīta vērtība!")
                sleep(3)
                sys.exit()            
        if uanswer1 == answer3 and answer1 == None: # Izpildas ja ir viena sakne
                Correct = Correct + 2
        elif uanswer1 == answer_list[0] and uanswer2 == answer_list[1]:
                Correct = Correct + 2
    print()
    random = randint(1,2)
    if random == 1:
        V = -32
        B = 14
        print("Zinams, ka kavdratvienadojuma x²+Bx+V=0 saknes ir −16 un 2.")
        print("Nosaki, kādi ir koeficienti B un V! (Ievadiet mazako sakni pirmo)")
        answ1 = input("Ievadiet pirmo koeficentu: ")
        answ2 = input("Ievadiet otro koeficentu: ")
        if int(answ1) == V:
            Correct = Correct +1
        if int(answ2) == B:
            Correct = Correct + 1
    else:
        N = -64
        A = 12
        print("Zināms, ka kvadrātvienādojuma x²+Ax+N=0 saknes ir −16 un 4.")
        print("Nosakiet, kādi ir koeficienti A un N! (Ievadiet mazako sakni pirmo)")
        answ1 = input("Ievadiet pirmo koefientu: ")
        answ2 = input("Ievadiet otro koeficentu: ")
        if int(answ1) == N:
            Correct = Correct +1
        if int(answ2) == A:
            Correct = Correct + 1 
    
    print("Jūs no 10 balem ieguvat",Correct,"balles.")
    print()
    question = input("Vai velaties meginat visu darbu no jauna? Y/N ")
    question2 = jautajums(question)
    if question2 == True:
        question3 = True
        os.system("cls")
