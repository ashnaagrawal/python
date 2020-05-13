import requests
import json
import random
import pprint
import html

score_correct = 0
score_incorrect = 0

url = "https://opentdb.com/api.php?amount=1"
endgame = ""



while endgame != "quit" :
    r = requests.get(url)
    r.status_code
    if(r.status_code != 200):
        endgame = input("Sorry, there was a problem retriving the question. Press enter to try again or type 'quit' to quit :")
    else:
        valid_answer = False
        answer_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        correct_ans = data['results'][0]['correct_answer']
        answers = data['results'][0]['incorrect_answers']
        answers.append(correct_ans)
        random.shuffle(answers)

        print(html.unescape(question) + "\n")

        for answer in answers:
            print(str(answer_number)+"-"+ html.unescape(answer))
            answer_number += 1

        while valid_answer == False:
            user_answer = input("\n Type the number of correct answer ")
            try:
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <= 0:
                    print("Invalid answer")
                else:
                    valid_answer = True
                    
            except:
                print("Invalid answer.Use only numbers ")
                
        user_answer = answers[int(user_answer)-1]
                

        if user_answer == correct_ans:
            print("\n Congratulations!! You answered correctly! THe correct answer was : "+ html.unescape(correct_ans))
            score_correct += 1
        else:
            print("Sorry, "+  html.unescape(user_answer)+"is incorrect.The correct answer is: "+html.unescape(correct_ans))
            score_incorrect += 1
        print("\n##############################")
        print("YOur Score is:")
        print("Correct answers :"+ str(score_correct))
        print("Incorrect answers :"+ str(score_incorrect))
        print("\n##############################")

        endgame = input("\n Press 'Enter' to play again or type 'quit' to quit game").lower()

print("\n Thanks for playing")
       
        
        
        
        
    
    




