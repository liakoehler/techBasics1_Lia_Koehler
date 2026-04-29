import random

# === Datenbank: Outfits nach Anlässen ===
outfits = {
    "uni": {
        "formal": {
            "oberteil": ["Hemd", "Polo-Shirt", "Bluse"],
            "hose": ["Anzughose", "Chino", "Jeans (formal)"],
            "schuhe": ["Schnürschuhe", "Lederschuhe", "Ballerinas"],
            "jacke": ["Blazer", "Weste", "Leichter Mantel"],
            "accessoires": ["Brille", "Uhr", "Tasche"]
        },
        "casual": {
            "oberteil": ["T-Shirt", "Pullover", "Leichtes Hemd"],
            "hose": ["Jeans", "Chino", "Shorts (im Sommer)"],
            "schuhe": ["Sneaker", "Ballerinas", "Sandalen"],
            "jacke": ["Jeansjacke", "Windbreaker", "Leichter Pullover"],
            "accessoires": ["Rucksack", "Sonnenbrille", "Kopfbedeckung"]
        }
    },
    "präsentation": {
        "formal": {
            "oberteil": ["Hemd", "Business-Bluse", "Formales Hemd"],
            "hose": ["Anzughose", "Chino (dunkel)"],
            "schuhe": ["Lederschuhe", "Schnürschuhe"],
            "jacke": ["Blazer", "Mantel"],
            "accessoires": ["Uhr", "Tasche", "Brille"]
        },
        "semi-formal": {
            "oberteil": ["Polo-Shirt", "Leichtes Hemd"],
            "hose": ["Chino", "Anzughose"],
            "schuhe": ["Sneaker (schlicht)", "Schnürschuhe"],
            "jacke": ["Leichter Blazer", "Weste"],
            "accessoires": ["Tasche", "Uhr"]
        }
    },
    "cafe-arbeit": {
        "casual": {
            "oberteil": ["T-Shirt", "Pullover", "Leichtes Hemd"],
            "hose": ["Jeans", "Chino", "Leggings"],
            "schuhe": ["Sneaker", "Ballerinas", "Sandalen"],
            "jacke": ["Jeansjacke", "Pullover"],
            "accessoires": ["Rucksack", "Kopfhörer", "Tasse"]
        },
        "cozy": {
            "oberteil": ["Wollpullover", "Kapuzenpulli"],
            "hose": ["Jeans", "Leggings"],
            "schuhe": ["Slipper", "Sneaker"],
            "jacke": ["Weste", "Leichter Mantel"],
            "accessoires": ["Kopfhörer", "Tasche", "Buch"]
        }
    },
    "date": {
        "romantisch": {
            "oberteil": ["Seidenbluse", "Top mit Spitze", "Hemd mit Muster"],
            "hose": ["Stoffhose", "Rock", "Jeans (schön)"],
            "schuhe": ["Pumps", "Stiefeletten", "Schuhe mit Absatz"],
            "jacke": ["Lederjacke", "Mantel"],
            "accessoires": ["Halskette", "Ohrringe", "Tasche"]
        },
        "casual-chic": {
            "oberteil": ["T-Shirt mit Design", "Pullover"],
            "hose": ["Jeans", "Chino"],
            "schuhe": ["Sneaker", "Stiefeletten"],
            "jacke": ["Leichter Mantel", "Jeansjacke"],
            "accessoires": ["Sonnenbrille", "Rucksack"]
        }
    },
    "sport": {
        "aktiv": {
            "oberteil": ["Laufshirt", "Sport-T-Shirt", "Funktionshemd"],
            "hose": ["Laufhose", "Shorts", "Trainingshose"],
            "schuhe": ["Laufschuhe", "Basketballschuhe"],
            "jacke": ["Windjacke", "Funktionsjacke"],
            "accessoires": ["Sportuhr", "Rucksack", "Trinkflasche"]
        }
    }
}


# === Funktion: Anlass erkennen und Outfit vorschlagen ===
def suggest_outfit():
    print("\n" + "=" * 50)
    print("✨ Willkommen beim Outfit-Generator! ✨")
    print("=" * 50)

    # Benutzer-Eingabe
    anlass = input(
        "\nFür welchen Anlass brauchst du ein Outfit? (z. B. Uni, Präsentation, Café-Arbeit, Date, Sport): ").strip().lower()

    # Optionale Eingabe: Stilrichtung
    stil = input(
        "Wie formell soll es sein? (formal / semi-formal / casual / cozy / romantisch / aktiv) [Enter für Standard]: ").strip().lower()
    if stil == "":
        stil = "casual"  # Standardwert

    # Optionale Eingabe: Wetter (für Erweiterung)
    wetter = input("Wie ist das Wetter? (warm / kalt / regnerisch / mild) [Enter für Standard]: ").strip().lower()
    if wetter == "":
        wetter = "mild"

    # Anlass erkennen und Outfit vorschlagen
    if anlass in ["uni", "präsentation", "cafe-arbeit", "date", "sport"]:
        if stil in outfits[anlass]:
            outfit = outfits[anlass][stil]
        else:
            # Falls Stil nicht existiert, nimm ersten Eintrag
            stil = list(outfits[anlass].keys())[0]
            outfit = outfits[anlass][stil]
            print(f"⚠️  Stil '{stil}' nicht verfügbar. Verwende stattdessen: {stil}.")
    else:
        print(f"❌ Anlass '{anlass}' ist nicht in der Datenbank. Versuche: Uni, Präsentation, Café-Arbeit, Date, Sport.")
        return

    # Zufällige Auswahl aus den Kategorien
    print(f"\n🎯 Vorgeschlagenes Outfit für: **{anlass.title()}** ({stil.title()})")
    print("-" * 40)
    for kategorie, items in outfit.items():
        item = random.choice(items)
        print(f"• {kategorie.title()}: {item}")

    # Zusätzliche Hinweise
    if wetter == "kalt":
        print("❄️  Tipp: Trage eine warme Jacke oder einen Mantel!")
    elif wetter == "regnerisch":
        print("☔  Tipp: Regenjacke und wasserfeste Schuhe nicht vergessen!")
    elif wetter == "warm":
        print("☀️  Tipp: Leichte Materialien und luftige Kleidung wählen!")

    # Option: Mehr Outfits vorschlagen
    weiter = input("\nMöchtest du ein weiteres Outfit vorschlagen lassen? (ja/nein): ").strip().lower()
    if weiter in ["ja", "j", "yes"]:
        suggest_outfit()
    else:
        print("\n🎉 Viel Erfolg mit deinem Outfit! Bis zum nächsten Mal! 👗👕")


# === Start des Programms ===
if __name__ == "__main__":
    suggest_outfit()
