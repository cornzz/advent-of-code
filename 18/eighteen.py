from fileinput import input

# Solution is an LF(1)-Parser implementing following grammars
# Inspired by @jonathanpaulson 's solution
# ========== Part 1 ==========
# TERM -> lit | \( EXPR \)
# EXPR -> TERM (op TERM)*


def term(L, i, p1):
    if L[i] == '(':
        v, i = (expr if p1 else emul)(L, i + 1)
        return v, i + 1
    else:
        return int(L[i]), i + 1


def expr(L, i):
    res, i = term(L, i, True)

    while i < len(L) and L[i] != ')':
        op = L[i]
        v, i = term(L, i + 1, True)
        res = res + v if op == '+' else res * v

    return res, i


# ========== Part 2 ==========
# TERM -> lit | \( EMUL \)
# EADD -> TERM (\+ TERM)*
# EMUL -> EADD (\* EADD)*


def emul(L, i):
    res, i = eadd(L, i)

    while i < len(L) and L[i] == '*':
        v, i = eadd(L, i + 1)
        res *= v

    return res, i


def eadd(L, i):
    res, i = term(L, i, False)

    while i < len(L) and L[i] == '+':
        v, i = term(L, i + 1, False)
        res += v

    return res, i


data = [line.strip().replace(' ', '') for line in input('input.txt')]

p1_ans = sum([expr(line, 0)[0] for line in data])
p2_ans = sum([emul(line, 0)[0] for line in data])

print(f'Part one: {p1_ans}, Part two {p2_ans}')
