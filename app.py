import io
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import matplotlib
import base64
from io import BytesIO
import numpy as np

matplotlib.use('Agg')  # Required to use Matplotlib without X server
app = Flask(__name__)

MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',    
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---', 
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',  
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',    
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--', 
    'Z': '--..',  '0': '-----',  '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-',  '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.'
}

def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        elif char == ' ':
            morse_code.append(' ')  # Space between words
        else:
            raise ValueError(f"Character '{char}' cannot be translated to Morse code.")
    morse_code = ' '.join(morse_code)
    return morse_code

def morse_to_stripes(morse_code):
    stripes = np.array([])
    for symbol in morse_code:
        if symbol == '.':
            stripes = np.append(stripes, 10) # Skinny stripe
        elif symbol == '-':
            stripes = np.append(stripes, [10, 10, 10])  # Wide stripe
        elif symbol == ' ':
            stripes = np.append(stripes, [1, 1]) # Space between words
            continue
        stripes = np.append(stripes, 1) # Space between stripes    
    return stripes

def visualize_stripes(stripes):
    pixels_per_stripe = 10
    dpi = 100

    fig = plt.figure(figsize=(len(stripes)*pixels_per_stripe/dpi, 2), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    ax.imshow(stripes.reshape(1, -1), cmap='binary', aspect='auto', interpolation='nearest')
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method == "POST":
        phrase = request.form['phrase']
        morse_code = text_to_morse(phrase)
        stripes = morse_to_stripes(morse_code)
        plot_url = visualize_stripes(stripes)
        return render_template("index.html", phrase=phrase, morse_code=morse_code, plot_url=plot_url)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)