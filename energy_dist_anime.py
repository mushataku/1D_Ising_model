import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import os

def set_ax(ax):
  ax.set_ylabel("number of times", fontsize=21)
  ax.set_xlabel("energy E/NJ", fontsize=21)
  ax.grid(linestyle="dotted")
  ax.xaxis.set_tick_params(direction='in')
  ax.yaxis.set_tick_params(direction='in')
  ax.tick_params(labelsize=21)  # 軸目盛の数字のサイズ
  ax.set_yscale("log")
  ax.set_ylim(ymin=1, ymax=1e7)
  ax.set_title("1D Ising model", fontsize=24)

##########CONFIG###########
GIF = 0
MP4 = 0
PLT = 1
###########################

T = np.arange(0.1, 8.02, 0.02)



FILE_PATH = 'energy_histo'

fig = plt.figure(figsize=(14, 8))
# fig.subplots_adjust(left=0.80)
ax = fig.add_subplot(111)



set_ax(ax)

fp = "data/spin100/energy_dist/spin100_T%.3f.csv" % T[0]
df = pd.read_csv(fp)
Energy = df["Energy"]

ax.hist(Energy/100, bins=33, ec="black", align="left", range=(-1.0,0.28), rwidth=30, color="b")


def animate(cnt):
  if(cnt != 0):
    ax.clear()
  set_ax(ax)
  fp = "data/spin100/energy_dist/spin100_T%.3f.csv"%T[cnt]
  df = pd.read_csv(fp)
  Energy = df["Energy"]
  ax.hist(Energy/100, bins=33, ec="black", align="left", range=(-1.0, 0.28), rwidth=30, color="b")

  ax.text(0.80, 0.95, r"$\mathrm{k_BT}$/J = %.2f" %
          T[cnt], transform=ax.transAxes, fontsize=20)

  print(cnt)


ani = FuncAnimation(fig, animate, frames=int(len(T))
              , interval=200, repeat=True, blit=False)


if(GIF == 1):
    ani.save("animes/"+FILE_PATH+".gif", writer="pillow", fps=5)
if(MP4 == 1):
    ani.save("animes/"+FILE_PATH+".mp4", writer="ffmpeg", fps=5)
if(PLT == 1):
    plt.show()

