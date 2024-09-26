from IHK_Notenberechnung import berechne_prozentwert,ermittle_note

def test_ermittle_note():
    assert ermittle_note(95) == "Sehr Gut!"
    assert ermittle_note(85) == "Gut!"
    assert ermittle_note(70) == "Befriedigend!"
    assert ermittle_note(55) == "Ausreichend!"
    assert ermittle_note(40) == "mangelhaft"

def test_zero_maximale_punkte():
    try:
        berechne_prozentwert(50, 0)
    except ValueError as e:
        if str(e) == "Fehler! Maximale Punkte muessen groeßer als 0 sein":
           print("Test klappt!")

def test_berechne_prozentwert():
    assert berechne_prozentwert(50, 100) == 50.0
    assert berechne_prozentwert(92, 100) == 92.0
    assert berechne_prozentwert(0, 100) == 0.0
    assert berechne_prozentwert(30, 100) == 30.0

