# QUIZ GAME

questions = ("IS HTML a programming language",
            "Whats the average salary in kosovo", 
            "Whats kosovo population in 2024",
            "Idk what to put here")

options = (("A. NO", "B. YES", "C. MAYBE", "D. PROBABLY "),
            ("A. 200 Eur", "B. 300 Eur", "C. 400 Eur", "D. 500 Eur"),
            ("A. 1.2M", "B. 1.4M", "C. 1.6M", "D. 1.8M"),
            ("A. ", "B. ", "C. ", "D "))

answers = ("A", "C", "B", "A")

guesses = []
score = 0
question_num = 0
answers_num = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    

    guess_input = input("Input (A,B,C,D): ").upper()
    guesses.append(guess_input)

    if guess_input == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
    question_num += 1

        
print("---------- RESULTS ----------")
total_score = score / 4 * 100
print(f"Here are your results! \nYour guesses {guesses} \nCorrect answers {answers}\nYour total score = {total_score}%")
print("-----------------------------")
