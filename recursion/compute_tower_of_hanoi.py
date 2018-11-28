NUM_PEGS = 3

def compute_tower_of_hanoi(num_rings):
    def c_t_o_h_s(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:
            c_t_o_h_s(num_rings_to_move - 1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            c_t_o_h_s(num_rings_to_move - 1, use_peg, to_peg, from_peg)

    result = []
    pegs = [list(reversed(range(1, num_rings + 1)))]
            + [[] for _ in range(1, NUM_PEGS)]
    c_t_o_h_s(num_rings, 0, 1, 2)
    return result
