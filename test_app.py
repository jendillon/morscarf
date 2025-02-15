import unittest
import numpy as np
from app import text_to_morse, morse_to_stripes, visualize_stripes, stripes_to_pattern

SOS_STRIPES = [10., 1., 10., 1., 10., 1.,# ... (s)
                        1., 1., # Space between letters
                        10., 10., 10., 1., 10., 10., 10., 1., 10., 10., 10., 1., # --- (o)
                        1., 1., # Space between letters
                        10., 1., 10., 1., 10., 1.,] # ... (s)

class TestMorseCodeTranslator(unittest.TestCase):

    def test_should_handle_single_character(self):
        self.assertEqual(text_to_morse("a"), ".-", "Failed for a")

    def test_should_handle_upper_and_lower_case(self):
        self.assertEqual(text_to_morse("SOS"), "... --- ...", "Failed for SOS")
        self.assertEqual(text_to_morse("sos"), "... --- ...", "Failed for sos")
        
    def test_should_handle_numbers(self):    
        self.assertEqual(text_to_morse("123"), ".---- ..--- ...--", "Failed for 123")
        
    def test_should_handle_spaces(self):        
        self.assertEqual(text_to_morse("HELLO WORLD"), 
                         ".... . .-.. .-.. ---   .-- --- .-. .-.. -..", 
                         "Failed for HELLO WORLD")
        
    def test_should_handle_invalid_characters(self):
        # Test for ValueError when invalid characters are present
        with self.assertRaises(ValueError):
            text_to_morse("%$&@*")

    def test_should_handle_empty_string(self):
        self.assertEqual(text_to_morse(""), "", "Failed for empty string")

    def test_should_handle_special_characters(self):
        self.assertEqual(text_to_morse(",.?/-()"), 
                         "--..-- .-.-.- ..--.. -..-. -....- -.--. -.--.-", 
                         "Failed for ,.?/-()")

    def test_morse_to_stripes(self):
        print("Testing morse_to_stripes")
        np.testing.assert_array_equal(morse_to_stripes("... --- ..."), 
                        np.array(SOS_STRIPES),
                        "Failed for SOS") 

        hello_world_expected = [
            10., 1., 10., 1., 10., 1., 10., 1., # .... (h)
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
            10., 10., 10., 1., 10., 1., 10., 1.] # -.. (d)       
            
        np.testing.assert_array_equal(
            morse_to_stripes(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."),                                       
            np.array(hello_world_expected),
            "Failed for HELLO WORLD")

    def test_should_handle_single_solid_stripe(self):
        expected_pattern = [
            "In color 1, Make a sl kt. Chain 20.\n",
            "In color 1, Sc 20 across.\n Ch 1. Turn.\n",
            "Repeat previous row 2 more time(s).\n"
        ]
        actual_pattern = stripes_to_pattern([10., 10., 10.])
        np.testing.assert_array_equal(actual_pattern, 
                                      expected_pattern, 
                                      "Failed for single solid stripe")

    def test_should_handle_sos(self):
        print("Testing sos pattern")
        expected_pattern = ["In color 1, Make a sl kt. Chain 20.\n",
                        "In color 1, Sc 20 across.\n Ch 1. Turn.\n",
                        "In color 2, Sc 20 across.\n Ch 1. Turn.\n",
                        "In color 1, Sc 20 across.\n Ch 1. Turn.\n",
                        "In color 2, Sc 20 across.\n Ch 1. Turn.\n",
                        "In color 1, Sc 20 across.\n Ch 1. Turn.\n",
                        "In color 2, Sc 20 across.\n Ch 1. Turn.\n",
                        "Repeat previous row 2 more time(s).\n",
                        "In color 1, Sc 20 across.\n Ch 1. Turn.\n",
                        "Repeat previous row 2 more time(s).\n",
                        "In color 2, Sc 20 across.\n Ch 1. Turn.\n",
                        "In color 1, Sc 20 across.\n Ch 1. Turn.\n",
                        "Repeat previous row 2 more time(s).\n",
                        "In color 2, Sc 20 across.\n Ch 1. Turn.\n",
                        "In color 1, Sc 20 across.\n Ch 1. Turn.\n",
                        "Repeat previous row 2 more time(s).\n",
                        "In color 2, Sc 20 across.\n Ch 1. Turn.\n",
                        "Repeat previous row 2 more time(s).\n",
                        "In color 1, Sc 20 across.\n Ch 1. Turn.\n",
                        "In color 2, Sc 20 across.\n Ch 1. Turn.\n",
                        "In color 1, Sc 20 across.\n Ch 1. Turn.\n",
                        "In color 2, Sc 20 across.\n Ch 1. Turn.\n",
                        "In color 1, Sc 20 across.\n Ch 1. Turn.\n",
                        "In color 2, Sc 20 across.\n Ch 1. Turn.\n"]

        np.testing.assert_array_equal(stripes_to_pattern(SOS_STRIPES), 
                                      expected_pattern, 
                                      "Failed for SOS")

    def test_visualize_stripes(self):
        stripes = np.array([1, 0, 1, 0, 1])
        plot_url = visualize_stripes(stripes)
        self.assertTrue(plot_url.startswith("iVBORw0KGgoAAAANSUhEUgAA"), 
                        "Failed to generate plot")

if __name__ == "__main__":
    unittest.main()