teams = [
    ['keshav', 'ishi', 'shivam kumar'],
    ['ansh', 'arpitha'],
    ['aarush', 'manas'],
    ['yatin', 'raghav'],
    ['shiwam', 'rahul'],
    ['farhan', 'shivam shreyansh']
]

def who_are_my_other_team_members(name):
    name = name.lower()

    for team in teams:
        if name in team:
            print([others for others in team if others != name])
            break