import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

datafull = pd.read_csv("datafull2.csv")
dataon = pd.read_csv("dataon2.csv")
histosdata = open("histosdata.csv","w")
writer = csv.writer(histosdata)

writer.writerow(["z1","z2","h"])

onevents = (dataon["i"])
onevents = list(onevents)

onid = (dataon["id"])
onid = list(onid)

onpx = (dataon["px"])
onpx = list(onpx)

onpy = (dataon["py"])
onpy = list(onpy)

onpz = (dataon["pz"])
onpz = list(onpz)

eon = []

globalzm = []
globalhm = []

#get the total energy of each lepton
def pabs(x,y,z):
    return np.sqrt(x**2 + y**2 + z**2)

for i in range(len(onevents)):
    if onid[i] == 15 or onid[i] == -15:
        eon.append(np.sqrt(1.777**2 + onpx[i]**2 + onpy[i]**2 + onpz[i]**2))
    else:
        eon.append(pabs(onpx[i],onpy[i],onpz[i]))

#z0 reconstructor
def reconstructor(ind1,ind2):
    z0e = eon[ind1] + eon[ind2]
    z0px = onpx[ind1]+onpx[ind2]
    z0py = onpy[ind1]+onpy[ind2]
    z0pz = onpz[ind1]+onpz[ind2]
    z0pabs = np.sqrt(z0px**2 + z0py**2 + z0pz**2)
    z0m = np.sqrt(z0e**2 - z0px**2 - z0py**2 - z0pz**2)
    return [z0px,z0py,z0pz,z0m,z0pabs,z0e]

def deleter(l1,l2,l3,l4,l5):
    del l3[l2.index(l1[0])]
    l2.remove(l1[0])
    del l4[0]
    del l5[0]
    del l1[0]
    return 0

def smalldeleter(l1,l2,l3):
    del l3[l2.index(l1[0])]
    l2.remove(l1[0])
    del l1[0]
    return 0

def zappender(l1,l2,l3,l4,l5,l6):
    l2.append(l1[0])
    l3.append(l1[1])
    l4.append(l1[2])
    l5.append(l1[-1])
    l6.append(l1[3])
    return 0

# def scan(lepton_list):
#     for i in range(len(lepton_list)):
#         if lepton_list[i] > 10:


k = 0
# for i in range(len(onevents)):
#     if k == onevents[i]:
#
i = 0
total_events = max(onevents)

while k <= total_events:#loop through all events
    # print("Event: ",k)
    muminus = []
    muminusindex = []
    muplus = []
    muplusindex = []
    eminus = []
    eminusindex = []
    eplus = []
    eplusindex = []
    tauminus = []
    tauminusindex = []
    tauplus = []
    tauplusindex = []
    all = []
    # i = i + k
    while True:#get all leptons on the event
        if i >= len(onevents)-1:
            break
        if onevents[i] != k:#change of the event
            k += 1
            break
        else:#append each lepton
        # leptonenergy = pabs(onpx[i],onpy[i],onpz[i])
            # print("first else")
            all.append(eon[i])
            if onid[i] == 11 and eon[i] > 10:
                muminus.append(eon[i])
                muminusindex.append(i)
                i += 1
                if i >= len(onevents)-1:
                    break
            elif onid[i] == -11 and eon[i] > 10:
                muplus.append(eon[i])
                muplusindex.append(i)
                i += 1
                if i >= len(onevents)-1:
                    break
            elif onid[i] == 13 and eon[i] > 10:
                eminus.append(eon[i])
                eminusindex.append(i)
                i += 1
                if i >= len(onevents)-1:
                    break
            elif onid[i] == -13 and eon[i] > 10:
                eplus.append(eon[i])
                eplusindex.append(i)
                i += 1
                if i >= len(onevents)-1:
                    break
            elif onid[i] == 15 and eon[i] > 10:
                tauminus.append(eon[i])
                tauminusindex.append(i)
                i += 1
                if i >= len(onevents)-1:
                    break
            elif onid[i] == -15 and eon[i] > 10:
                tauplus.append(eon[i])
                tauplusindex.append(i)
                i += 1
                if i >= len(onevents)-1:
                    break
            else:
                i += 1
                if i >= len(onevents)-1:
                    break
    #logic to reconstruct z0
    #to add: check if the four selected leptons exceed the 125GeV Higgs mass
    c = 1
    zm = []
    ze = []
    zpx = []
    zpy = []
    zpz = []
    while c < 3:
        lepton_count = len(muminus)+len(muplus)+len(eminus)+len(eplus)+len(tauminus)+len(tauplus)
        if lepton_count >= 2:
            all.sort(reverse=True)
            if all[0] in muminus:
                if len(muplus) > 0:
                    #reconstruir z0
                    z0 = reconstructor(muminusindex[muminus.index(all[0])],muplusindex[0])
                    # print(z0)
                    zappender(z0,zpx,zpy,zpz,ze,zm)
                    # zpx.append(z0[0])
                    # zpy.append(z0[1])
                    # zpz.append(z0[2])
                    # ze.append(z0[-1])
                    deleter(all,muminus,muminusindex,muplus,muplusindex)
                    # del muminusindex[muminus.index(all[0])]
                    # muminus.remove(all[0])
                    # del muplus[0]
                    # del muplusindex[0]
                    # del all[0]
                    c += 1
                else:
                    smalldeleter(all,muminus,muminusindex)
                    # del muminusindex[muminus.index(all[0])]
                    # muminus.remove(all[0])
                    # del all[0]
            elif all[0] in muplus:
                if len(muminus) > 0:
                    z0 = reconstructor(muplusindex[muplus.index(all[0])],muminusindex[0])
                    # print(z0)
                    zappender(z0,zpx,zpy,zpz,ze,zm)
                    deleter(all,muplus,muplusindex,muminus,muminusindex)
                    c += 1
                else:
                    smalldeleter(all,muplus,muplusindex)
            elif all[0] in eminus:
                if len(eplus) > 0:
                    z0 = reconstructor(eminusindex[eminus.index(all[0])],eplusindex[0])
                    # print(z0)
                    zappender(z0,zpx,zpy,zpz,ze,zm)
                    deleter(all,eminus,eminusindex,eplus,eplusindex)
                    c += 1
                else:
                    smalldeleter(all,eminus,eminusindex)
            elif all[0] in eplus:
                if len(eminus) > 0:
                    z0 = reconstructor(eplusindex[eplus.index(all[0])],eminusindex[0])
                    # print(z0)
                    zappender(z0,zpx,zpy,zpz,ze,zm)
                    deleter(all,eplus,eplusindex,eminus,eminusindex)
                    c += 1
                else:
                    smalldeleter(all,eplus,eplusindex)
            elif all[0] in tauminus:
                if len(tauplus) > 0:
                    z0 = reconstructor(tauminusindex[tauminus.index(all[0])],tauplusindex[0])
                    # print(z0)
                    zappender(z0,zpx,zpy,zpz,ze,zm)
                    deleter(all,tauminus,tauminusindex,tauplus,tauplusindex)
                    c += 1
                else:
                    smalldeleter(all,tauminus,tauminusindex)
            elif all[0] in tauplus:
                if len(tauminus) > 0:
                    z0 = reconstructor(tauplusindex[tauplus.index(all[0])],tauminusindex[0])
                    # print(z0)
                    zappender(z0,zpx,zpy,zpz,ze,zm)
                    deleter(all,tauplus,tauplusindex,tauminus,tauminusindex)
                    c += 1
                else:
                    smalldeleter(all,tauplus,tauplusindex)
            else:
                c = 3
        else:
            c = 3
    #logic to reconstruct H0
    if len(ze) > 1:
        he = ze[0] + ze[1]
        hpx = zpx[0] + zpx[1]
        hpy = zpy[0] + zpy[1]
        hpz = zpz[0] + zpz[1]
        hpabs = np.sqrt(hpx**2 + hpy**2 + hpz**2)
        hm = np.sqrt(he**2 - hpx**2 - hpy**2 - hpz**2)
        # if hm > 124.8 and hm < 125.1:
        if hm > 124 and hm < 126:
            # globalzm.append(zm[0])
            # globalzm.append(zm[1])
            # globalhm.append(hm)
            data = [zm[0],zm[1],hm]
            writer.writerow(data)
            print("Event: ",k-1)
            print("HIGGS")
            print(hm,hpabs,he)
    else:
        c = 3
        # else:
        #     print("No Higgs")
    # else:
    #     print("No Higgs")
# plt.hist(globalzm)
# plt.show()
# plt.hist(globalhm)
# plt.show()
