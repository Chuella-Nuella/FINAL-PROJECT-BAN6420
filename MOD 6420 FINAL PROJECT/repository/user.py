import csv

def save_to_csv(users_data):
    with open("user_data.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Age', 'Gender', 'Income', 'Utilities', 'Entertainment', 'School Fees', 'Shopping', 'Healthcare'])
        for user in users_data:
            writer.writerow([
                user['age'], user['gender'], user['income'],
                user.get('utilitiesAmount', 0),
                user.get('entertainmentAmount', 0),
                user.get('schoolFeesAmount', 0),
                user.get('shoppingAmount', 0),
                user.get('healthcareAmount', 0)
            ])

            

