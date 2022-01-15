n = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]''' 

n = open("input.txt")

s = [list(x) for x in n.read().strip().split("\n")]

total = 0

tot_score = []

opened = ["[", "{", "(", "<"]
closed = ["]", "}", ")", ">"]

d = {"]":"[", "}":"{", ")":"(", ">":"<"}
score = {"]":57, "}":1197, ")":3, ">":25137}
new_score = {"]":2, "}":3, ")":1, ">":4}

for i in range(len(s)):
  open = []
  for j in range(len(s[i])):
    if s[i][j] in opened:
      open.append(s[i][j])
    else:
      if open[-1] != d[s[i][j]]:
        total += score[s[i][j]]
        break
      else:
        open = open[:-1]
  else:
    temp_score = 0
    for i in range(len(open) - 1, -1, -1):
      temp_score *= 5
      temp_score += new_score[closed[opened.index(open[i])]]
    tot_score.append(temp_score)

tot_score.sort()
  
print(total)
print(tot_score[len(tot_score)//2])
        
  