import csv, os, pprint

def read_file():
    file_to_load=os.path.join("Resources","election_data.csv")

    candidate_counts={}

    with open(file_to_load, "r") as election_data:
        reader = csv.DictReader(election_data,delimiter=",")
        # Headers: Voter ID,County,Candidate
        for row in reader:
            candidate = row["Candidate"]
            if candidate not in candidate_counts.keys():
                candidate_counts[candidate] = 1
            else:
                candidate_counts[candidate] += 1
    #   The total number of votes each candidate won
    return candidate_counts


def calculations(candidate_counts):
    #   The total number of votes cast
    vote_total = sum(candidate_counts.values())

    #   A complete list of candidates who received votes
    conv_candidate_counts = list(candidate_counts)

    #   The percentage of votes each candidate won
    Khan_percent = (candidate_counts['Khan']/vote_total)*100
    Correy_percent = (candidate_counts['Correy']/vote_total)*100
    Li_percent = (candidate_counts['Li']/vote_total)*100
    OTooley_percent = (candidate_counts["O'Tooley"]/vote_total)*100

    return Khan_percent, Correy_percent, Li_percent, OTooley_percent, conv_candidate_counts, vote_total


def winner(Khan_percent, Correy_percent, Li_percent, OTooley_percent, candidate_counts, vote_total):
    if Khan_percent > Correy_percent and Khan_percent > Li_percent and Khan_percent > OTooley_percent:
        winner = 'Khan'
    elif Correy_percent > Khan_percent and Correy_percent > Li_percent and Correy_percent > OTooley_percent:
        winner = 'Correy'
    elif Li_percent > Khan_percent and Li_percent > Correy_percent and Li_percent > OTooley_percent:
        winner = 'Li'
    elif OTooley_percent > Khan_percent and OTooley_percent > Correy_percent and OTooley_percent > Li_percent:
        winner = 'OTooley'

    output=(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {vote_total}\n"
        f"Khan: "+str(Khan_percent)+" ("+str(candidate_counts['Khan'])+") \n"
        f"Correy: "+str(Correy_percent)+" ("+str(candidate_counts['Correy'])+") \n"
        f"Li: "+str(Li_percent)+" ("+str(candidate_counts['Li'])+") \n"
        f"O'Tooley: "+str(OTooley_percent)+" ("+str(candidate_counts["O'Tooley"])+") \n"
        f"-------------------------\n"
        f"Winner: "+winner+"\n"
        f"-------------------------\n"    
    )
    print(output)

    file_to_output=os.path.join("Analysis","election_results.txt")

    with open(file_to_output, "w") as text_file:
        text_file.write(output)





candidate_counts = read_file()
pprint.pprint(candidate_counts)

khan_percent = calculations(candidate_counts)[0]
correy_percent = calculations(candidate_counts)[1]
li_percent = calculations(candidate_counts)[2] 
otooley_percent = calculations(candidate_counts)[3] 
conv_candidate_counts = calculations(candidate_counts)[4]
vote_total = calculations(candidate_counts)[5]

pprint.pprint(conv_candidate_counts)

winner(khan_percent, correy_percent, li_percent, otooley_percent, candidate_counts, vote_total)