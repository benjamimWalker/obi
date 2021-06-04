b, o, y = (int(i) for i in input().split())
god_we_trust = []

for c in range(b):
    god_we_trust.append(input().split())

earth = input().split()
earth.reverse()
your_thoughts = []
answer = ''

for live in earth:
    for to_be in god_we_trust:
        your_thoughts.append(live in to_be or not to_be)
    if False in your_thoughts:
        your_thoughts.clear()
        for a_prayer in god_we_trust:
            if live in a_prayer:
                a_prayer.clear()
    else:
        break

for yes in god_we_trust:
    if not not yes:
        answer += str(god_we_trust.index(yes) + 1) + ' '

print(answer)
