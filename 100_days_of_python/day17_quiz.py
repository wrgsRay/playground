from day17_question_model import Question
from day17_data import question_data
from day17_quiz_brain import QuizBrain

question_bank = [Question(i['question'], i['correct_answer']) for i in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")