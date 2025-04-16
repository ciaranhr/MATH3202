ps = [
    [.2, .3, .35, .38, .4],
    [.25, .3, .33, .35, .38],
    [.1, .3, .4, .45, .5]
]

def minStudy(t, s):
    if t == 3:
        return (1, None)
    else:
        min_prob = (1, None)
        for a in range(s + 1):
            p = (1-ps[t][a]) * (minStudy(t+1, s-a)[0])
            if p < min_prob[0]:
                min_prob = (p, a, s-a)
        return min_prob


def sol():
    subjects = ["Algebra", "Calculus", "Statistics"]
    s = 4
    for t in range(len(subjects)):
        v = minStudy(t, s)

        if t == 0:
            print("probability of passing at least one course is", 1-v[0])

        print(v[1], "hours for", subjects[t])
        s = v[2]

sol()


