# ax.plot(y)

import matplotlib.pyplot as plt 
import numpy as np 

np.random.seed(0)

y_data = np.random.normal(loc=0, scale=1, size=(300,) ) # loc : center, scale : Std, size : N

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(y_data)

fig.tight_layout(pad=3)
ax.tick_params(labelsize=25)

ax.grid(True)

# ax.spines
# spines는 Dict 형태로 구성되어있다. Keys는 left, right, bottom, top 등의 위치를 나타낸다. 
# value에는 우리가 조작할 수 있는 객체들이 들어가 있다. 
# 축을 조작해서 우리가 원하는 위치로 옮길 수 있다. 
for spine_loc, spine in ax.spines.items():
    spine.set_linewidth(3)
    
    if spine_loc in ['right', 'top']:
        spine.set_visible(False) # 축을 제거
    
    if spine_loc in ['bottom', 'left']:
        spine.set_position(('data', 0)) # 'data'가 0인 지점에 position 시킨다.
plt.show()

############################################################################################
# ax.set_xticks
y_data = np.random.normal(loc=0, scale=1, size=(300,))

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(y_data)

fig.tight_layout(pad=3)
ax.tick_params(labelsize=25)

x_ticks=np.arange(301, step=50)
ax.set_xticks(x_ticks)
plt.show()


y_data = np.random.normal(loc=0, scale=1, size=(300,))

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(y_data)

fig.tight_layout(pad=3)
ax.tick_params(labelsize=25)

x_ticks = np.arange(301, step=100)
ax.set_xticks(x_ticks)
plt.show()

############################################################################################

n_data = 100
s_idx = 30
x_data = np.arange(s_idx, s_idx + n_data)
y_data = np.random.normal(0, 1, (n_data, ))

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x_data, y_data)

fig.tight_layout(pad=3)
x_ticks = np.arange(s_idx, s_idx + n_data + 1, 20)
ax.set_xticks(x_ticks)

ax.tick_params(labelsize=25)
ax.grid()

plt.show()

############################################################################################
# ax.plot(x, y)

x_data = np.array([10, 25, 31, 40, 55, 80, 100])
y_data = np.random.normal(0, 1, (7, ))

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x_data, y_data)

fig.subplots_adjust(left=0.2)
ax.tick_params(labelsize=25)

ax.set_xticks(x_data)
ylim = ax.get_ylim()
yticks = np.linspace(ylim[0], ylim[1], 8)
ax.set_yticks(yticks)

ax.grid()
plt.show()

############################################################################################
x_data = np.random.normal(0, 1, (10, ))
y_data = np.random.normal(0, 1, (10, ))

fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(x_data, y_data)
plt.show()

############################################################################################

random_noise1 = np.random.normal(0, 1, (100, ))
random_noise2 = np.random.normal(1, 1, (100, ))
random_noise3 = np.random.normal(2, 1, (100, ))

fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(random_noise1)
ax.plot(random_noise2)
ax.plot(random_noise3)

ax.tick_params(labelsize=20)
plt.show()

############################################################################################
n_data1, n_data2, n_data3 = 200, 50, 10

x_data1 = np.linspace(0, 200, n_data1)
x_data2 = np.linspace(0, 200, n_data2)
x_data3 = np.linspace(0, 200, n_data3)

random_noise1 = np.random.normal(0, 1, (n_data1, ))
random_noise2 = np.random.normal(2, 1, (n_data2, ))
random_noise3 = np.random.normal(3, 1, (n_data3, ))

fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(x_data1, random_noise1)
ax.plot(x_data2, random_noise2)
ax.plot(x_data3, random_noise3)
plt.show()

############################################################################################

PI = np.pi 
t = np.linspace(-4*PI, 4*PI, 300)
sin = np.sin(t)
linear = 0.1*t

fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(t, sin)
ax.plot(t, linear)

ax.set_ylim([-1.5, 1.5])

x_ticks = np.arange(-4*PI, 4*PI+0.1, PI) # letex 가능.
x_ticklabels = [str(i) + r'$\pi$' for i in range(-4, 5)] 
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_ticklabels)

ax.tick_params(labelsize=20)
ax.grid()

plt.show()

############################################################################################

PI = np.pi 
t = np.linspace(-4*PI, 4*PI, 1000)
sin = np.sin(t)
cos = np.cos(t)
tan = np.tan(t)

fig, axes = plt.subplots(3, 1, figsize=(7, 10))

axes[0].plot(t, sin)
axes[1].plot(t, cos)
axes[2].plot(t, tan)
fig.tight_layout()

axes[2].set_ylim([-5, 5]) # limit을 안해주면 값이 너무 커진다.
plt.show()


############################################################################################

PI = np.pi 
t = np.linspace(-4*PI, 4*PI, 1000).reshape(1, -1)
sin = np.sin(t)
cos = np.cos(t)
tan = np.tan(t)
data = np.vstack((sin, cos, tan))

title_list = [r'$sin(t)$', r'$cos(t)$', r'$tan(t)$']
x_ticks = np.arange(-4*PI, 4*PI+PI, PI)
x_ticklabels = [str(i) + r'$\pi$' for i in range(-4, 5)]

fig, axes = plt.subplots(3, 1, figsize=(7, 10), sharex = True)

for ax_idx, ax in enumerate(axes.flat):
    ax.plot(t.flatten(), data[ax_idx])
    ax.set_title(title_list[ax_idx], fontsize=30)
    ax.tick_params(labelsize=20)
    ax.grid()
    
    if ax_idx ==2:
        ax.set_ylim([-3, 3])
        
fig.subplots_adjust(left=0.1, right=0.95, bottom=0.05, top=0.95)

axes[-1].set_xticks(x_ticks)
axes[-1].set_xticklabels(x_ticklabels)
plt.show()

############################################################################################
# ax.axvline and ax.axhline 

fig, ax = plt.subplots(figsize=(7, 7))

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])

ax.axvline(x=1, color='black', linewidth=1)
plt.show()



fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])

ax.axvline(x=1, ymax=0.8, ymin=0.2, color='black', linewidth=1)
plt.show()

############################################################################################
# ax.axvline and ax.axhline 

fig, ax = plt.subplots(figsize=(7, 7))

ax.set_ylim([-5, 5])
ax.set_xlim([-5, 5])

ax.axhline(y=1, color='black', linewidth=1)
plt.show()


fig, ax = plt.subplots(figsize=(7, 7))

ax.set_ylim([-5, 5])
ax.set_xlim([-5, 5])

ax.axhline(y=1, color='black', linewidth=1, xmax=0.8, xmin=0.2)
plt.show()