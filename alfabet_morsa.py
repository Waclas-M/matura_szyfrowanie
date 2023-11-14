class Morse_Code:
    alfabet_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "Ą": ".-.-",
    "Ć": "-.-..",
    "Ę": "..-..",
    "Ł": ".-..-",
    "Ń": "--.--",
    "Ó": "---.",
    "Ś": "...-...",
    "Ż": "--..-.",
    "Ź": "--..-",
    }
    def __init__(self, ciag_wejsciowy: str) -> None:
        self.ciag_wejsciowy = ciag_wejsciowy.upper()
        self.ciag_znakow = None
        self.ciag_kodow = None
        if self.ciag_wejsciowy.isalpha():
            self.kierunek = "ASCII-Morse"
            self.ciag_znakow = self.ciag_wejsciowy
            self.zakoduj_morse()
        else:
            self.kierunek = "Morse-ASCII"
            self.ciag_kodow = self.ciag_wejsciowy
            self.odkoduj_morse()

    def zakoduj_morse(self) -> str:
        separator = "#"
        zakodowany_tekst = ""
        for znak in self.ciag_znakow:
            try:
                zakodowany_tekst += Morse_Code.alfabet_morse[znak]
            except KeyError:
                pass
        self.ciag_kodow = zakodowany_tekst

    def odkoduj_morse(self) -> str:

        def odk_znak(kod: str):
            for key, ind in Morse_Code.alfabet_morse.items():
                if kod == ind:
                    return key
                else:
                    return ""
        self.lista_znakow = []
        self.lista_znakow = self.ciag_kodow.split('#')
        odkodowany = ""
        for znak in self.lista_znakow:
            odkodowany += odk_znak(znak)
            self.ciag_znakow = odkodowany
# przykład wywołania
kod_1 = Morse_Code("Linux")
print(kod_1.ciag_znakow)
print(kod_1.ciag_kodow)
print(kod_1.kierunek)
print()
kod_2 = Morse_Code("---#.--.#.#-.#...#---#..-#.-.#-.-.#.#")
print(kod_2.ciag_znakow)
print(kod_2.ciag_kodow)
print(kod_2.kierunek)
