
p_food = 0.6
p_mate = 0.004
food = 32

d_rest = 3.6

def d_sing(s):
    return 12 + 0.002 *s
    
def d_forage(s):
    return 8 + 0.007 *s

def dsong(t, s, m):
    x = s//1
    p = s - x
    return p * song(t, x + 1, m)[0] + (1 - p) * song(t, x, m)[0]

_song = {}
def bsong(t, s, m):
    return .25*dsong(t, s-6.4, m) + .5*dsong(t, s, m) + .25*dsong(t, s+6.4,m)

def song(t, s, m):
    if s <= 0:
        return (0, "Dead")
    
    if t == 150:
        if s > 0:
            if m == "Yes":
                return  (2, "Yes Mate")
            elif m == "No":
                return (1, "No Mate")
    if (t, s, m) not in  _song:

        if t >= 75:
            _song[t, s, m] = (dsong(t + 1, s- d_rest, m)), "Rest"
        else:
            rest = dsong(t + 1, s - d_rest, m)

            sing = 0.004 * bsong(t + 1, s - d_sing(s), "Yes") + \
            (1-.004) * bsong(t + 1, s - d_sing(s), m)

            forage = 0.6 * bsong(t + 1, s - d_forage(s) + food, m) + \
                0.4 * bsong(t + 1, s - d_forage(s), m)
            
            _song[t, s, m] = max((rest, "Rest"), (sing, "Sing"), (forage, "Forage"))

    return _song[t, s, m]
    
print(song(0, 100, "No"))