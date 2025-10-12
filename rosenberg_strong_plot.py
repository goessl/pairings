from pairings.rosenberg_strong import *
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

xs, ys = zip(*map(depair, range(25)))
ax.plot(xs, ys, lw=0.5, c='C1')
for n, (x, y) in enumerate(zip(xs, ys)):
    ax.text(x, y, f'${n}$', c='C0', ha='center', va='center')

ax.set_title('Rosenberg-Strong')
ax.set_xlabel('$i$')
ax.set_xticks(tuple(range(4+1)))
ax.set_ylabel('$j$')
ax.set_yticks(tuple(range(4+1)))
fig.tight_layout()
fig.savefig('docs/rosenberg_strong.png', dpi=600)
#plt.show()
