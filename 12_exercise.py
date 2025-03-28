#Determine if an applicant is eligible for a loan based on having high income or good credit:
high_income = input('Do you have a high income? (yes or no): ').strip().lower() == "yes"
good_credit = input('Do you have a good credit? (yes or no): ').strip().lower() == "yes"

if high_income or good_credit:
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan.")