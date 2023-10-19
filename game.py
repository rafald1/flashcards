import random
import os


class Game:
    def __init__(self, data):
        self.data = data

    def get_next_word(self, category):
        list_of_words = self.data.fetch_data(key="category", value=category)
        if list_of_words:
            random.shuffle(list_of_words)
            return list_of_words.pop()
        return None

    def mark_word_as_learned(self, id_value):
        self.data.mark_word_as_learned(key="id", value=id_value)

    def reset_progress(self, category):
        self.data.reset_learned_value(key="category", value=category)

    def build_list_of_categories(self):
        return self.data.get_count_of_not_learned_words_by_category()

    @staticmethod
    def pronounce_word(word, language):
        word = word.lstrip("-")  # to avoid an error: say: invalid option
        if language == "es":
            voice = "Mónica"
        elif language == "en":
            voice = "Superstar"
        else:
            print("Error: Available languages to pronounce words: es, en.")
            return
        os.system(f"say -v '{voice}' '{word}'")
