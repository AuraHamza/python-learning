import chess
def evaluate_board(board):
    values = {
        chess.PAWN: 100,
        chess.KNIGHT: 320,
        chess.BISHOP: 330,
        chess.ROOK: 500,
        chess.QUEEN: 900,
        chess.KING: 0
    }

    if board.is_checkmate():
        return -100000 if board.turn == chess.WHITE else 100000
    score = 0
    for piece in board.piece_map().values():
        if piece.color == chess.WHITE:
            score += values[piece.piece_type]
        else:
            score -= values[piece.piece_type]
    return score

def beam_search(board, k, depth):
    beam = [(board.copy(), [])]
    for level in range(depth):
        candidates = []
        for current, moves in beam:
            if current.is_game_over():
                candidates.append((current, moves))
                continue
            for move in current.legal_moves:
                new_board = current.copy()
                new_board.push(move)
                new_moves = moves + [move.uci()]
                candidates.append((new_board, new_moves))

        if not candidates:
            break

        candidates.sort(
            key=lambda x: evaluate_board(x[0]),
            reverse=(board.turn == chess.WHITE)
        )
        beam = candidates[:k]
    best_board, best_moves = beam[0]
    return best_moves, evaluate_board(best_board)


board = chess.Board()
k = 3
depth = 3
moves, score = beam_search(board, k, depth)
print("Best move sequence:", " -> ".join(moves))
print("Final evaluation score:", score)