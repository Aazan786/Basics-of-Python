#Main file from where we run our code

#importing classes from modules
from Question_data import Data
from Questions_model import Question
from Quiz_Function import QuizBrain

# Creating list which store objects of Question class
# This objects in list store two attributes text and answer
Question_bank= []

#Traversing Data from Data list to store objects in Question bank list.
for question  in Data:
    question_text = question["text"]
    question_answer = question["answer"]

    #Creating object of question class
    new_question = Question(question_text, question_answer)
    Question_bank.append(new_question)

#creating object of Quizbrain class
quiz = QuizBrain(Question_bank)
while quiz.still_has_question():
    quiz.next_question()
 
print("You have Completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_no}")
