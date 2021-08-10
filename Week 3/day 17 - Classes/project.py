from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
  question_bank.append(Question(question["text"], question["answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
  quiz_brain.next()

print(f'You completed the quiz. Your final score is {quiz_brain.score/quiz_brain.q_num}')