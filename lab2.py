import re

class TextProcessor:
    def __init__(self, text: str, vowels: str):
        if text is None:
            raise ValueError("Об'єкт тексту не може бути.")
        self.text_builder = list(text)
        self.vowels = vowels

    def sort_vowel_words(self):
        try:
            text = "".join(self.text_builder)
            pattern = r"[a-zA-Zа-яА-ЯіїєґІЇЄҐ]+(?:['’`][a-zA-Zа-яА-ЯіїєґІЇЄҐ]+)*"
            words = re.findall(pattern, text)

            if not words:
                return "Помилка: Ви ввели порожній рядок або текст без слів."
            unique_vowel_words = {}
            for word in words:
                lower_word = word.lower()
                if lower_word[0] in self.vowels:
                    if lower_word not in unique_vowel_words:
                        unique_vowel_words[lower_word] = word

            result_list = list(unique_vowel_words.values())

            if not result_list:
                return "Слів, що починаються на голосну, не знайдено."

            sorted_words = sorted(
                result_list,
                key=lambda x: x[1].lower() if len(x) > 1 else ""
            )

            return sorted_words

        except Exception as e:
            return f"Виникла помилка: {e}"

class Executor:
    @staticmethod
    def run():
        print("--- Програма сортування ---")

        try:
            user_input = input("Введіть текст: ").strip()
            vowels = "аеєиіїоуюяaeiouy"

            if not user_input:
                print("Ви нічого не ввели.")
                return

            processor = TextProcessor(user_input, vowels)
            result = processor.sort_vowel_words()

            print("\nРезультат:")
            if isinstance(result, list):
                print(", ".join(result))
            else:
                print(result)

        except KeyboardInterrupt:
            print("\nПрограму перервано.")
        except Exception as e:
            print(f"Критична помилка: {e}")
        finally:
            print("\n" + "=" * 40)
            print("Робота завершена.")


if __name__ == "__main__":
    Executor.run()