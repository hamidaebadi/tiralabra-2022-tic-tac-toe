
def minimax(node, last_move, move_list, min_turn):
    if min_turn and node.is_winning(last_move):
        return (-1, last_move)
    elif not min_turn and node.is_winning(last_move):
        return (1, last_move)
    elif node.is_draw():
        return (0, last_move)

    if min_turn:
        value = (float('+inf'), None)

        for move in move_list:
            node.add_mark(move[0], move[1], "O")  #add sign to the neighbour slot

            cloned_move_list = move_list.copy()
            cloned_move_list.remove(move)     # remove tested slot from cloned
            neighbors = node.free_neighbour_slots(move[0], move[1])         # add all free neighbour slots to the cloned moveList
            for slot in neighbors:
                cloned_move_list.add(slot)

            child_Value = minimax(node, move, cloned_move_list, False)

            value = min(value, child_Value)

            # remove tested move from the board
            node.remove_mark(move[0], move[1])

            # beta = min(beta, child_Value[0])
            # if beta <= alpha:
            #     break
                        
        return value

    else:   # it's max's turn
        value = (float('-inf'), None)
        for move in move_list:
            node.add_mark(move[0], move[1], "X")
            
            cloned_move_list = move_list.copy()
            cloned_move_list.remove(move)    # remove tested slot from cloned

            neighbors = node.free_neighbour_slots(move[0], move[1])         # add all free neighbour slots to the cloned moveList
            for slot in neighbors:
                cloned_move_list.add(slot)

            child_Value = minimax(node, move, cloned_move_list, True)

            value = max(value, child_Value)
             # remove tested move from the board
            node.remove_mark(move[0], move[1])

            # alpha = max(alpha, child_Value[0])
            # if beta <= alpha:
            #     break

        return value