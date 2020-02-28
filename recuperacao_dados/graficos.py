import matplotlib.pyplot as plt
import numpy as np

(fig, ax) = plt.subplots(1, 1, figsize=(15,10))

#ax.set_title('Um histograma')
#ax.set_xlabel('Idade')
#ax.set_ylabel('Quantidade')

#idades = np.random.normal(30,4,size=200).astype(int) # mais repetições no meio e menos nas extremidades

#idades = np.random.exponential(1,size=200)
#idades *= 25
#ax.hist(idades, bins=20)

ax.set_title('Desemprego X inflacao')
ax.set_xlabel('Desempregro')
ax.set_ylabel('Inflacao')

paises = np.random.choice([0,1,2], size=1000)
desemprego = np.random.normal(10, 2, size = 1000)
inflacao = np.random.normal(3, 0.1, size = 1000)

#ax.scatter(desemprego, inflacao, color=cor, marker='o', alpha=0.5)

# inflacao_por_pais = dict()
# for (p, d, i) in zip(paises, desemprego, inflacao):
#     ip = inflacao_por_pais.get(p, [])
#     ip.append((d, i))
#     inflacao_por_pais[p] = ip

# cores = ['r', 'g', 'b']

# for (cor, valores) in zip(cores, inflacao_por_pais.values()):
#     ax.scatter([v[0] for v in valores], [v[1] for v in valores], color=cor, marker='o', alpha=0.5)



plt.show()