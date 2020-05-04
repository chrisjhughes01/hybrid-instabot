import csv

processed_usernames = []
with open('csvs/processed_usernames.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        processed_usernames.append(row['username'])

dom = input("Paste HTML DOM here: ")

dom_usernames = []
split_before_usernames = dom.split('title="')
for each in split_before_usernames[1:]:
    dom_usernames.append(each.split('"')[0])

print(len(dom_usernames), 'unprocessed usernames found.')

unprocessed_usernames = 0
for username in dom_usernames:
    if username not in processed_usernames:
        unprocessed_usernames += 1
        with open('csvs/processed_usernames.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([username])
        with open('csvs/new_usernames.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([username])

print(unprocessed_usernames, 'usernames written to csv files.')
