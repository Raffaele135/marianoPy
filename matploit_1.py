import matplotlib.pyplot as plt

data = {'Estate': 30, 'Primavera': 15, 'Inverno': 7, 'Autunno': 5}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Quale è la stagione preferita dai ragazzi?')


plt.show()
