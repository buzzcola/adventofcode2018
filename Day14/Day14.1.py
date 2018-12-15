scores = [3,7]
elf1 = 0
elf2 = 1
input = 990941
answer_length = 10

while len(scores) < input + answer_length:
    new_score = scores[elf1] + scores[elf2]
    for digit in str(new_score):
        scores.append(int(digit))
    elf1 = (elf1 + scores[elf1] + 1) % len(scores)
    elf2 = (elf2 + scores[elf2] + 1) % len(scores)

print ''.join(str(x) for x in scores[input:input + answer_length])