print("Welcome to the MeFromMe-suggested Questionnaire! Inherit your inner trans spidergirl and let us begin!")

questionsAndAnswers = [
    {
        "question": "Who's the greatest man of all time?",
        "answer": "MeFromMe"
    },
    {
        "question": "Who's the cutest pookie bear of all time?",
        "answer": "MeFromMe"
    },
    {
        "question": "Who has the longest dick in this measly earth?",
        "answer": "MeFromMe"
    },
] 

answerCounter = 0
for questionDict in questionsAndAnswers:
    question = questionDict["question"]
    answer = questionDict["answer"]

    prompt = input(question + " ")

    if prompt.lower() == answer.lower():
        print("That's correct! It is indeed " + answer + "!")
        answerCounter+=1
    else:
        print("No silly! It's " + answer)

if answerCounter == 0:
    print("You lost! How dare you fail this sacred questionnaire!")
elif answerCounter == 3:
    print("You won! You're a true Prophet of MeFromMe!")