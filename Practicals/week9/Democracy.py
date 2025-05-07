# Data from https://en.wikipedia.org/wiki/List_of_cities_in_Australia_by_population
# Retrieved 2025-04-30

lgas = [
    ['City of Brisbane', 1355640],
    ['City of Gold Coast', 681389],
    ['City of Moreton Bay', 522494],
    ['City of Blacktown', 438843],
    ['City of Casey', 405415],
    ['City of Logan', 392339],
    ['City of Canterbury-Bankstown', 385242],
    ['Sunshine Coast Region', 375328],
    ['Central Coast Council', 354803],
    ['City of Wyndham', 337009],
    ['City of Greater Geelong', 289565],
    ['City of Parramatta', 274956],
    ['City of Hume', 271709],
    ['Northern Beaches Council', 270772],
    ['City of Ipswich', 259886],
    ['City of Liverpool', 254905],
    ['City of Whittlesea', 253204],
    ['Cumberland Council', 252399],
    ['City of Stirling', 249872],
    ['Sutherland Shire', 238614],
    ['City of Wanneroo', 237628],
    ['City of Sydney', 237278],
    ['City of Penrith', 228661],
    ['City of Wollongong', 221894],
    ['City of Lake Macquarie', 221859],
    ['City of Melton', 219697],
    ['The Hills Shire', 215612],
    ['City of Fairfield', 212210],
    ['City of Monash', 209268],
    ['City of Townsville', 204541],
    ['City of Brimbank', 198152],
    ['Inner West Council', 190939],
    ['City of Melbourne', 189381],
    ['City of Campbelltown', 188303],
    ['City of Merri-bek', 186534],
    ['Bayside Council', 185880],
    ['Toowoomba Region', 184377],
    ['City of Whitehorse', 183462],
    ['City of Onkaparinga', 182821],
    ['City of Swan', 179207],
    ['Cairns Region', 178104],
    ['City of Boroondara', 178008],
    ['City of Newcastle', 176860],
    ['City of Joondalup', 173469],
    ['Shire of Mornington Peninsula', 171450],
    ['Redland City', 170225],
    ['City of Greater Dandenong', 167298],
    ['City of Kingston', 166521],
    ['City of Knox', 163302],
    ['Georges River Council', 161593]
]

L = range(len(lgas))

seats = 100

population = sum(lgas[j][1] for j in L)
target = [seats * lgas[j][1]/population for j in L]

_V = {}

def V(j, s):
    if (j, s) in _V:
        return _V[j,s]
    
    if j == 49:

        _V[j,s] = (abs(s - target[j]), s)
    else:
        _V[j,s] = min((max(abs(a - target[j]), V(j + 1, s - a)[0]), a)
                      for a in range(0, s + 1)) 
    return _V[j,s]

print(V(0,100))

def representatives():
    s = seats
    for j in L:
        v = V(j, s)
        print(lgas[j][0], v[1], round(abs(v[1]-target[j]), 3))
        s = s - v[1]

representatives()

