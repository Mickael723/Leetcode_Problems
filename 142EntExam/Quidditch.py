if __name__== "__main__":
    # Initialize
    team1, team2 = tuple(map(str, input().split()))
    score = {team1: 0, team2: 0}
    
    while (True):
        team_scored = input()
        if team_scored == None:
            break
        elif team_scored == team1:
            score[team1] = score[team1] + 10
        elif team_scored == team2:
            score[team2] = score[team2] + 10
        # End Case
        else:
            snitch_team = team_scored.split()
            score[snitch_team[0]] = score[snitch_team[0]] + 150
            break
    
    #Print Results
    if score[team1] > score[team2]:
        print(f"{team1} wins")
        print(f"{score[team1]}-{score[team2]}")
    elif score[team1] < score[team2]:
        print(f"{team2} wins")
        print(f"{score[team2]}-{score[team1]}")
    else:
        print("Tie")
        print(f"{score[team1]}-{score[team2]}")
