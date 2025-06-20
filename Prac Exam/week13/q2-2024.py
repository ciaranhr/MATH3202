# Data
online = 80
costs = [30,40,45,50,55]
ps = [.2,.4,.7,.7,.9]

#stage is location
#state is current prob score(p) and shops you have travelled to (s) 
#action is visit or skip
#value is min expected cost  if we are at store j with s visits remaining
def shopaholic(j, s):
    #base case is when you are visiting the 3rd store
    if s == 0 or j == 5:
        return (online, 'poor')
    else:
        #in shop or not in shop
        visit = (ps[j]*costs[j] + (1-ps[j])*shopaholic(j+1, s-1)[0], "Visit")
        skip = (shopaholic(j+1,s)[0], "skip")
        return min(visit, skip)
    
print(shopaholic(0, 2))



visits = 2
j = 0
while True:
    v = shopaholic(j, visits)
    print(j, v[1])
    if v[1] == "Online":
        break
    if v[1] == "Visit":
        visits -= 1
    j += 1




