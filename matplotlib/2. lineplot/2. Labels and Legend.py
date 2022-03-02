import matplotlib.pyplot as plt 
import numpy as np 

# Basic
n_data = 100 
random_noise1 = np.random.normal(0, 1, (n_data, ))
random_noise2 = np.random.normal(1, 1, (n_data, ))
random_noise3 = np.random.normal(2, 1, (n_data, ))

fig,ax = plt.subplots(figsize=(10, 7))
ax.tick_parmas(labelsize=20)

ax.plot(random_noise1, label='random noise1')
ax.plot(random_noise2, label='random noise2')
ax.plot(random_noise3, label='random noise3')
ax.legend()
plt.show()

##########################################################
# legend location : best, upper right, upper left, lower left,\
# right, center left, center rifht, lower center, upper center, center


n_data = 100 
random_noise1 = np.random.normal(0, 1, (n_data, ))
random_noise2 = np.random.normal(1, 1, (n_data, ))
random_noise3 = np.random.normal(2, 1, (n_data, ))

fig, ax = plt.subplots(figsize=(10, 10))

ax.plot(random_noise1, label = 'random noise1')
ax.plot(random_noise2, label = 'random noise2')
ax.plot(random_noise3, label = 'random noise3')

ax.tick_params(labelsize=20)

ax.legend(fontsize=20, loc='upper right')
plt.show()


##########################################################
fig, ax = plt.subplots(figsize=(10, 10))

ax.plot(random_noise1, label = 'random noise1')
ax.plot(random_noise2, label = 'random noise2')
ax.plot(random_noise3, label = 'random noise3')

ax.tick_params(labelsize=20)
ax.legend(fontsize=20, loc='upper left')
plt.show()

##########################################################
fig, ax = plt.subplots(figsize=(10, 10))

ax.plot(random_noise1, label = 'random noise1')
ax.plot(random_noise2, label = 'random noise2')
ax.plot(random_noise3, label = 'random noise3')

ax.tick_params(labelsize=20)
ax.legend(fontsize=20, loc='upper right')
plt.show()

##########################################################
fig, ax = plt.subplots(figsize=(10, 10))

ax.plot(random_noise1, label = 'random noise1')
ax.plot(random_noise2, label = 'random noise2')
ax.plot(random_noise3, label = 'random noise3')

ax.tick_params(labelsize=20)
ax.legend(fontsize=20, loc='lower left')
plt.show()



##########################################################
# ncol argument

PI = np.pi
t = np.linspace(-4*PI, 4*PI, 300)
sin = np.sin(t)

fig, ax = plt.subplots(figsize=(10, 10))

for ax_idx in range(12):
    label_template = 'added by {}'
    ax.plot(t, sin+ax_idx, label = label_template.format(ax_idx))
    
ax.legend(fontsize=20)
plt.show()

##########################################################
PI = np.pi
t = np.linspace(-4*PI, 4*PI, 300)
sin = np.sin(t)

fig, ax = plt.subplots(figsize=(10, 10))

for ax_idx in range(12):
    label_template = 'added by {}'
    ax.plot(t, sin+ax_idx, label=label_template.format(ax_idx))
    
ax.legend(fontsize=15, ncol=2) # or ncol=3
plt.show()

# bbox_to_anchor = (0,1) or (1,0)...
# bbox_to_anchor는 (x,y) legend box의 위치를 정해준다. 1,1 일경우 좌상단, 0,0일 경우 우하단
fig, ax =plt.subplots(figsize=(10, 10))

for ax_idx in range(10):
    label_template = 'added by {}'
    ax.plot(t, sin+ax_idx,label=label_template.format(ax_idx))
    
ax.legend(fontsize=15, ncol=2, bbox_to_anchor = (0.5, 0))
plt.show()


n_data =100
random_noise1 = np.random.normal(0, 1, (n_data, ))
random_noise2 = np.random.normal(1, 1, (n_data, ))
random_noise3 = np.random.normal(2, 1, (n_data, ))

fig, ax = plt.subplots(figsize=(10, 7))
ax.tick_params(labelsize=20)

ax.plot(random_noise1, label='random noise1')
ax.plot(random_noise2, label='random noise2')
ax.plot(random_noise3, label='random noise3')

ax.legend(fontsize=20, bbox_to_anchor=(1, 0.5), loc='center left')
fig.tight_layout() # 지정해주지 않으면 legend가  짤려서 나온다. 
plt.show()


# bbox_to_anchor=(-0.1, 0.5), loc='center right'
fig, ax = plt.subplots(figsize=(10, 7))
ax.tick_params(labelsize=20)

ax.plot(random_noise1, label='random noise1')
ax.plot(random_noise2, label='random noise2')
ax.plot(random_noise3, label='random noise3')

ax.legend(fontsize=20, bbox_to_anchor=(-0.1, 0.5), loc='center right')
fig.tight_layout()
plt.show()


# ax.legend(fontsize=20, bbox_to_anchor=(1, 0.5), loc='center left')
fig, ax = plt.subplots(figsize=(10, 7))
ax.tick_params(labelsize=20)

ax.plot(random_noise1, label='random noise1')
ax.plot(random_noise2, label='random noise2')
ax.plot(random_noise3, label='random noise3')

ax.legend(fontsize=20, bbox_to_anchor=(1, 0.5), loc='center left')
fig.tight_layout()
plt.show()


# ax.legend(fontsize=20, bbox_to_anchor=(0.5, 1), loc='lower center')
fig, ax = plt.subplots(figsize=(10, 7))
ax.tick_params(labelsize=20)

ax.plot(random_noise1, label='random noise1')
ax.plot(random_noise2, label='random noise2')
ax.plot(random_noise3, label='random noise3')

ax.legend(fontsize=20, bbox_to_anchor=(0.5, 1), loc='lower center')
fig.tight_layout()
plt.show()


# ax.legend(fontsize=20, bbox_to_anchor=(0.5, -0.1), loc='upper center')
fig, ax = plt.subplots(figsize=(10, 7))
ax.tick_params(labelsize=20)

ax.plot(random_noise1, label='random noise1')
ax.plot(random_noise2, label='random noise2')
ax.plot(random_noise3, label='random noise3')

ax.legend(fontsize=20, bbox_to_anchor=(0.5, -0.1), loc='upper center')
fig.tight_layout()
plt.show()


PI = np.pi
t = np.linspace(-4*PI, 4*PI, 300)
sin = np.sin(t)

fig, ax = plt.subplots(figsize=(10, 10))

for ax_idx in range(12):
    label_template = 'added by {}'
    ax.plot(t, sin+ax_idx, label=label_template.format(ax_idx))
    
ax.legend(fontsize=15, ncol=4, bbox_to_anchor=(0.5, -0.05), loc='upper center')
fig.tight_layout()
plt.show()