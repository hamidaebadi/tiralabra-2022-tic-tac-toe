
def minimax(node, last_move, move_list, min_turn, depth):
    if min_turn and node.is_winning(last_move):
        return (-1, last_move)
    elif not min_turn and node.is_winning(last_move):
        return (1, last_move)
    elif len(move_list) == 0 :
        return (0, last_move)

    if min_turn:
        value = (float('+inf'), None)
        for move in move_list:
            node.add_mark(move[0], move[1], 'o')    #add sign to the neighbour slot

            cloned_move_list = move_list.copy()
            cloned_move_list.remove((move[0], move[1]))     # remove tested slot from cloned
            neighbors = node.free_neighbour_slots(move[0], move[1])         # add all free neighbour slots to the cloned moveList
            for slot in neighbors:
                cloned_move_list.add(slot)

            min_tuple = minimax(node, move, cloned_move_list, False, depth+1)

            if min_tuple[0] < value[0]:
                value = (min_tuple[0], move)

            # remove tested move from the board
            node.remove_mark(move[0], move[1])
                        
        return value

    else:   # it's max's turn
        value = (float('-inf'), None)
        for move in move_list:
            node.add_mark(move[0], move[1], 'x')
            
            cloned_move_list = move_list.copy()
            cloned_move_list.remove((move[0], move[1]))    # remove tested slot from cloned

            neighbors = node.free_neighbour_slots(move[0], move[1])         # add all free neighbour slots to the cloned moveList
            for slot in neighbors:
                cloned_move_list.add(slot)

            max_tuple = minimax(node, move, cloned_move_list, True, depth+1)
            if max_tuple[0] > value[0]:
                value = (max_tuple[0], move)
            value = (max(value[0], max_tuple[0]), move)

            # remove tested move from the board
            node.remove_mark(move[0], move[1])
            
        return value