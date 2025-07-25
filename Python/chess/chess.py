#!/usr/bin/env python3


def parse_fen(fen):
    fen_pieces, to_move, castling_rights, ep, hm, fm = fen.split(" ")
    board_state = [[]]
    for char in fen_pieces:
        if char.isdigit():
            board_state[-1].extend(["."] * int(char))
        elif char == "/":
            board_state.append([])
        else:
            board_state[-1].append(char)

    return board_state, to_move


def generate_moves(board_state):
        moves = []
        row_index = 0
        col_index = 0
        co_ord = ()
        
        for col in board_state[row_index]:
            print(col)
            print(board_state[row_index][])
    
    #raise NotImplementedError("This function is not implemented yet.")


def apply_move(board, move):
    raise NotImplementedError("This function is not implemented yet.")

if __name__ == '__main__':
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    board = parse_fen(fen)
    for i in board[0]:
        print(i)
    generate_moves(board[0], board[1])
