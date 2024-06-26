def start_game():
    guesses = []
    correct = 0
    question_num = 1

    for key in questions:
        print("---------------------")  # A seperator
        print(key)
        for i in answer_text[question_num - 1]:
            print(i)

        guess = input("A, B, C oder D: ")
        guess = guess.upper()
        guesses.append(guess)

        correct += check_answer(guess, questions.get(key))
        question_num += 1
    display_score(correct, question_num-1)


def check_answer(guess, answer):
    if guess == answer:
        print("KORREKT :)")
        return 1

    else:
        print("FAAAALSCH! :(")
        return 0


def display_score(score, total):
    print("---------")
    if score == total:
        print("PERFEKT! WOW")
    elif score > total/2:
        print("GLÜCKWUNSCH!")
    else:
        print("DAS GEHT BESSER!")

    print("+++ PUNKTE: " + str(score) + " von " + str(total) + " +++")


def play_again():
    pass

# -------------Main Part------------------


questions = {                                              # All "Question / Answer Nr." Pairs
    "In welcher Stadt leben wir?": "B",
    "Was ist die Antwort auf das Universum?": "C",
    "Warum heißt Stuhl? Was heißt Stuhl?": "B"
}

answer_text = [                                             # All Possible Answers belonging to the Question
    ["A. Amsterdam", "B. Eine bewohnbare Stadt", "C. London", "D .Irgendwo"],
    ["A. Was", "B. Ja", "C. 42", "D. Erdbeermarmeladenbrot mit Honig"],
    ["A. Hö?", "B. BENJAMIN BLÜMCHEN!!!!", "C. Warum", "D. Stuhl ist ein, auf sich hinsetzbarer, Gegenstand"],
]

start_game()  # starts the Game, obviously ._.

while True:
    if input("Play again? (y/n) ") == "y":
        start_game()
