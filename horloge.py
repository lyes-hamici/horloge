import time   
from time import strftime
import keyboard



def alarme(t):
    global l2
    l2 = []
    l2.append(t[0])
    l2.append(t[1])
    l2.append(t[2])


def format_heures(t):
    format = int(input("Chossisez un format d'affichage 12 ou 24 :"))
    if format == 12:
        afficher_heure_12(t)
    elif format == 24:
        afficher_heure(t)
    else:
        print("Choix non valide.")
    

def afficher_heure(t):
    print("appuier sur 'q' pour mettre en pause l'horloge")
    run = True
    l = []
    l.append(t[0])
    l.append(t[1])
    l.append(t[2])
    while run :
        time.sleep(1)
        if int(l[2]) < 60 :
            l[2] += 1
        
        if l[0] == l2[0] and l[1] == l2[1] and l[2] == l2[2]:
            print(l[0],":",l[1],":",l[2] ,"Vôtre alarme sonne")
   
                    
        if int(l[2]) > 59:
            l[2] = 0
            l[1] += 1
        



        if int(l[1]) > 59:
            l[1] = 0
            l[0] += 1


        if int(l[0]) == 24 :
            l[0] = 0
        print(f"{l[0]:02d}:{l[1]:02d}:{l[2]:02d}")

        if keyboard.is_pressed("q"):
            print("Pour reprendre appuier sur 'l'")
            keyboard.wait("l")
            
  

def afficher_heure_12(t):
    print("appuier sur 'q' pour mettre en pause l'horloge")
    run = True
    l = []
    l.append(t[0])
    l.append(t[1])
    l.append(t[2])
    while run :
        time.sleep(1)
        if l[0] <= 12:
            if int(l[2]) < 60 :
                l[2] += 1
        
            if l[0] == l2[0] and l[1] == l2[1] and l[2] == l2[2]:
                print(l[0],":",l[1],":",l[2] ,"Vôtre alarme sonne")
    
                        
            if int(l[2]) > 59:
                l[2] = 0
                l[1] += 1
            



            if int(l[1]) > 59:
                l[1] = 0
                l[0] += 1


            if int(l[0]) <12 :
                l[0] = 0
            print(f"{l[0]:02d}:{l[1]:02d}:{l[2]:02d} AM")

        else :
            if int(l[2]) < 60 :
                l[2] += 1
        
            if l[0] == l2[0] and l[1] == l2[1] and l[2] == l2[2]:
                print(l[0],":",l[1],":",l[2] ,"Vôtre alarme sonne")
    
                        
            if int(l[2]) > 59:
                l[2] = 0
                l[1] += 1
            



            if int(l[1]) > 59:
                l[1] = 0
                l[0] += 1


            if int(l[0]) < 12 :
                l[0] = 0
            print(f"{l[0]%12:02d}:{l[1]:02d}:{l[2]:02d} PM")

        if keyboard.is_pressed("q"):
            print("Pour reprendre appuier sur 'l'")
            keyboard.wait("l")


alarme((16,30,10))        
format_heures((12,59,50))