W = [4,8,12]

prey = { 4: .66, 8: .77, 12: .82 }
caught = { 4: .01, 8: .02, 12: .03 }

food = 6

def alpha(w,s):
    return -.125*w + .005*w*s + .4

def dweb(t,s):
    # uncomment to return to the un-discretised version
    # return V(t,s)[0]
    x = int(s)
    p = s - x
    return p*V(t,x+1)[0] + (1-p)*V(t,x)[0]

_V = {}
def V(t,s):
    if s >= 80:
        return (1, "Success")
    elif s < 25:
        return (0, "Died")
    elif t == 11:
        return (0, "Too late")
    else:
        if not (t,s) in _V:
            _V[t,s] = max(  
                ((1-caught[w])*prey[w]*dweb(t+1,s+food-alpha(w,s)) +
                (1-caught[w])*(1-prey[w])*dweb(t+1,s-alpha(w,s)) +
                caught[w]*0, w) 
                for w in W)
        return _V[t,s]