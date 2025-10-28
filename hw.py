class StringReverse:
    def __init__(self, text):
        self.__text = text
    def reverse_words(self):
        words = self.__text.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words
    def __str__(self):
        return f"Reversed string: {self.reverse_words()}"
if __name__ == "__main__":
    s = StringReverse("hi")
    print(s)
    print("hi:", s._StringReverse__text)
    print("hi:", s.reverse_words())
