import random
import time
import asci


print(asci.logo)


start_text = f" Input The Name of Your Team: "
team = input(start_text)
print(f"You Have Chosen {team.upper()}")

team_arr = ['Bangladesh', 'India', 'Pakistan', 'Nepal', 'Srilanka', 'Australia', 'Newzealand', 'South Africa',
            'Westindies', 'England', 'Afganistan', 'Ireland', 'Netherlands', 'Papua New Gunie', 'UAE', 'Zimbabwe']

pitch = ['dusty', 'flat', 'sporting', 'green']
weather = ['Sunny', 'Cloudy', 'Bit Cloudy', 'Windy', 'Moderately Windy']
pitch_supp = {'dusty': 'spinners', 'flat': 'batters',
              'green': 'pacers', 'sporting': 'both batters and bowlers'}
pitch_ana = ['Harsha Bhogle 👨🏾', 'Geoffrey Boycott 👨🏻',
             'Lan Bishop 👨🏿', 'Ramiz Raza 👦🏽', 'Ravi Sashri 👨🏽‍🦲', 'Atahar Ali Khan 🧔🏽']

coin = ['Heads', 'Tails']
toss_winner = []
choice = ['bat 🏏', 'field ⚾']


com_team = team_arr[random.randint(0, len(team_arr)-1)]
decided = {team: '', com_team: ''}
pitch_sel = pitch[random.randint(0, len(pitch)-1)]
pitch_con = pitch_supp[pitch_sel]
pitch_anl = pitch_ana[random.randint(0, len(pitch_ana)-1)]

while team.lower() == com_team.lower():
    com_team = team_arr[random.randint(0, len(team_arr)-1)]


print(f"Opponent Have Chosen {com_team.upper()}")

print("------------------------------------------------------------")
print(
    f"Commentator:\" the weather is {weather[random.randint(0, len(weather)-1)]} and crowd is cheering 🎉🎉 \n Lets see what {pitch_anl} have for us in Pitch Report\n ")

time.sleep(4)

print("------------------------------------------------------------")


print(asci.message1)
time.sleep(2)

print(f" \n \"Hello I'm {pitch_anl}, and welcome to this important match between {team.capitalize()} and {com_team.capitalize()}. \n Todays pitch is {pitch_sel.upper()} and it will have a huge advantage for {pitch_con.upper()}\"")
time.sleep(3)

print("------------------------------------------------------------")


print(f"\"Commentators: Thanks {pitch_anl}! \n Both captians from {team.capitalize()} and {com_team.capitalize()} is on the field \n where they are preparing for toss. They are directly joining us from the pitch.\"")
time.sleep(3)

print("------------------------------------------------------------")
print(asci.message2)
print(f"{pitch_anl}: \" So, captain of {team.upper()} what do you want to choose? Heads or tails? \"")
plr_in = int(input("PRESS 1 TO CHOOSE HEADS AND 2 FOR TAILS:  "))

plr_coin = coin[plr_in-1]

time.sleep(2)
print(f"You: \" {plr_coin.upper()} \"")

print(f"{pitch_anl}: \" Great, Here we go! \"")
time.sleep(2)

print(f"---Tosses The Coin--- \n")

print(asci.toss)


toss_res = coin[random.randint(0, len(coin)-1)]
time.sleep(3)

if toss_res == coin[0]:
    print("\n" + asci.heads)

else:
    print("\n" + asci.tails)


print(f"\n{pitch_anl}: \" Its, ")
time.sleep(1)
print(f"{toss_res.upper()}!\"")

time.sleep(3)

if plr_coin == toss_res:
    msg = f"{team.upper()} has won the toss"
    toss_winner.append(team)
else:
    msg = f"{com_team.upper()} has won the toss"
    toss_winner.append(com_team)

print(f"{pitch_anl}: \"{msg}\"")
print("------------------------------------------------------------")

print(
    f"{pitch_anl}: \"So, Captain of {toss_winner[0].upper()} what do you want to choose? Bat or Field? \"")

time.sleep(3)

if toss_winner[0].lower() == team.lower():
    plr_decided = int(input(f"Press 1 to BAT or 2 to FIELD"))
    plr_decide = choice[plr_decided-1]  # choses bat
    decided[team] = plr_decide
    decided[com_team] = choice[plr_decided-2]
    print(f"{team} Captain: \"We will {plr_decide.upper()} first \"")
else:
    com_random_choice = random.randint(0, len(choice)-1)
    com_decided = choice[com_random_choice]
    decided[com_team] = com_decided  # registers com choice in dic
    decided[team] = choice[com_random_choice-1]  # registers plr choice in dic
    print(f"{com_team} Captain: \"We will {com_decided.upper()} first \"")

time.sleep(2)

if decided[toss_winner[0]] == choice[0]:
    print(asci.bat)
else:
    print(asci.bowl)
