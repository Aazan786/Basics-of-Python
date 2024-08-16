#Create question class for storing Question objects in a list and later pass to Quiz function class.
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer