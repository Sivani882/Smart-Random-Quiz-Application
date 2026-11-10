
import random

easy_questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Hyderabad"],
        "answer": "B"
    },
    {
        "question": "How many days are there in a week?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "What is 10 + 5?",
        "options": ["A. 10", "B. 15", "C. 20", "D. 25"],
        "answer": "B"
    },
    {
        "question": "Which is the national animal of India?",
        "options": ["A. Lion", "B. Elephant", "C. Tiger", "D. Deer"],
        "answer": "C"
    },
    {
        "question": "How many months are there in a year?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is 5 * 5?",
        "options": ["A. 10", "B. 15", "C. 20", "D. 25"],
        "answer": "D"
    }
]

medium_questions = [
    {
        "question": "Which language is used for AI?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. <!--", "D. **"],
        "answer": "B"
    },
    {
        "question": "Which file extension is used for Python files?",
        "options": ["A. .html", "B. .py", "C. .css", "D. .java"],
        "answer": "B"
    },
    {
        "question": "Which device is used to type text?",
        "options": ["A. Mouse", "B. Keyboard", "C. Monitor", "D. Printer"],
        "answer": "B"
    },
    {
        "question": "Which part is called the brain of a computer?",
        "options": ["A. CPU", "B. Mouse", "C. Keyboard", "D. Monitor"],
        "answer": "A"
    },
    {
        "question": "What is the square of 6?",
        "options": ["A. 12", "B. 24", "C. 30", "D. 36"],
        "answer": "D"
    },
    {
        "question": "What is 100 / 10?",
        "options": ["A. 5", "B. 10", "C. 15", "D. 20"],
        "answer": "B"
    }
]

hard_questions = [
    {
        "question": "What is the output of len('Python')?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "B"
    },
    {
        "question": "Which Python data type is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "What is the output of 2 ** 3?",
        "options": ["A. 5", "B. 6", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. String"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used for exception handling?",
        "options": ["A. try", "B. repeat", "C. check", "D. test"],
        "answer": "A"
    },
    {
        "question": "What is the result of 10 % 3?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 0"],
        "answer": "A"
    }
]

while True:

    print("\nWelcome to Smart Random Quiz Application!")

    print("\nSelect Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    level = input("Enter your choice (1/2/3): ")

    if level == "1":
        questions = easy_questions
        print("You selected Easy Level!")

    elif level == "2":
        questions = medium_questions
        print("You selected Medium Level!")

    elif level == "3":
        questions = hard_questions
        print("You selected Hard Level!")

    else:
        questions = easy_questions
        print("Invalid choice! Defaulting to Easy Level.")

    selected_questions = random.sample(questions, 5)

    print("\nLet's start the quiz!")

    score = 0

    for q in selected_questions:
        print("\n" + q["question"])

        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer!")
            print("Correct answer is:", q["answer"])

    print("\nQuiz Completed!")
    print("Your final score is:", score, "/", len(selected_questions))

    percentage = (score / len(selected_questions)) * 100

    print("Your percentage is:", percentage, "%")

    if percentage == 100:
        print("Excellent! Perfect Score!")
    elif percentage >= 80:
        print("Very Good! Keep it up!")
    elif percentage >= 60:
        print("Good! Keep Practicing!")
    elif percentage >= 40:
        print("Nice Try! Practice more!")
    else:
        print("Don't give up! Try again!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThank you for playing!")
        break
