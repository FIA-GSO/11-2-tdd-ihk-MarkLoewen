def berechne_prozentwert(erreichtepunkte, maximalepunkte):

    if erreichtepunkte > maximalepunkte:
        raise ValueError("Fehler! Erreichte Punkte duerfen nicht groeßer als maximale Punkte sein")
    if maximalepunkte <= 0:
        raise ValueError ("Fehler! Maximale Punkte muessen groeßer als 0 sein")
    if erreichte_punkte <= 0:
        raise ValueError ("Fehler! Erreichte Punkte koennen nicht 0 oder weniger sein")
    return (erreichtepunkte / maximalepunkte) * 100

def ermittle_note(prozentwert):

    if prozentwert >= 92:
        return "Sehr Gut!"
    elif prozentwert >= 81:
        return "Gut!"
    elif prozentwert >= 67:
        return "Befriedigend!"
    elif prozentwert >= 50:
        return "Ausreichend!"
    else:
        return "mangelhaft"

erreichte_punkte = float(input("Bitte die erreichten Punkte eingeben: "))
maximale_punkte = float(input("Bitte die maximalen Punkte eingeben: "))


prozentwert = berechne_prozentwert(erreichte_punkte, maximale_punkte)
print(f"Du hast {prozentwert}% erreicht.")

note = ermittle_note(prozentwert)
print(f"Deine Note ist: {note}")


