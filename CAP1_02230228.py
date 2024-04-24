
 #name: Tashi Tobgay Choden,
 #section: 1ICE
 #StudentIDNumber: 02230228
 #REFERENCES:
 #https://www.askpython.com/python/examples/easy-games-in-python
 #https://www.youtube.com/watch?v=fn68QNcatfo
 #https://www.youtube.com/watch?v=Gyc5dMdP2uc
 #theproblem
 #http://link.to.an.article/video.com
 #SOLUTION:
 #your solution score: 49843
 #input_8_cap1
 

 #codeheretoreadyourinputfile
def calculate_score(rivals_choice, result):
    choice_score = {'A': 1, 'B': 2, 'C': 3}
    outcome_score = {'X': 0, 'Y': 3, 'Z': 6}
    my_choice = None

    if result == 'Y':  # Draw
        my_choice = rivals_choice
    elif result == 'Z':  # Win
        if rivals_choice == 'A':
            my_choice = 'B'
        elif rivals_choice == 'B':
            my_choice = 'C'
        else:
            my_choice = 'A'
    else:  # Lose
        if rivals_choice == 'A':
            my_choice = 'C'
        elif rivals_choice == 'B':
            my_choice = 'A'
        else:
            my_choice = 'B'

    return choice_score[my_choice] + outcome_score[result]

total_score = 0
with open('CSF101-CAP/input_8_cap1.txt', 'r') as file:
    for line in file:
        rivals_choice, result = line.strip().split()
        round_score = calculate_score(rivals_choice, result)
        total_score += round_score

print(f"Total score: {total_score}")