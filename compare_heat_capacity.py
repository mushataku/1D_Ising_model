import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

spinnums = ["50", "100", "500", "1000"]
spinnum = "50"

df = pd.read_csv("data/spin"+spinnum+"/heat_capacity.csv")


T = df["T"]
analytic = df["analytic"]
analytic2 = df["analytic2"]

FILE_PATH = "compare_heat_capacity"

#plt.rcParams["font.family"] = "Times New Roman"

fig = plt.figure(figsize=(12, 8))
# fig.subplots_adjust(left=0.80)
ax = fig.add_subplot(111)

ax.plot(T, analytic, label="analytic")
for spinnum in spinnums:
  df = pd.read_csv("data/spin"+spinnum+"/heat_capacity.csv")
  numeric = df["numerical"]
  if(spinnum == "100"):
    ax.plot(T, numeric, "ro-", label="N = "+spinnum)
  elif(spinnum == "1000"):
    ax.plot(T, numeric, "bo-", label="N = "+spinnum)
  else:
    ax.plot(T, numeric, "o-", label="N = "+spinnum)

#ax.plot(T, C_analytic2,"--", label="analytic2")
ax.set_ylabel(r"Heat Capacity c", fontsize=24)
ax.set_xlabel(r"Temperature $\tau$", fontsize=24)
ax.grid(linestyle="dotted")
ax.xaxis.set_tick_params(direction='in')
ax.yaxis.set_tick_params(direction='in')
ax.set_xticks(np.arange(0, 5.1, 0.5))
#ax.set_yscale("log")
ax.tick_params(labelsize=20)  # 軸目盛の数字のサイズ
ax.legend(fontsize=20)
# os.mkdir("fig")
plt.savefig("fig/"+FILE_PATH+".png")
plt.savefig("report_tex/"+FILE_PATH+".png")

plt.show()
