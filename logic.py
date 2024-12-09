import csv
import os
from collections import Counter

def store_vote(user_id, candidate_name):
    '''This function receives the ID and Candidate from the gui
    and then enters them into the csv file'''
    file_exists = os.path.exists("votes.csv")
    header = ["User ID", "Candidate"]

    if file_exists:
        with open("votes.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            first_row = next(reader, None)
            if first_row != header:
                lines = list(reader)
                with open("votes.csv", mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(lines)


        with open("votes.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == user_id:
                    raise ValueError(f"User ID {user_id} has already voted.")


    with open("votes.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(header)
        writer.writerow([user_id, candidate_name])

def count_votes():
    '''This function counts the votes for each candidate and saves it into a
    dictionary to be used for the live count on the gui'''
    votes_count = Counter()

    if not os.path.exists("votes.csv"):
        return dict(votes_count)

    with open("votes.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            candidate = row[1]
            votes_count[candidate] += 1
    return dict(votes_count)