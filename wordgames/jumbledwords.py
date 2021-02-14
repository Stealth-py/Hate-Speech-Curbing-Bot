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

def jumbledwords():
    string = random.choice(sentence)
    jumbledword = []
    answer = string
    length = len(string)
    for i in range (0,length):
        if (len(string)!= 0):
            word = random.choice(string)
            jumbledword.append(word)
            string = string.replace(word,"",1)
    return(", ".join(jumbledword), answer)
    
        
    
        
    
