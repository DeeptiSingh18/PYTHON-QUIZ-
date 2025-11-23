import random
import time
#FLASHCARDS FOR CSE

flashcards = [
    {
        "question": "In C language, what is the size of 'int' on a 64-bit system?",
        "answer": "4"
    },
    {
        "question": "Python is interpreted or compiled?",
        "answer": "interpreted"
    },
    {
        "question": "Which data structure uses FIFO?",
        "answer": "queue"
    },
    {
        "question": "What does RAM stand for?",
        "answer": "random access memory"
    },
    {
        "question": "AND gate gives output 1 only when?",
        "answer": "both inputs are 1"
    },
    {
        "question": "Name the algorithm used for shortest path in graphs.",
        "answer": "dijkstra"
    },
    {
        "question": "What is the default value of uninitialized int in C?",
        "answer": "garbage"
    },
    {
        "question": "Which Python collection type is ordered, mutable, and allows duplicates?",
        "answer": "list"
    },
    {
        "question": "In DBMS, what does ACID stand for? (Write only A)",
        "answer": "atomicity"
    },
    {
        "question": "Which number system does a computer understand?",
        "answer": "binary"
    },
    {
        "question": "In OS, what is the program that manages hardware?",
        "answer": "kernel"
    },
    {
        "question": "State De Morgan’s first law: NOT(A AND B) = ?",
        "answer": "not a or not b"
    },
    {
        "question": "Which searching algorithm works only on sorted arrays?",
        "answer": "binary search"
    },
]

#QUIZ LOGIC
def flashcard_quiz():
    print("\n==============================")
    print("    CSE FLASHCARD QUIZ    ")
    print("==============================")
    print("Type your answers. Not case-sensitive.")
    print("Type 'exit' anytime to quit.\n")

    score = 0
    random.shuffle(flashcards)
    
    for card in flashcards:
        print("\nQuestion:")
        print(card["question"])
        user_ans = input("Your answer: ").strip().lower()

        if user_ans == "exit":
            break

        if user_ans == card["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! Correct answer → {card['answer']}")

        time.sleep(0.5)

    print("\n-----------------------------")
    print(f"Quiz Finished! Your Score: {score}/{len(flashcards)}")
    if score == len(flashcards):
        print(" Outstanding! topper mode activated!")
    elif score > len(flashcards) * 0.7:
        print(" Great job!")
    else:
        print(" Keep practicing!")

# Run quiz
flashcard_quiz()
