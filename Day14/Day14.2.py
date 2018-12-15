scores = [3,7]
elf1 = 0
elf2 = 1
input = '990941'
input_digits = list(int(x) for x in input)

done = False
while not done:
    new_score = scores[elf1] + scores[elf2]
    for digit in str(new_score):
        scores.append(int(digit))
        if scores[-len(input_digits)-1:-1] == input_digits:
            print len(scores) - len(input_digits) - 1
            done = True
            break
    elf1 = (elf1 + scores[elf1] + 1) % len(scores)
    elf2 = (elf2 + scores[elf2] + 1) % len(scores)
