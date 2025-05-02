#Data
salesH = 800
salesL = 600
costA = 70
costP = 80

pHY = 0.8
pHN = 0.6
pLY = 0.6
pLN = .2

#Stages = Weeks

# ACtions - Advertise or not

# State - High or Low

def advertise(t,s):
    if t == 5:
        return (0, "Done")
    else:
        if s == "High":
            yes = pHY *(salesH + advertise(t+1, "High")[0]) + \
            (1 - pHY) * (salesL - costP + advertise(t+1, "Low")[0]) - costA
            no = pHN *(salesH + advertise(t+1, "High")[0]) + \
            (1 - pHY) * (salesL - costP + advertise(t+1, "Low")[0])
        else:
            yes = pLY *(salesH - costP + advertise(t+1, "High")[0]) + \
            (1 - pHY) * (salesL + advertise(t+1, "Low")[0]) - costA
            no = pLN *(salesH - costP + advertise(t+1, "High")[0]) + \
            (1 - pLN) * (salesL + advertise(t+1, "Low")[0])
            
        return max([(yes, "Yes"), (no, "No")])

print(advertise(1, "High"))
print(advertise(1, "Low"))