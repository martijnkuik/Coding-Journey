# Write code below 💖

import random

def magic_8_ball():
    answers = [
        "Yes - definitely.",
        "It is decidedly so.",
        "Without a doubt.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    return random.choice(answers)

def main():
    question = input("Question:      ")
    print("Magic 8 Ball: ", magic_8_ball())

if __name__ == "__main__":
    main()
