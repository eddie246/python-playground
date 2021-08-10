class QuizBrain():
  def __init__(self, q_list):
    self.q_num = 0
    self.q_list = q_list
    self.score = 0

  def next(self):
    question = self.q_list[self.q_num]
    self.q_num += 1
    user_input = input(f"Q.{self.q_num}: {question.text} (true/false): ")
    self.check_answer(user_input, question.answer)
  
  def still_has_questions(self):
    return self.q_num < len(self.q_list)

  def check_answer(self, user_input, correct_answer):
    if user_input.lower() == correct_answer.lower():
      print('You got it right!')
      self.score += 1
    else:
      print("That's wrong.")
    print(f"The correct answer is {correct_answer}")
    print(f"Your current score is: {self.score}/{self.q_num}")
    print('\n')
