
team_list = list(set(input(f"Enter the name of team {i+1}: ") for i in range(int(input("Enter the no. of teams: ")))))
for team1, team2 in zip(team_list[::2], team_list[1::2]):
    print(f"\n  >> {team1} <----> {team2}")

    

    


