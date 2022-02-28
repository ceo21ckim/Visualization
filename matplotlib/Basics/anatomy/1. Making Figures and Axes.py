import matplotlib.pyplot as plt 
import numpy as np

# figsize
fig = plt.figure()
fig = plt.figure(figsize = (7, 7))
plt.show()

# facecolor
fig = plt.figure(figsize=(7, 7), facecolor = 'red')
plt.show()

# add_subplot
fig = plt.figure(figsize = (7, 7), facecolor = 'linen')
ax = fig.add_subplot()
ax.plot([2, 3, 1])
plt.show()


fig = plt.figure(figsize = (7, 7), facecolor = 'linen')
ax = fig.add_subplot()
ax.scatter([2, 3, 1], [2, 3, 4])
plt.show()

fig = plt.figure(figsize = (7, 7), facecolor = 'linen')
fig.add_subplot(111) # add_subplot(row columns 'i'th axes)
plt.show()

fig = plt.figure(figsize = (7, 7), facecolor = 'linen')
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

ax1.scatter([2, 3, 1], [2, 3, 4])
ax2.plot([2, 3, 1])
plt.show()



fig = plt.figure(figsize = (7, 7), facecolor = 'linen')
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax3 = fig.add_subplot(2, 2, 2)
plt.show()


fig = plt.figure(figsize = (7, 7), facecolor = 'linen')
ax1 = fig.add_subplot(311, facecolor='r')
ax2 = fig.add_subplot(312, facecolor='g')
ax3 = fig.add_subplot(313, facecolor='b')
plt.show()


# plt.subplots
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

fig, axes = plt.subplots(nrows=2, ncols=1, facecolor = 'linen')
axes[0]
axes[1]
plt.show()

# plt.subplot2gird / Comparison with other APIs
fig = plt.figure(figsize=(7, 7), facecolor='linen')
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

plt.show()
######################################################################
fig, axes = plt.subplots(2, 1, figsize = (7, 7), facecolor = 'linen')

plt.show()
######################################################################
fig = plt.figure(figsize=(7, 7), facecolor = 'linen')
ax1 = plt.subplot2grid((2, 1), (0, 0), fig = fig)
ax2 = plt.subplot2grid((2, 1), (1, 0), fig = fig)

plt.show()

fig = plt.figure(figsize=(7, 7), facecolor='linen')
ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2, fig=fig)
ax2 = plt.subplot2grid((2, 2), (1, 0), fig = fig)
ax3 = plt.subplot2grid((2, 2), (1, 1), fig = fig)
plt.show()


fig = plt.figure(figsize=(7, 7), facecolor='linen')
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2, fig=fig)
ax1 = plt.subplot2grid((3, 3), (1, 0), colspan=2, fig=fig)
ax1 = plt.subplot2grid((3, 3), (2, 0), colspan=2, fig=fig)
ax1 = plt.subplot2grid((3, 3), (0, 2), colspan=1, rowspan=3, fig=fig)
plt.show()


fig = plt.figure(figsize=(7, 7), facecolor='linen')
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, fig=fig)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, fig=fig)
ax3 = plt.subplot2grid((3, 3), (2, 0), fig=fig)
ax4 = plt.subplot2grid((3, 3), (2, 1), fig=fig)
ax5 = plt.subplot2grid((3, 3), (1, 2), rowspan=2, fig=fig)
plt.show()


fig = plt.figure(figsize=(25, 20))
ax1 = plt.subplot2grid((2, 2), (0, 0), rowspan=2, fig = fig)
ax2= plt.subplot2grid((2, 2), (0, 1), projection = '3d', fig=fig)
ax2= plt.subplot2grid((2, 2), (1, 1), projection = '3d', fig=fig)
plt.show()
