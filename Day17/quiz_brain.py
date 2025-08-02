class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 1
        self.question_list = question_list

    def next_question(self):
        for item in self.question_list:
            user_choice = input(f"Q.{self.question_number} {item.text} (True/False)?\t").title()
            if(user_choice==item.answer):
                self.question_number += 1
                if(self.question_number==13):
                    print(f'We are at the end of the quiz, your got it all right with final score of: {self.question_number-1}')
                    break
                else:
                    print("Great going, that was correct, we proceed to next question\n")
            else:
                print(f'You guessed it wrong. Your score is {self.question_number-1}\n')
                break


