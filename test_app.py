import unittest
import numpy as np
from app import text_to_morse, morse_to_stripes, visualize_stripes

class TestMorseCodeTranslator(unittest.TestCase):

    def test_text_to_morse(self):
        self.assertEqual(text_to_morse("a"), ".-")
        self.assertEqual(text_to_morse("SOS"), "... --- ...")
        self.assertEqual(text_to_morse("sos"), "... --- ...")
        self.assertEqual(text_to_morse("HELLO"), ".... . .-.. .-.. ---")
        self.assertEqual(text_to_morse("123"), ".---- ..--- ...--")
        self.assertEqual(text_to_morse("HELLO WORLD"), ".... . .-.. .-.. ---   .-- --- .-. .-.. -..")
        
        # Test for ValueError when invalid characters are present
        with self.assertRaises(ValueError):
            text_to_morse("%$&@*")

    def test_morse_to_stripes(self):
        np.testing.assert_array_equal(morse_to_stripes("... --- ..."), 
                                      np.array([10., 1., 10., 1., 10., 1.,# ...
                                                1., 1., # Space
                                                10., 10., 10., 1., 10., 10., 10., 1., 10., 10., 10., 1., # ---
                                                1., 1., # Space                                                
                                                10., 1., 10., 1., 10., 1.,])) # ...
        # np.testing.assert_array_equal(morse_to_stripes(".... . .-.. .-.. ---"), np.array([1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1]))
        # np.testing.assert_array_equal(morse_to_stripes(".---- ..--- ...--"), np.array([1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1]))
        # np.testing.assert_array_equal(morse_to_stripes(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."), np.array([1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1]))

    def test_visualize_stripes(self):
        stripes = np.array([1, 0, 1, 0, 1])
        plot_url = visualize_stripes(stripes)
        self.assertTrue(plot_url.startswith("iVBORw0KGgoAAAANSUhEUgAA"))

if __name__ == '__main__':
    unittest.main()