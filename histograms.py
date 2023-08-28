import pandas as pd
import matplotlib.pyplot as plt
import statistics as st

plt.style.use('seaborn-deep')

data = pd.read_csv("histosdata.csv")

z1 = (data["z1"])
z1 = list(z1)

z2 = (data["z2"])
z2 = list(z2)

entries = len(z1)+len(z2)
print('zs: ', entries)

h = (data["h"])
h = list(h)

print('Hs: ', len(h))

z = z1 + z2

print(st.mean(z),' ',st.stdev(z))
print(st.mean(h),' ',st.stdev(h))

plt.title("$Z^{0}$ mass \n H range: 124 to 126 GeV")
plt.hist(z,100,(min(z),max(z)),color="firebrick")
plt.legend(['Entries: 350 \n Mean: 52 GeV \n Stdev: 27 GeV'])
plt.xlabel("$Z^{0}$ mass (GeV)")
plt.ylabel("Frequency")
plt.savefig('fig4.png',dpi=200)
plt.show()
plt.title("$H$ mass \n H range: 124 to 126 GeV")
plt.hist(h,100,color="firebrick")
plt.legend(['Entries: 175 \n Mean: 125 GeV \n Stdev: 0.2 GeV'])
plt.xlabel("$H$ mass (GeV)")
plt.ylabel("Frequency")
plt.savefig('fig5.png',dpi=200)
plt.show()
