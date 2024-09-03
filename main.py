# Ordstatistik
# Din uppgift är att läsa in text från filen som är angiven.
# Därefter ska ditt program räkna ut följande:
# - Antal ord
# - Mest frekventa ord
# - Genomsnittlig ordlängd
# Gör en funktion för varje.

# Bonus, gör en i taget, skapa en funktion för varje: 
# - Längsta och kortaste ordet - om det finns flera, bestäm själv om du skriver ut ett eller flera
# - Räkna antalet unika ord (alltså ord som bara förekommer en gång)

from collections import Counter

def read_from_file(path: str):
    """Reads a file with the given parameter path and returns the file as a list of strings, split on newline (\n).

    Args:
        path (str): the path of the readable file

    Returns:
        list(str): list of strings
    """
    with open(path, "r" ,encoding="utf-8") as f:
        return f.readlines()
    
def ordnatill(sentences):
    ord = []
    for u in sentences:
        u = u.strip().replace(",", "").replace(".", "").replace("-", "").lower() # Tar bort "-" då det inte är ett ord
        ord.extend(u.split()) # Extend fungerar som append fast lägger till alla ord induvelt (Vilket gör att det inte blir en lista i en lista) - https://www.geeksforgeeks.org/python-list-extend-method/
    return ord

def antalord(ord):
    return len(ord)

def frekventa(ord):
    u = Counter(ord) # - https://stackabuse.com/count-number-of-word-occurrences-in-list-python/
    return max(u, key=u.get) # Tar ut ordet som uppkommer felst gånnger

def ordlängd(ord):
    längd = 0
    for u in ord:
        längd += len(u)
    return f'{längd/antalord(ord):.2f}'
        
def main():
    sentences = read_from_file("en_resa_genom_svenska_skogen.txt")
    ord = ordnatill(sentences)
    print(antalord(ord))
    print(frekventa(ord))
    print(ordlängd(ord))

if __name__ == "__main__":
    main()