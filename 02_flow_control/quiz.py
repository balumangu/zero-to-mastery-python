# ==============================================================================
# SCRIPT: quiz.py
# PURPOSE: Demonstrating working of lists and tuples
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

# This is a program that simulates a quiz. 
# It uses tuples to store questions and answers, and lists to store the correct answers.

questions = (
    "1. Which element has the highest electrical conductivity of all metals?",
    "2. Which planet in our solar system rotates clockwise (retrograde rotation)?",
    "3. In computer science, what does the ""S"" stand for in the acronym 'HTTPS'?",
    "4. Which part of the human eye is responsible for giving it its distinctive color?",
    "5. Which of these is the only continent on Earth that has no active volcanoes?"
)

options = (
    ["(A) Gold", "(B) Silver", "(C) Copper", "(D) Aluminum"],
    ["(A) Jupiter", "(B) Mars", "(C) Venus", "(D) Saturn"],
    ["(A) Secure", "(B) Simple", "(C) Standard", "(D) Speedy"],
    ["(A) Pupil", "(B) Cornea", "(C) Retina", "(D) Iris"],
    ["(A) Antarctica", "(B) Australia", "(C) Europe", "(D) North America"]
)

answers = ("B", "C", "A", "D", "B")
guesses = []
score = 0

for i in range(len(questions)):
    print(questions[i])
    for option in options[i]:
        print(option)
    guess = input("Enter your answer (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[i]:
        score += 1
        print("Correct!")
    else:
        print("Wrong! The correct answer is:", answers[i])
    print()

print(f"Your final score is: {score}/{len(questions)}")