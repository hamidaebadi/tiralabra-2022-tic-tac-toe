def find_best_move(node, last_move):
    moves_list = set()
    neighbours_slots = node.free_neighbour_slots(last_move[0], last_move[1]) 
    
    for slot in neighbours_slots:
        moves_list.add(slot)

    best_move = None
    best_score = float("+inf")
    for move in moves_list:
        result = minimax(node, last_move, moves_list, False)
        move = result[1]
        score = result[0]
        if score < best_score:
            best_score = score
            best_move = move
    return best_move
    


def minimax(node, last_move, moves_list, is_maximizing):
    if is_maximizing and node.is_winning(last_move):
        return (1, last_move)
    elif not is_maximizing and node.is_winning(last_move):
        return (-1, last_move)
    
    if is_maximizing:
        best_move = None
        value = (float('-inf'), best_move)

        for move in moves_list:
            node.add_mark(move[0], move[1], "X")  #add sign to the neighbour slot

            cloned_move_list = moves_list.copy()
            cloned_move_list.remove(move)     # remove tested slot from cloned
            neighbors = node.free_neighbour_slots(move[0], move[1])      # add all free neighbour slots to the cloned moveList
            for slot in neighbors:
                cloned_move_list.add(slot)

            child_Value = minimax(node, move, cloned_move_list, False)

            if child_Value[0] > value[0]:
                best_move = move
            value = (max(value[0], child_Value[0]), best_move)

            # remove tested move from the board
            node.remove_mark(move[0], move[1])

        return value

    else:   #it's Min's turn
        best_move = None
        value = (float('+inf'), best_move)

        for move in moves_list:
            node.add_mark(move[0], move[1], "O")  #add sign to the neighbour slot
            cloned_move_list = moves_list.copy()
            cloned_move_list.remove(move)     # remove tested slot from cloned
            neighbors = node.free_neighbour_slots(move[0], move[1])      # add all free neighbour slots to the cloned moveList
            for slot in neighbors:
                cloned_move_list.add(slot)

            child_Value = minimax(node, move, cloned_move_list, True)
            if child_Value[0] < value[0]:
                best_move = move
            value = (min(value[0], child_Value[0]), best_move)

            # remove tested move from the board
            node.remove_mark(move[0], move[1])

        return value

