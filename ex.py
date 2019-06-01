ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
            {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
            {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
            {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
            {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
            {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]

#A 'gold' is worth 3 points, 
# 'silver' is worth 2 points,
# 'bronze' is worth 1 point.


#make an list and default to 0.
participants = {
    'Smudge': 0,
    'Tigger': 0,
    'Simba': 0,
    'Bella': 0,
    'Lucky': 0,
    'Boots': 0,
    'Felix': 0
    }

#loop the ballots and voters
for x in ballots:
    for key, value in ballot.items():
        if key == 'gold':
            participants[value] += 3
        elif key == 'silver':
            participants[value] += 2
        elif key == 'bronze':
            participants[value] += 1
winner = max(participants, key=participants.get)
print(winner)