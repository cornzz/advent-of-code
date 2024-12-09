X = open("input.txt").read().strip()

mem, file = [], 0
for i, c in enumerate(X):
    if i % 2:
        mem.extend(["."] * int(c))
    else:
        mem.extend([file] * int(c))
        file += 1

def defrag(mem, p1=True):
    if p1:
        free = 0
        for idx in range(len(mem) - 1, -1, -1):
            while mem[free] != ".":
                free += 1
            if idx < free:
                break
            if mem[idx] != ".":
                mem[free], mem[idx] = mem[idx], mem[free]
    else:
        idx = len(mem) - 1
        while idx >= 0:
            while mem[idx] == ".":
                idx -= 1
            file, file_len = mem[idx], 0
            while mem[idx] == file:
                file_len += 1
                idx -= 1
            free, free_len = 0, 0
            while free <= idx:
                free_len = free_len + 1 if mem[free] == "." else 0
                free += 1
                if free_len == file_len:
                    mem[free - file_len : free] = mem[idx + 1 : idx + 1 + file_len]
                    mem[idx + 1 : idx + 1 + file_len] = ["."] * file_len
                    break
    return mem

mem_p1 = defrag(mem.copy())
mem_p2 = defrag(mem.copy(), False)
p1 = sum(file * i for i, file in enumerate(mem_p1) if file != ".")
p2 = sum(file * i for i, file in enumerate(mem_p2) if file != ".")
print(p1)
print(p2)
