class QA:

    def greet(self):
        name = str(input(" Enter your name:\n"))
        print(f"Welcome {name}, to the best madlip")

    def questions(self):
        questionList = {"a": 'ADJ', "b": 'NOUN', "c": 'NOUN (PLURAL)', "d": 'NOUN', "e": 'PLACE', "f": 'ADJECTIVE',
                        "g": 'NOUN'}
        for index in questionList:
            questionList[index] = input(f"Please enter a {questionList[index]}")
        return questionList

    def output(self):
        answered = self.questions()
        print("Be kind to your" + str(answered["a"]) + " footed" + str(answered["a"]) + "For a duck may be somebody`s" + str(answered["c"])+ "Be kind to your" + str(answered["d"]) + " in " + str(answered["e"]) + "Where the weather is always" + str(answered["f"]) + ". You may think that this is the" + str(answered["g"]) + ", Well it is.")

