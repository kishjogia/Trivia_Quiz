# ToDo:
# 1. [X] Access the OpenTDB API and get questions
# 2. [ ] Read the JSON file and out as seperate questions
# 3. [ ] Ask each question and check answer, keeping score
# 4. [ ] Provide result from the questions
# 5. [ ] Allow user to choose number of questions
# 6. [ ] Allow user to choose the category of the questions

import requests
import json
import html

def get_questions():
    session_key = requests.get("https://opentdb.com/api_token.php?command=request")
    token = json.loads(session_key.text)
    token = token["token"]                      # get the session token, to prevent same questions

    URL = "https://opentdb.com/api.php?amount=10&type=multiple&token=" + token
    response = requests.get(URL)                # get a set of 10 random questions

    questions_tdb = json.loads(response.text)
    questions_tdb = questions_tdb["results"]

    unescape = html.unescape

    question_list = [[0 for y in range(4)] for x in range(10)]

    for question_dict in questions_tdb:
        category = unescape(question_dict["category"])
        question = unescape(question_dict["question"])
        correct_ans = unescape(question_dict["correct_answer"])
        wrong_ans = unescape(question_dict["incorrect_answers"])

        question_list[0][0] = category
        question_list[0][1] = question
        question_list[0][2] = correct_ans
        question_list[0][3] = wrong_ans

    print (question_list[0])

    return

if __name__ == "__main__":
    get_questions()