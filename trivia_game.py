import random

questions = {
    "What color is the sky?" : "blue",
    "What is largest organ of the body?" : "skin",
    "How many continents are there?" : "7",
    "What gas do humans breathe in to survive?" : "oxygen",
    "What planet is known as the Red Planet?" : "mars"
}

def trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    
    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong as always. The correct answer is {correct_answer}.\n")

    print(f"Game over! Your final score is: {score} / {total_questions} ")

trivia_game()