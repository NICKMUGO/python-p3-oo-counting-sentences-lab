class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
            self.value = ""
        else:
            self.value = value

    def is_sentence(self):
        if self.value.endswith("."):
            return True
        return False

    def is_question(self):
        if self.value.endswith("?"):
            return True
        return False

    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        return False

    def count_sentences(self):
        if not self.value:
            return 0

        sentences = self.value.split('.')
        sentences = [s for s in sentences if s]  # Remove empty strings
        return len(sentences)
