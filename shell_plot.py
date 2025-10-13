from pairings.util import *
import matplotlib.pyplot as plt

fig, axs = plt.subplots(ncols=2)

N = 4
for d in range(2*N+1):
    i = list(range(max(0, d-N), min(d, N)+1))
    axs[0].plot(i, list(reversed(i)), lw=0.5, c='C1')
    axs[0].text(d/2, d/2, f'${d}$', c='C0', ha='center', va='center')
axs[0].set_title('diagonal')
axs[0].set_aspect('equal')
axs[0].set_xlabel('$i$')
#axs[0].set_xticks(tuple(range(N+1)))
axs[0].set_ylabel('$j$')
axs[0].set_yticks(tuple(range(N+1)))
axs[0].grid(lw=0.25)

for d in range(N+1):
    i = list(range(d+1)) + [d]*d
    j = [d]*d + list(reversed(range(d+1)))
    axs[1].plot(i, j, lw=0.5, c='C1')
    axs[1].text(d, d, f'${d}$', c='C0', ha='center', va='center')
axs[1].set_title('cubic')
axs[1].set_aspect('equal')
axs[1].set_xlabel('$i$')
#axs[0].set_xticks(tuple(range(N+1)))
axs[1].set_ylabel('$j$')
axs[1].set_yticks(tuple(range(N+1)))
axs[1].grid(lw=0.25)

fig.tight_layout()
fig.savefig('docs/shells.png', dpi=600)
#plt.show()
