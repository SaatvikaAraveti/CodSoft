import random
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Earth", "Mars", "Venus", "Jupiter"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["African Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "correct_answer": "Blue Whale"
    }
]
def present_quiz(questions):
    score = 0
    for idx, question in enumerate(questions):
        print(f"\nQuestion {idx + 1}: {question['question']}")
        for i, choice in enumerate(question['choices']):
            print(f"{i + 1}. {choice}")
        user_answer = input("Your answer (1/2/3/4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question['choices']):
            user_answer = question['choices'][int(user_answer) - 1]
            if user_answer == question['correct_answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Sorry, the correct answer is: {question['correct_answer']}")
        else:
            print("Invalid input. Please enter a valid choice.")
    return score
def display_results(score, total_questions):
    print(f"\nQuiz Complete!")
    print(f"Your Score: {score}/{total_questions}")
    if score == total_questions:
        print("Congratulations, you got all questions right!")
    else:
        print("Keep practicing!")
while True:
    print("\nWelcome to the General Knowledge Quiz!")
    print("You will be asked multiple-choice questions.")
    random.shuffle(quiz_questions)
    total_questions = len(quiz_questions)
    user_score = present_quiz(quiz_questions)
    display_results(user_score, total_questions)
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print("Thanks for playing! Goodbye!")
        break