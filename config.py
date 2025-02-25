
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',    
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',  
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',    
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', ',': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

DOT = [10.]
DASH = [10., 10., 10.]
SPACE_LETTER = [1., 1.]
SPACE_STRIPE = [1.]
SPACE_WORD = [1., 1., 1., 1., 1., 1.]

FIRST_ROW = "In color 1, Make a sl kt. Chain 20.\n"
ROW_IN_COLOR_1 = "In color 1, Sc 20 across.\n Ch 1. Turn.\n"
ROW_IN_COLOR_2 = "In color 2, Sc 20 across.\n Ch 1. Turn.\n"
ROW_REPEAT = "Repeat previous row {repeat_row_counter} more time(s).\n"


PATTERN_DOT = "In color {color_1}, add one row\n"
PATTERN_DASH = "In color {color_1}, add three rows \n"
PATTERN_SPACE_LETTER = "In color {color_2}, add two rows. \n"
PATTERN_SPACE_STRIPE = "In color {color_2}, add one row\n"
PATTERN_SPACE_WORD = "In color {color_2}, add six rows\n"