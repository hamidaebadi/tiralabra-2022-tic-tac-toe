
def minimax(node, last_move, move_list: set, min_turn):
    if min_turn and node.is_over(last_move[0], last_move[1]):
        return -1
    elif not min_turn and node.is_over(last_move[0], last_move[1]):
        return 1
    elif len(move_list) == 0 :
        return 0

    if min_turn:
        value = float('+inf')
        for move in move_list:
            node.add_sign(move[0], move[1], '0')    #add sign to the neighbour slot
            
            cloned_move_list = move_list
            cloned_move_list.remove((move[0], move[1]))     # remove tested slot from cloned
            neighbors = node.free_neighbour_slots()         # add all free neighbour slots to the cloned moveList
            for slot in neighbors:
                cloned_move_list.add(slot)

            value = min(value, minimax(node, move, cloned_move_list, False))

            # remove tested move from the board
            node.remove_sign(move[0], move[1])
        return value

    else:   # it's max's turn
        value = float('-inf')
        for move in move_list:
            node.add_sign(move[0], move[1], 'x')
            
            cloned_move_list = move_list
            cloned_move_list.remove((move[0], move[1]))    # remove tested slot from cloned

            neighbors = node.free_neighbour_slots()         # add all free neighbour slots to the cloned moveList
            for slot in neighbors:
                cloned_move_list.add(slot)

            value = max(value, minimax(node, move, cloned_move_list, True))
            # remove tested move from the board
            node.remove_sign(move[0], move[1])
        return value