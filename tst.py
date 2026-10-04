import time

massive_delay = 3.5
long_delay = 2.5
short_delay = 1.5

print("CIAO FRA!")
time.sleep(long_delay)
input("Come stai? [Bene/Male] ")
print("Dai, sono contenta")
time.sleep(short_delay)
print("Il messaggio non cambiava in base alla risposta, non ho ancora imparato gli if. Guarda il codice")
time.sleep(long_delay)
print("\n\tinput(\"Come stai? [Bene/Male] \")\n\tprint(\"Dai, sono contenta\")\n")
time.sleep(massive_delay)
print("Vuoi picchiarmi eh?")
time.sleep(long_delay)
print("Comunque...")
time.sleep(short_delay)
print("...ti volevo chiedere...")
time.sleep(short_delay)
print("...ti andrebbe di uscire?")
time.sleep(long_delay)
while True:
    response = input("Valuta bene la risposta. Puoi inserire \"SI\" o \"NO\". Prova ad inserire NO -> ")
    if(response == "NO" or response == "no" or response == "No"):
        break
    print("Hey, non barare!")
print("No, questa risposta non va bene")
time.sleep(long_delay)
print("Ok, scherzavo. Ora seriamente, ti va di uscire?")
while True:
    response = input()
    if(response == "SI" or response == "Si" or response == "si"):
        break
    print("Questa risposta non va bene. Riprova ")
print("OK! Va facciamo martedì? o martedì prossimo? Ritorna in chat però, non ho più risposte... :(")