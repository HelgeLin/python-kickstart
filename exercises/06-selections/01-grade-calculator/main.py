#!/usr/bin/env python3
"""
Exercise 1: Grade Calculator

Convert numeric scores to letter grades with feedback.
"""

# Write your code here
# 1. Ask user for a score (0-100)
# 2. Convert score to letter grade using if/elif/else:
#    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59
# 3. Provide appropriate feedback for each grade
# 4. Display the grade and feedback

import time
import sys
import random

# -------------------------
# Hjälpfunktioner
# -------------------------
def skrivmaskin(text, delay=0.04):
    """Skriv text bokstav för bokstav."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def generera_fejk_ip():
    """Skapar en trovärdig (men fejk) IP-adress."""
    return f"{random.randint(10, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

def clear_screen():
    """Rensa terminalen (ANSI)."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def animera_monstrade(bredd=40, hojd=10, frames=12, delay=0.08):
    """
    Animerar ett 'coolt mönster' i terminalen: rörliga block och gradientfärg.
    Begränsat antal frames så det inte kör för länge.
    """
    colors = ["\033[95m", "\033[94m", "\033[96m", "\033[92m", "\033[93m", "\033[91m"]
    for f in range(frames):
        clear_screen()
        # skapa en vågform som flyttar sig
        offset = f * 2
        for y in range(hojd):
            line = ""
            for x in range(bredd):
                # beräkna "intensitet" för mönster
                val = (x + offset + (y * 3)) % (bredd // 2)
                if val < 3:
                    # välj färg baserat på val + y
                    color = colors[(val + y) % len(colors)]
                    line += color + "■"  # blocksymbol
                else:
                    line += "\033[90m·"  # dim punkt
            line += "\033[0m"
            print(line)
        # liten footer
        print("\n\033[90mLaddar mystisk diagnostik...\033[0m")
        time.sleep(delay)
    # lämna skärmen någorlunda synlig
    time.sleep(0.25)
    clear_screen()

# -------------------------
# Programlogik
# -------------------------
def main():
    try:
        number = int(input("Skriv en siffra mellan 0-100: "))
    except ValueError:
        # Om användaren skriver text som inte går att konvertera: visa pattern + fel
        animera_monstrade(bredd=48, hojd=12, frames=10, delay=0.06)
        skrivmaskin("\033[91mFel: Ogiltig inmatning (inte en siffra)!\033[0m", 0.06)
        time.sleep(0.5)
        ip = generera_fejk_ip()
        skrivmaskin(f"\033[94mLoggar IP-adress: {ip}\033[0m", 0.07)
        skrivmaskin("\033[90mKontakta systemadministratören om du tror detta är ett misstag.\033[0m", 0.04)
        return

    # Normala betyg
    if 90 <= number <= 100:
        skrivmaskin("\033[92mDu har betyget A\033[0m", 0.04)
    elif 80 <= number <= 89:
        skrivmaskin("\033[96mDu har betyget B\033[0m", 0.04)
    elif 70 <= number <= 79:
        skrivmaskin("\033[94mDu har betyget C\033[0m", 0.04)
    elif 60 <= number <= 69:
        skrivmaskin("\033[93mDu har betyget D\033[0m", 0.04)
    elif 0 <= number <= 59:
        skrivmaskin("\033[91mDu har betyget F\033[0m", 0.04)
    # Ogiltiga värden: animera och visa mystisk IP
    elif number > 100 or number < 0:
        animera_monstrade(bredd=50, hojd=11, frames=14, delay=0.05)
        skrivmaskin("\033[91m⚠ Fel: Otillåtet värde upptäckt...\033[0m", 0.06)
        time.sleep(0.6)
        skrivmaskin("\033[93mAnalyserar intrångsförsök...\033[0m", 0.05)
        time.sleep(0.7)
        ip = generera_fejk_ip()
        skrivmaskin(f"\033[94mLoggar IP-adress: {ip}\033[0m", 0.07)
        time.sleep(0.4)
        skrivmaskin("\033[90mSystemrapport skickad till administration.\033[0m", 0.04)

if __name__ == "__main__":
    main()

