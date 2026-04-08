import unittest
from lab2 import TextProcessor

class TestTextProcessor(unittest.TestCase):
    def setUp(self):
        self.vowels = "аеєиіїоуюяaeiouy"

    def test_standard_sorting(self):
        text = "apple orange ant eat"
        processor = TextProcessor(text, self.vowels)
        result = processor.sort_vowel_words()
        self.assertEqual(result, ["eat", "ant", "apple", "orange"])

    def test_ukrainian_and_apostrophe(self):
        text = "яблуко ім'я огірок око"
        processor = TextProcessor(text, self.vowels)
        result = processor.sort_vowel_words()
        self.assertEqual(result, ["яблуко", "огірок", "око", "ім'я"])

    def test_uniqueness(self):
        text = "Apple apple APPLE"
        processor = TextProcessor(text, self.vowels)
        result = processor.sort_vowel_words()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].lower(), "apple")

    def test_single_letter_words(self):
        text = "а апельсин"
        processor = TextProcessor(text, self.vowels)
        result = processor.sort_vowel_words()
        self.assertEqual(result, ["а", "апельсин"])

    def test_no_vowels_found(self):
        text = "мир праця батон"
        processor = TextProcessor(text, self.vowels)
        result = processor.sort_vowel_words()
        self.assertEqual(result, "Слів, що починаються на голосну, не знайдено.")

    def test_empty_input(self):
        processor = TextProcessor("", self.vowels)
        result = processor.sort_vowel_words()
        self.assertEqual(result, "Помилка: Ви ввели порожній рядок або текст без слів.")

    def test_none_input(self):
        with self.assertRaises(ValueError):
            TextProcessor(None, self.vowels)

if __name__ == "__main__":
    unittest.main()