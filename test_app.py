import unittest
import numpy as np
from app import text_to_morse, morse_to_stripes, visualize_stripes

class TestMorseCodeTranslator(unittest.TestCase):

    def test_should_handle_single_character(self):
        self.assertEqual(text_to_morse("a"), ".-")

    def test_should_handle_upper_and_lower_case(self):
        self.assertEqual(text_to_morse("SOS"), "... --- ...")
        self.assertEqual(text_to_morse("sos"), "... --- ...")
        
    def test_should_handle_numbers(self):    
        self.assertEqual(text_to_morse("123"), ".---- ..--- ...--")
        
    def test_should_handle_spaces(self):        
        self.assertEqual(text_to_morse("HELLO WORLD"), ".... . .-.. .-.. ---   .-- --- .-. .-.. -..")
        
    def test_should_handle_invalid_characters(self):
        # Test for ValueError when invalid characters are present
        with self.assertRaises(ValueError):
            text_to_morse("%$&@*")

    def test_should_handle_empty_string(self):
        self.assertEqual(text_to_morse(""), "")

    def test_should_handle_special_characters(self):
        self.assertEqual(text_to_morse(",.?/-()"), "--..-- .-.-.- ..--.. -..-. -....- -.--. -.--.-")

    def test_morse_to_stripes(self):
        print("Testing morse_to_stripes")
        sos_expected = [10., 1., 10., 1., 10., 1.,# ... (s)
                        1., 1., # Space between letters
                        10., 10., 10., 1., 10., 10., 10., 1., 10., 10., 10., 1., # --- (o)
                        1., 1., # Space between letters
                        10., 1., 10., 1., 10., 1.,] # ... (s)
        
        np.testing.assert_array_equal(morse_to_stripes("... --- ..."), 
                        np.array(sos_expected)) 

        hello_world_expected = [10., 1., 10., 1., 10., 1., 10., 1., # .... (h)
                        1., 1., # Space between letters
                        10., 1., # . (e)
                        1., 1., # Space between letters
                        10., 1., 10., 10., 10., 1., 10., 1., 10., 1., # .-.. (l)
                        1., 1., # Space between letters
                        10., 1., 10., 10., 10., 1., 10., 1., 10., 1., # .-.. (l)
                        1., 1., # Space between letters
                        10., 10., 10., 1., 10., 10., 10., 1., 10., 10., 10., 1., # --- (o)
                        1., 1., 1., 1., 1., 1., # Space between words
                        10., 1., 10., 10., 10., 1., 10., 10., 10, 1., # .-- (w)
                        1., 1., # Space between letters
                        10., 10., 10., 1., 10., 10., 10., 1., 10., 10., 10., 1., # --- (o)
                        1., 1., # Space between letters                        
                        10., 1., 10., 10., 10., 1., 10., 1., # .-. (r)
                        1., 1., # Space between letters
                        10., 1., 10., 10., 10., 1., 10., 1., 10., 1., # .-.. (l)
                        1., 1., # Space between letters
                        10., 10., 10., 1., 10., 1., 10., 1., # -.. (d)       
                        ]

        np.testing.assert_array_equal(morse_to_stripes(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."),                                       
                        np.array(hello_world_expected))

    def test_visualize_stripes(self):
        print("Testing visualize_stripes")
        stripes = np.array([1, 0, 1, 0, 1])
        plot_url = visualize_stripes(stripes)
        self.assertTrue(plot_url.startswith("iVBORw0KGgoAAAANSUhEUgAA"))

if __name__ == '__main__':
    unittest.main()