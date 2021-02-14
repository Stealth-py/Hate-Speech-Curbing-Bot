import random

sentence = []
sentence.append("Hello")
sentence.append("Police")
sentence.append("Snow")
sentence.append("Helicopter")
sentence.append("Hackathon")
sentence.append("Winner")
sentence.append("Coder")
sentence.append("Hacker")
sentence.append("Macintosh")
sentence.append("Apple")
sentence.append("Windows")
sentence.append("Microsoft")
sentence.append("Compiler")
sentence.append("Mobile")
sentence.append("Hack")
sentence.append("Geography")
sentence.append("Chopper")
sentence.append("Constipation")
sentence.append("Linear")
sentence.append("Algebra")
sentence.append("Python")
sentence.append("Instagram")
sentence.append("Introduction")
sentence.append("Human")
sentence.append("Interaction")
sentence.append("Digital")
sentence.append("Circuits")
sentence.append("Communication")
sentence.append("Physics")
sentence.append("Chemistry")
sentence.append("Biology")
sentence.append("Maths")
sentence.append("History")
sentence.append("Consumer")

def answer_checker(answer,word_min):
    for x in word_min:
        if x == answer:
            return 1
        else:
            return 0


def hangman():
    word = random.choice(sentence)
    wordcopy = word
    length = len(word)
    question = []
    while(question.find("_")!=0):
        for i in range(0,length):
            question.append["_"]
        lives = 5
        print ("You have ", lives, " lives")
        word_min = list(set(word))
    #input character from user
        answer = input()
        if (answer_checker(answer,word_min) == 1):
            while(word.find(answer)!=0):
                question[word.find(answer)] = answer
                word.replace(answer," ", 1)
        
        else :
            lives -= 1
        print("You have ", lives, " lives")
        if (lives == 0):
            print("You are out of lives")
            print("The word was ", wordcopy)
            break
        else:
            print(question)





    