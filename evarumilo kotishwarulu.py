questions = [
    ["What is the capital of India?", "Delhi"],
    ["Which planet is known as the Red Planet?", "Mars"],
    ["How many states are there in India?", "28"],
    ["Who wrote the national anthem of India?", "Rabindranath Tagore"]
    ["Which is the largest ocean in the world?", "Pacific Ocean"]
]

Moneyearned = [100, 1000, 10000, 100000,10000000]
winnings = 0

print(" Welcome to Evaru Meelo Kotiswarulu \n")

for i in range(len(questions)):
    print(f"Q{i+1}: {questions[i][0]}")
    useranswer = input("Enter your answer: ")
    if useranswer.strip().lower() == questions[i][1].lower():
        winnings = Moneyearned[i]
        print(f" Correct! You won ₹{Moneyearned[i]}\n")
    else:
        print(" Wrong answer!")
        break

print(f"\n🏆 You take home ₹{winnings}")
