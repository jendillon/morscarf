from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def translate_single_letter_to_units(letter):
    morse_letter = ""

    try:
        morse_letter = MORSE_CODE_DICT[letter.upper()]
    except KeyError:
        return ""  # Not Translatable... Consider making red bar?

    unit_letter = []

    for c in morse_letter:
        if c == '-':
            unit_letter.append("111")  # "Long" dash
        else:
            unit_letter.append("1")  # "Short" dot

        unit_letter.append("0")  # Space between dots and dashes in the same letter

    return ''.join(unit_letter).rstrip('0')

def translate_phrase_to_units(phrase):
    unit_phrase = []

    for c in phrase:
        if c == ' ':
            unit_phrase.append("0000")  # Space between words
            # Note: This should be 7 units, but we've already appended 3 for the space between letters.
        else:
            unit_phrase.append(translate_single_letter_to_units(c))
            unit_phrase.append("000")  # Space between letters

    return ''.join(unit_phrase).rstrip('0')

# def main():
#     import sys

#     while True:
#         print("Enter a phrase to translate to Morse Code:")
#         phrase = input()
#         # phrase = sys.argv[1]
#         if phrase == "":
#             break
#         translated_units = translate_phrase_to_units(phrase)
#         print(translated_units)
#         phrase = ""

# if __name__ == "__main__":
#     main()


class MorseCodeTranslator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Morse Code Translator')

        layout = QVBoxLayout()

        self.label = QLabel('Enter a phrase to translate to Morse Code:')
        layout.addWidget(self.label)

        self.entry = QLineEdit(self)
        layout.addWidget(self.entry)

        self.button = QPushButton('Translate', self)
        self.button.clicked.connect(self.translate_phrase)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def translate_phrase(self):
        phrase = self.entry.text()
        translated_units = translate_phrase_to_units(phrase)
        QMessageBox.information(self, 'Translated Morse Code', translated_units)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    translator = MorseCodeTranslator()
    translator.show()
    sys.exit(app.exec_())