from data import question_data
from question_model import Question, QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))


quiz = QuizBrain(question_bank)

while quiz.still_has_q():

    quiz.next_q()
    print(f"You have completed the quiz and your final score is {quiz.score}/{len(question_bank)}")







