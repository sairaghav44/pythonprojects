#py quiz game

questions = ("how many elements are there in the periodic table ?",
             "what is the capital of india ?",
             "what is the largest planet in our solar system ?",
             "what is the chemical symbol for copper ?",
             "who is the author of the onepiece ?")
options = (("A.118","B.119","C.120","D.121"),
           ("A.New Delhi","B.Mumbai","C.Kolkata","D.Chennai"),
           ("A.Jupiter","B.Saturn","C.Neptune","D.Uranus"),
           ("A.Cu","B.Ag","C.Au","D.Fe"),
           ("A.Eiichiro Oda","B.Masashi Kishimoto","C.Tite Kubo","D.Kaiji Taniguchi"))

answers = ("A","A","A","A","A")
gusses =[]
score=0
question_no=0


for  question in questions:
    print("-----------------------------")   
    print (question)

    for option in options[question_no]:
        print(option)


    guess = input("Enter ( A, B , C , D ,)): ").upper()
    gusses.append(guess)
    if guess == answers[question_no]:
        score += 1 
        print("CORRECT !")
        print("Damn nigga you prodigy :O")
    else:
        print("wrong !!")    
        print(f"{answers[question_no]} is the correct answer nigga :p ")

    question_no += 1 

print("-----------------------------")
print(f"         RESULTS            ")
print("-----------------------------")   

print("answers: " , end = " ")
for answer in answers:
    print(answer, end = " ")
print()

print("gusses: " , end = " ")
for guess in gusses:
    print(guess, end = " ")
print()

score = int(score / len(questions) * 100)
print (f"your score is  : {score}%")