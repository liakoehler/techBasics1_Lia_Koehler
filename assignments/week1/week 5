"""
Week 5 - Refactored Outfit Generator
Refactored from Week 2 .

This program suggests an outfit based on:
- Occasion (Anlass)
- Style (Stil)
- Temperature

I used Claude AI for explanation .
"""

import random
import time

# ==================================================
# Constants
# ==================================================

DEFAULT_STYLE = "casual"
VALID_OCCASIONS = ["uni", "präsentation", "cafe-arbeit", "date", "sport"]

# Outfit database
OUTFITS = {
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


# ==================================================
# Functions
# ==================================================

def get_user_input(prompt, default=""):
    """
    Ask the user for input and return the result.
    If the user presses Enter, return the default value.
    """
    user_input = input(prompt).strip().lower()
    if user_input == "":
        return default
    return user_input


def get_outfit(anlass, stil):
    """
    Return the outfit dictionary and the final style.
    If the style is not available, use the first available style.
    """
    if anlass not in OUTFITS:
        return None, None

    if stil not in OUTFITS[anlass]:
        stil = list(OUTFITS[anlass].keys())[0]

    return OUTFITS[anlass][stil], stil


def display_outfit(anlass, stil, outfit):
    """
    Display a randomly generated outfit.
    """
    print(f"\n🎯 Vorgeschlagenes Outfit für: {anlass.title()} ({stil.title()})")
    print("-" * 40)

    for kategorie, items in outfit.items():
        print(f"• {kategorie.title()}: {random.choice(items)}")


def get_temperature_tip(temperature):
    """
    Return a clothing tip based on temperature.
    """
    if -15 <= temperature <= 0:
        return "❄️ Tipp: Trage eine warme Jacke oder einen Mantel!"
    elif 1 <= temperature <= 10:
        return "☔ Tipp: Regenjacke und wasserfeste Schuhe nicht vergessen!"
    elif 11 <= temperature <= 25:
        return "☀️ Tipp: Leichte Materialien und luftige Kleidung wählen!"
    else:
        return "Temperatur ist zu warm oder zu kalt."


def ask_for_temperature():
    """
    Ask the user for a valid temperature and return it as an integer.
    """
    while True:
        user_input = input("Wie hoch ist die Temperatur? ")

        try:
            temperature = int(user_input)
            return temperature
        except ValueError:
            print("Bitte gib eine ganze Zahl ein.")


def show_temperature_tip():
    """
    Ask for temperature and display the matching tip.
    """
    print("Ich gebe dir mal einen Tipp...")
    time.sleep(2)

    while True:
        temperature = ask_for_temperature()
        tip = get_temperature_tip(temperature)
        print(tip)

        if temperature >= -15 and temperature <= 25:
            break


def ask_to_continue():
    """
    Ask the user if they want another outfit suggestion.
    Returns True if yes, otherwise False.
    """
    answer = get_user_input(
        "\nMöchtest du ein weiteres Outfit vorschlagen lassen? (ja/nein): "
    )
    return answer in ["ja", "j", "yes", "y"]


def suggest_outfit():
    """
    Run one complete outfit suggestion.
    """
    print("\n" + "=" * 50)
    print("✨ Willkommen beim Outfit-Generator! ✨")
    print("=" * 50)

    # Get user inputs
    anlass = get_user_input(
        "\nFür welchen Anlass brauchst du ein Outfit? "
        "(Uni, Präsentation, Café-Arbeit, Date, Sport): "
    )

    stil = get_user_input(
        "Wie formell soll es sein? "
        "(formal / semi-formal / casual / cozy / romantisch / aktiv) "
        "[Enter für Standard]: ",
        DEFAULT_STYLE
    )

    # Validate occasion
    if anlass not in VALID_OCCASIONS:
        print(
            "\n❌ Dieser Anlass ist nicht verfügbar.\n"
            "Bitte versuche: Uni, Präsentation, Café-Arbeit, Date oder Sport."
        )
        return

    # Get outfit
    outfit, final_style = get_outfit(anlass, stil)

    if stil != final_style:
        print(
            f"⚠️ Stil '{stil}' nicht verfügbar. "
            f"Verwende stattdessen '{final_style}'."
        )

    # Display outfit
    display_outfit(anlass, final_style, outfit)

    # Show weather tip
    show_temperature_tip()


# ==================================================
# Main Function
# ==================================================

def main():
    """
    Main program loop.
    """
    while True:
        suggest_outfit()

        if not ask_to_continue():
            print("\n🎉 Viel Erfolg mit deinem Outfit! Bis zum nächsten Mal! 👗👕")
            break


# ==================================================
# Program Start
# ==================================================

if __name__ == "__main__":
    main()
