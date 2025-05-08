"""
Created on Wed Mar 12 15:22:32 2025

MATH3202_A3
Brolga Fire Management: Feral Pig Control
KOBI WICKENS
CIARAN HUANG-RYAN
SACHITH PANDITHA 
"""
# DATA
def damage(t):
    """
    Environmental damage caused by pigs

    Parameters
    ----------
    t : int
        week of year

    Returns
    -------
    d : float
        Damage unit per pig.

    """
    d = 2
    dt = min(abs(t-2), abs((52+t)-2), abs(t-(52+2)))
    if dt < 10:
        d += 8*(1-(dt/10)**2)**2
    dt = min(abs(t-21), abs((52+t)-21), abs(t-(52+21)))
    if dt < 7:
        d += 6*(1-(dt/7)**2)**2
    return d


def reprod(x):
    """
    Pig reproduction

    Parameters
    ----------
    x : int
        Current Pig Population

    Returns
    -------
    int
        New Pig Population Due to Breeding

    """
    if x <= 0:
        return 0
    else:
        return round(x + x*(420-x)/5000)

    
def trap(x):
    """
    Pigs murdered for a single trap

    Parameters
    ----------
    x : int
        Current pig population

    Returns
    -------
    int
        Expected number ofpigs trapped

    """
    return round(.03*x)

traps = 27
trap_max = 4
pig_init = 74


_strategy = {}
## Key: [week, pig population], Value: (damage, action, traps remaining)
def strategy(t,s,y):
    """
    Function to determine optimal trap deployment strategy

    Parameters
    ----------
    d : float
        Total Damage inflicted
    s : int (STATE)
        Pig Population
    y : int
        Traps available
    t : int (STAGE)
        week 0-51

    """
    #Base Case
    if t == 52:
        return (0, "Year Finished")
    
    #Recursive Case
    elif (t, s, y) not in _strategy:
        if y == 0:
           _strategy[t,s, y] = (damage(t)*s) + strategy(t+1,reprod(s),y)[0],0
        elif y > 0:
            _strategy[t,s, y] = min((damage(t)*s + strategy(t+1,reprod(s)-a*trap(s),y-a)[0],a) 
                                for a in range(min(trap_max, y) + 1)) 
    return _strategy[t,s, y]


print(strategy(0, 82, 1)) 