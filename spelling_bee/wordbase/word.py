class SpellingBeeWord:
    def __init__(self, word, difficulty, pronunciation, origin, definition, part_of_speech, example_sentence):
        self.word = word
        self.difficulty = difficulty
        self.pronunciation = pronunciation
        self.origin = origin
        self.definition = definition
        self.part_of_speech = part_of_speech
        self.example_sentence = example_sentence

# Example usage
if __name__ == "__main__":
    word = SpellingBeeWord(
        word="example",
        difficulty="easy",
        pronunciation="ig-ZAM-puhl",
        origin="Latin",
        definition="A thing characteristic of its kind or illustrating a general rule.",
        part_of_speech="Noun",
        example_sentence="This is an example sentence."
    )