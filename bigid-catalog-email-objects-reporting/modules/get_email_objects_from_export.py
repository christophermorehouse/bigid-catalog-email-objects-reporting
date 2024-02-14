import csv

# Get list of email object FQNs
def get_email_objects(csv_file):
    # Create a list to store the email FQNs
    email_fqn = []

    with open(csv_file, mode='r', encoding="utf8", newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        # Iterate through each row and extract the value from the Fully Qualified Name column
        for i in reader:
            value = i['Fully Qualified Name']
            email_fqn.append(value)
            
    return email_fqn