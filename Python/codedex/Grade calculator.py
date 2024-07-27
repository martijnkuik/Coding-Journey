"""Name of exam: Computer science
Max. posslible Score: 100
Your Score:79
You got 79.00% wich is a B
90%A+, 80% A- , 70% B, 60% C, 50% D snd 40%"""


print("Grade Calculator\n")
exam_name = (input("What is the name of the exam\n"))
total_score = int(input("Enter Maximum score\n"))
your_score = int(input("What is your score\n"))


number_score = float(your_score / total_score)
final_score = round(number_score, 2)
final_perc = round(float(your_score / total_score)*100, 2)
print("You got an",final_perc,"%")
if final_score >= .90:
    print("Wow thats an  A+, Great job Einstein")
elif final_score >= .80 and final_score <= .89:
        print("Impresive you got an A-")
elif final_score >= .70 and final_score <= .79:
        print("You got an B, It is good but not that great")
elif final_score >= .60 and final_score <= .69:
        print("You got an C, It is enough, But you can do better")
elif final_score >= .50 and final_score <= .59:
        print("You got an D, Please explain yourself")
elif final_score <= .49:
        print("You got an U, Thats really not good!")
else:    
       print(" Maybe better luck next time")
  
