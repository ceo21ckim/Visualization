# fig.tight_layout

import enum
import numpy as np 
import matplotlib.pyplot as plt 

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_title('Title!', fontsize=20)
ax.set_xlabel('X Label!', fontsize=15)
ax.set_ylabel('Y Label!', fontsize=15)
plt.show()

title_list = ['Ax' + str(i) for i in range(4)]
xlabel_list = ['X Label ' + str(i) for i in range(4)]
ylabel_list = ['Y Label ' + str(i) for i in range(4)]

fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for ax_idx, ax in enumerate(axes.flat):
    ax.set_title(title_list[ax_idx], fontsize=20)
    ax.set_xlabel(xlabel_list[ax_idx], fontsize=20)
    ax.set_ylabel(ylabel_list[ax_idx], fontsize=20)
plt.show()



fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for ax_idx, ax in enumerate(axes.flat):
    ax.set_title(title_list[ax_idx], fontsize=20)
    ax.set_xlabel(xlabel_list[ax_idx], fontsize=20)
    ax.set_ylabel(ylabel_list[ax_idx], fontsize=20)
fig.tight_layout(pad = 3) # tight_layout을 설정해주면 안겹치게 잘 그려준다. pad를 지정해서 간격을 넓혀줄 수 있다. 
plt.show()


# fig.subplots_adjust
# set_visible -> axis를 없애준다. 
fig, ax = plt.subplots(figsize=(10, 10))

xaxis = ax.get_xaxis()
yaxis = ax.get_yaxis()

xaxis.set_visible(False)
yaxis.set_visible(False)
plt.show()


fig, ax = plt.subplots(figsize=(10, 10))
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for ax_idx, ax in enumerate(axes.flat):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()


# fig.subplots_adjust(Position Arguments)
# left, bottom은 0에 가까울수록 붙고, top, right는 1에 가까울수록 완전히 화면에 붙어버림.
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for ax_idx, ax in enumerate(axes.flat):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
fig.subplots_adjust(bottom = 0.01, top = 0.99)
fig.subplots_adjust(left=0, right=1)
plt.show()


fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for ax_idx, ax in enumerate(axes.flat):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
fig.subplots_adjust(bottom = 0.01, top = 0.99, left = 0.05, right = 0.8)
plt.show()


fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for ax_idx, ax in enumerate(axes.flat):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
fig.subplots_adjust(hspace = 0.5) # 상하 간격
plt.show()


fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for ax_idx, ax in enumerate(axes.flat):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
fig.subplots_adjust(wspace = 0.9) # 좌우 간격
plt.show()


# fig.subplots_adjust(Spacing Arguments)
fig, axes = plt.subplots(3, 3, figsize = (10, 10))

for idx, ax in enumerate(axes.flat):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
fig.subplots_adjust(hspace=0.2, wspace=0.05)


fig = plt.figure(figsize=(12, 13))
axes_g1 = np.empty(shape = (0,))
main = plt.subplot2grid((5, 4), (0, 0), 2, 2, fig = fig)  # (0,0) 위치에 2 by 2 짜리 그림.
axes_g1 = np.append(axes_g1, main)

for r_idx in range(2, 2 + 3):
    for c_idx in range(2):
        ax = plt.subplot2grid((5, 4), (r_idx, c_idx), fig = fig)
        axes_g1 = np.append(axes_g1, ax)
        
axes_g1 = axes_g1.reshape(1, -1)
print(axes_g1.shape)


# fig.subplots_adjust(Practice)
axes_g2 = np.empty(shape=(0,))
main = plt.subplot2grid((5, 4), (0, 2), 2, 2, fig=fig)
axes_g2 = np.append(axes_g2, main)
for r_idx in range(2, 2+3):
    for c_idx in range(2, 2+2):
        ax = plt.subplot2grid((5, 4), (r_idx, c_idx), fig=fig)
        
        axes_g2 = np.append(axes_g2, ax)
        
axes_g2 = axes_g2.reshape(1, -1)
print(axes_g2.shape)
plt.show()


# Axis sharing
# sharing하게 되면 겹치는 axis는 사라진다.
fig, axes = plt.subplots(2, 2, figsize=(7, 7))
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(7, 7), sharey=True)
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True, sharey=True)
plt.show()


############################################################################
fig, axes = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
fig.subplots_adjust(bottom=0.05, top=0.95, left=0.05, right=0.95, hspace=0.05)
axes[0].set_xlim([10, 1000])
plt.show()

############################################################################
fig, axes = plt.subplots(2, 2 , figsize=(10, 10), sharex=True, sharey=True)

fig.subplots_adjust(bottom=0.05, top=0.95, left=0.05, right=0.95, hspace=0.1, wspace=0.1)
axes[0, 0].set_xlim([0, 120])
axes[0, 0].set_ylim([0, 1])
plt.show()


# fig.add_subplot
fig, axes = plt.subplots(2, 1, figsize=(7, 7), sharex=True)
axes[0].set_xlim([0, 100])
plt.show()

fig = plt.figure(figsize=(7, 7))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212, sharex=ax1)  # add_subplot을 사용하려면 ax2에 sharex=ax1로 해주어야된다.
ax2.set_xlim([0, 100])


############################################################################
fig = plt.figure(figsize=(10, 10))
ax1_1 = fig.add_subplot(221)
ax1_2 = fig.add_subplot(222, sharey=ax1_1)

ax2_1 = fig.add_subplot(223, sharex=ax1_1)
ax2_2 = fig.add_subplot(224, sharey=ax2_1, sharex=ax1_2)

ax1_1.set_ylim([-10, 10])
ax2_1.set_ylim([0, 100])
ax2_1.set_xlim([0, 20])
ax2_2.set_xlim([20, 40])

fig.tight_layout()
plt.show()


############################################################################
fig = plt.figure(figsize=(10, 10))

left, bottom = 0.05, 0.05
spacing = 0.05 
width1, height1 = 0.6, 0.6 
width2 = 1 - (2*left + spacing + width1)
height2 = 1 - (2*bottom + spacing + height1)

rect1 = [left, bottom, width1, height1]
rect2 = [left, bottom + height1 + spacing, width1, height2]
rect3 = [left + width1 + spacing, bottom, width2, height1]

ax1 = fig.add_axes(rect1)
ax2 = fig.add_axes(rect2)
ax3 = fig.add_axes(rect3)

plt.show()


############################################################################
fig = plt.figure(figsize=(20, 10))
n_row, n_col = 3, 4
axes = np.empty(shape=(0, n_col))

xlabel_list = [f'Iteration {i}1' for i in range(4)]
ylabel_list = ['Log-Likelihood', 'Negative Grad.', 'Probability']

for r_idx in range(n_row):
    axes_row = np.empty(shape=(0, ))
    
    for c_idx in range(n_col):
        ax = fig.add_subplot(n_row, n_col, n_col*r_idx + c_idx + 1)
        
        # plotting 
        ax.plot([], marker='|', color='b', label='regression')
        ax.plot([], marker='o', color='r', label='cross entropy')
        ax.plot([], marker='v', color='g', label='target')
        ax.legend()
        axes_row = np.append(axes_row, ax)
        
    axes = np.vstack((axes, axes_row))
    
# set xylabels 
for ax_idx, ax in enumerate(axes.flat):
    if ax_idx % n_col == 0:
        ax.set_ylabel(ylabel_list[ax_idx // n_col], fontsize=20)
        
    if ax_idx >= 2*n_col:
        ax.set_xlabel(xlabel_list[ax_idx - 2*n_col], fontsize=20)

fig.tight_layout()
plt.show()


##################################################################

fig = plt.figure(figsize=(20, 10))
n_row, n_col = 3, 4
axes = np.empty(shape=(0, n_col))

xlabel_list = [f'Iteration {i}1' for i in range(4)]
ylabel_list = ['Log-Likelihood', 'Negative Grad.', 'Probability']

for r_idx in range(n_row):
    axes_row = np.empty(shape=(0, ))
    
    for c_idx in range(n_col):
        ax = fig.add_subplot(n_row, n_col, n_col*r_idx + c_idx + 1)
        
        # plotting 
        ax.plot([], marker='|', color='b', label='regression')
        ax.plot([], marker='o', color='r', label='cross entropy')
        ax.plot([], marker='v', color='g', label='target')
        ax.legend()
        axes_row = np.append(axes_row, ax)
        
    axes = np.vstack((axes, axes_row))
    
axes[0, 0].set_ylim([1.5, 2.0])
axes[1, 0].set_ylim([-0.7, 0.7])
axes[2, 0].set_ylim([0, 0.14])
plt.show()



#################################################################
# ax.twinx

import matplotlib.pyplot as plt
import numpy as np

PI = np.pi 
t = np.linspace(0.01, 5*PI, 100)
sin = np.sin(t)
exp = np.exp(t)

fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot()

ax1.plot(t, sin)
ax1.plot(t, exp)
plt.show()

#################################################################
fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot()
ax1.plot(t, sin)

ax2 = ax1.twinx()
ax2.plot(t, exp)
plt.show()

#################################################################
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot()
ax2 = ax1.twinx()

ax1.set_xlim([0,100])
plt.show()

ax1.set_xlim([0, 100])
ax1.set_ylim([0, 100])
ax2.set_ylim([0, 0.1])
plt.show()

#################################################################
fig = plt.figure(figsize=(7, 7))

ax1 = fig.add_subplot()
ax2 = ax1.twinx()

ax1.set_ylim([0, 100])
ax1.set_ylim([0, 100])
ax2.set_ylim([0, 0.1])

ax1.set_title('Twinx Graph', fontsize=30)
ax1.set_ylabel('Data1', fontsize=20)
ax2.set_ylabel('Data2', fontsize=20)
fig.tight_layout()
plt.show()


#################################################################
# ax.set_yscale(Log Scale)

t = np.linspace(0, 3, 300)
exp = np.exp(t)

fig, ax = plt.subplots(figsize=(7, 7))
ax.plot(t, exp)
plt.show()


fig, ax = plt.subplots(figsize=(7, 7))

ax.set_yscale('log')
ax.plot(t, exp)
plt.show()

#################################################################
p = np.linspace(0.001, 0.999, 300)
information = -np.log2(p)

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_yscale('log', basey=2) # basey = 2로 하면 밑이 2가 된다!
ax.plot(p, information )
plt.show()

#################################################################

logit = np.linspace(-10, 10, 300)
sigmoid = 1 / (1 + np.exp(-logit))

fig, ax = plt.subplots(figsize = (7, 7))
ax.plot(logit, sigmoid) # ax.plot(x, y)
plt.show()

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_yscale('logit')
ax.plot(logit, sigmoid)
plt.show()