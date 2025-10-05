from pairings.nz import *
import matplotlib.pyplot as plt

fig, axs = plt.subplots(ncols=2)



i = tuple(range(-5, +6))
n = tuple(map(fold, i))
axs[0].scatter(i, n, marker='x')
axs[0].plot(i, n, lw=0.5, c='C1')

axs[0].set_title('fold')
axs[0].set_xlabel('$i$')
axs[0].set_xticks(tuple(range(-5, +6, 2)))
axs[0].set_ylabel('$n$')
#axs[0].set_yticks(tuple(range(0, 11, 2)))


n = tuple(range(11))
i = tuple(map(unfold, n))
axs[1].scatter(n, i, marker='x')
axs[1].plot(n, i, lw=0.5, c='C1')

axs[1].set_title('unfold')
axs[1].set_xlabel('$n$')
axs[1].set_xticks(tuple(range(0, 11, 2)))
axs[1].set_ylabel('$i$')
axs[1].set_yticks(tuple(range(-5, +6, 2)))


fig.tight_layout()
fig.savefig('docs/nz.png', dpi=600)
