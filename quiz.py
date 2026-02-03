def display_question(prompt, choices, answer):
    print(prompt)
    for i, choice in enumerate(choices, 1):
        print(i, ". ", choice)
    user_answer = int(input("Enter your answer (1-" + str(len(choices)) + "): "))
    if user_answer == answer:
        return True
    else:
        return False

def run_quiz(questions):
    score = 0
    for question in questions:
        prompt, choices, answer = question
        if display_question(prompt, choices, answer):
            score += 1
    print("You got", score, "out of", len(questions))

computer_questions = [
    ("What does CPU stand for? ", ["Central Processing Unit", "Computer Processing Unit", "Central Programming Unit"], 1),
    ("What does RAM stand for? ", ["Random Access Memory", "Random Application Memory", "Random Access Module"], 1)
]

sports_questions = [
    ("What is the capital of France? ", ["Paris", "London", "Rome"], 1),
    ("Who is the president of the United States? ", ["Donald Trump", "Joe Biden", "Barack Obama"], 2)
]

bollywood_questions = [
    ("Who played the role of Raj in Dilwale Dulhania Le Jayenge? ", ["Shah Rukh Khan", "Aamir Khan", "Salman Khan"], 1),
    ("Who won the National Film Award for Best Actress in 2020? ", ["Deepika Padukone", "Alia Bhatt", "Kangana Ranaut"], 3)
]

topics = [
    ("Computer", computer_questions),
    ("Sports", sports_questions),
    ("Bollywood", bollywood_questions)
]

def run_quiz_game():
    print("Quiz Game")
    print("==============")
    print("Choose a topic:")
    for i, topic in enumerate(topics, 1):
        print(i, ". ", topic[0])
    topic_num = int(input("Enter the number of your chosen topic: "))
    run_quiz(topics[topic_num-1][1])

run_quiz_game()