class Question(object):
    def __init__ (self, category, question, correct_ans, wrong_ans):
        self.category = category
        self.question = question
        self.correct_ans = correct_ans
        self.wrong_ans = wrong_ans