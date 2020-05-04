import webbrowser
import csv
print("Press 'enter' to open another username or type 'stop' to exit.")

new_usernames = []
with open('csvs/new_usernames.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        new_usernames.append(row['username'])

processed_usernames = []
for username in new_usernames:
    url = 'https://www.instagram.com/' + username
    webbrowser.open(url)
    processed_usernames.append(username)

    print(username)
    if input('Continue? ') == 'stop':
        break

with open('csvs/new_usernames.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['username'])
    for username in new_usernames:
        if username not in processed_usernames:
            writer.writerow([username])
