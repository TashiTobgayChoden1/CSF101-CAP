
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
 

def compute_round_score(opponent_move, desired_outcome):
    move_scores = {'A': 1, 'B': 2, 'C': 3}
    outcome_scores = {'X': 0, 'Y': 3, 'Z': 6}
    player_move = None

    if desired_outcome == 'Y':  # Draw
        player_move = opponent_move
    elif desired_outcome == 'Z':  # Win
        if opponent_move == 'A':
            player_move = 'B'
        elif opponent_move == 'B':
            player_move = 'C'
        else:
            player_move = 'A'
    else:  # Lose
        if opponent_move == 'A':
            player_move = 'C'
        elif opponent_move == 'B':
            player_move = 'A'
        else:
            player_move = 'B'

    return move_scores[player_move] + outcome_scores[desired_outcome]

total_score = sum(
    compute_round_score(opponent_move, desired_outcome)
    for opponent_move, desired_outcome in (line.strip().split() for line in open('CSF101-CAP/input_8_cap1.txt'))
)

print(f"Total score: {total_score}")