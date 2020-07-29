# ToDo:
# 1. [X] Access the OpenTDB API and get questions
# 2. [X] Read the JSON file and out as seperate questions
# 3. [X] Ask each question and check answer, keeping score
# 4. [ ] Provide result from the questions
# 5. [ ] Allow user to choose number of questions
# 6. [ ] Allow user to change the difficulity of questions
# 7. [ ] Allow user to choose the category of the questions

from questions import Question
import requests
import json
import html
import random

def request_questions(ques_nos):
    session_key = requests.get("https://opentdb.com/api_token.php?command=request")
    token = json.loads(session_key.text)
    token = token["token"]                      # get the session token, to prevent same questions

    URL = "https://opentdb.com/api.php?amount=" + ques_nos + "&type=multiple&token=" + token
    response = requests.get(URL)                # get a set of random questions

    return response

def get_questions(data_from_opentdb):   
    questions_tdb = json.loads(response.text)
    questions_tdb = questions_tdb["results"]

    unescape = html.unescape

    question_list = []

    for question_dict in questions_tdb:
        category = unescape(question_dict["category"])
        question = unescape(question_dict["question"])
        correct_ans = unescape(question_dict["correct_answer"])
        wrong_ans = unescape(question_dict["incorrect_answers"])

        question_list.append(Question(category, question, correct_ans, wrong_ans))
    
    return question_list

if __name__ == "__main__":
    no_of_ques = input("How many questions would like (choose between 1 - 50)? ")
    if no_of_ques not in range(1, 50):
        print("Your number was invalid, pleas try again")
        exit()

    response = request_questions(no_of_ques)
    question_list = get_questions(response)

    num_right = 0

    for i in range(len(question_list)):
        print("Q" + str(i+1) + ": " + question_list[i].question)
        
        answers = question_list[i].wrong_ans
        answers.append(question_list[i].correct_ans)
        random.shuffle(answers)                     # randomise the order of the answers

        print("A: " + answers[0])
        print("B: " + answers[1])
        print("C: " + answers[2])
        print("D: " + answers[3])

        user_ans = input("Make your selection: ")

        if user_ans not in ("A", "a", "B", "b", "C", "c", "D", "d"):
            print ("Try again:")
            user_ans = input("Make your selection: ")

        if user_ans in ("A", "a"):
            if answers[0] == question_list[i].correct_ans:
                num_right = num_right + 1
        elif user_ans in ("B", "b"):
            if answers[1] == question_list[i].correct_ans:
                num_right = num_right + 1
        elif user_ans in ("C", "c"):
            if answers[2] == question_list[i].correct_ans:
                num_right = num_right + 1
        elif user_ans in ("D", "d"):
            if answers[3] == question_list[i].correct_ans:
                num_right = num_right + 1
        else:
            print ("Invalid option, counts as wrong answer")

    print("Number correct: " + str(num_right))