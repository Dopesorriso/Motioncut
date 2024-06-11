def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= len(options):
                break
            else:
                print("Invalid input. Please enter a number corresponding to one of the options.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if options[answer - 1] == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong. The correct answer is: {correct_answer}\n")
        return False

def quiz_game(questions):
    score = 0

    for question, options, correct_answer in questions:
        if ask_question(question, options, correct_answer):
            score += 1

    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    questions = [
        ("What is the capital of France?", ["Berlin", "London", "Paris", "Rome"], "Paris"),
        ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], "Mars"),
        ("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "Mark Twain", "Ernest Hemingway", "Jane Austen"], "Harper Lee"),
        ("What is the smallest prime number?", ["0", "1", "2", "3"], "2"),
        ("What is the powerhouse of the cell?", ["Nucleus", "Ribosome", "Mitochondria", "Golgi apparatus"], "Mitochondria"),
        ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "NaCl"], "H2O"),
        ("Who painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "Leonardo da Vinci"),
        ("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "Pacific Ocean"),
        ("Who is known as the Father of Computers?", ["Alan Turing", "Charles Babbage", "John von Neumann", "Bill Gates"], "Charles Babbage"),
        ("What is the longest river in the world?", ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], "Nile River")
    ]

    quiz_game(questions)
