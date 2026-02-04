import datetime

def gauti_laika():
    # Graziname dabartini laika teksto pavidalu
    dabar = datetime.datetime.now()
    return dabar.strftime("%Y-%m-%d %H:%M:%S")

def sveikintis(vardas):
    laikas = gauti_laika()
    print(f"Sveikas, {vardas}!")
    print(f"Dabar yra: {laikas}")
    print("GitHub ryšys veikia puikiai.")

if __name__ == "__main__":
    # Galite pakeisti varda i savo
    naudotojas = "Programuotojas"
    sveikintis(naudotojas)