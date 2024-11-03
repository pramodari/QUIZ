quiz_data = [
    {
        "question": "Who won the 2024 ICC Cricket World Cup?",
        "options": ["A. India", "B. Australia", "C. England", "D. New Zealand"],
        "answer": "A"
    },
    {
        "question": "Which player scored the most runs in the 2024 IPL?",
        "options": ["A. Virat Kohli", "B. Kane Williamson", "C. David Warner", "D. Rohit Sharma"],
        "answer": "C"
    },
    {
        "question": "Who was the highest wicket-taker in the 2024 Ashes series?",
        "options": ["A. Pat Cummins", "B. Stuart Broad", "C. Mitchell Starc", "D. James Anderson"],
        "answer": "B"
    }
]

def ask_question(question_data):
    print("\n" + question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Your answer (A, B, C, or D): ").upper()    
    while user_answer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        user_answer = input("Your answer (A, B, C, or D): ").upper()
    return user_answer == question_data["answer"], question_data["answer"]

def main():
    print("Welcome to the Quiz Game!")
    score = 0
    total_questions = len(quiz_data)
    for question_data in quiz_data:
        correct, correct_answer = ask_question(question_data)
        if correct:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
    print(f"\nYour final score is {score} out of {total_questions}.")

if __name__ == "__main__":
    main()
