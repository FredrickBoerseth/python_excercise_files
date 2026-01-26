print("Welcome!")
user_question = input("type your question: ")

with open("user_question.txt", "w") as f:
    f.write(user_question)
