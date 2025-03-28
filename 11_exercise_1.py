## **🔹 Exercise:**
#🔸 Write a program that:  
#✔ Asks the user to enter their exam score.  
#✔ If the score is **90 or above**, print `"Grade: A"`  
#✔ If the score is **80-89**, print `"Grade: B"`  
#✔ If the score is **70-79**, print `"Grade: C"`  
#✔ If the score is **60-69**, print `"Grade: D"`  
#✔ If the score is **below 60**, print `"Grade: F"`  

exam_score = float(input('Enter your exam score (0 - 100): '))

if exam_score >= 90:
    print(f'{exam_score} obtained is grade A.')
elif exam_score >= 80:  # Now correctly checks scores between 80-89
    print(f'{exam_score} obtained is grade B.')
elif exam_score >= 70:  # Now correctly checks scores between 70-79
    print(f'{exam_score} obtained is grade C.')
elif exam_score >= 60:  # Now correctly checks scores between 60-69
    print(f'{exam_score} obtained is grade D.')
else:  # Any score below 60 is F
    print(f'{exam_score} obtained is grade F.')
     
                                                                               