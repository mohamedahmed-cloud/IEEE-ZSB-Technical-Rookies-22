# input operation
number_of_players=int(input())
leader_board=list(set(map(int,input().split())))

number_of_games_player_play=int(input())
score_for_games=list(map(int,input().split()))

# leader_board.sort()
# output operation 
j=0
leader_board.sort()
number_of_unrepeated_players=len(leader_board)
player_score=0
for i in score_for_games:
    while j <number_of_unrepeated_players and leader_board[j]<=i :
        j+=1
    print(number_of_unrepeated_players-j+1)
    



    # Don't work because of time execution
    
    # leader_board.append(i)
    # leader_board=sorted(leader_board,reverse=True)
    # print(leader_board.index(i)+1)
    # leader_board.remove(i)    




  
