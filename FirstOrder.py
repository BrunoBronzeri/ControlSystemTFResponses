import numpy as np
import matplotlib.pyplot as plt
import control

# Define a função de transferência
G = control.tf([1], [5, 1])

# Calcula a resposta ao degrau unitário
t, y = control.step_response(G)

# Calcula o tempo de assentamento de 5%
info = control.step_info(G) #rtol=0.05
ts = info['SettlingTime']
tmax = info['SettlingMax']

# Plota a resposta ao degrau
plt.figure()
plt.plot(t, y)
plt.grid()
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Resposta ao degrau')
plt.axvline(ts, color='r', linestyle='--', label='Tempo de assentamento de 2%')
plt.legend()

# Adiciona uma linha horizontal indicando o nível de 2% do regime permanente
plt.axhline(y=tmax*0.98, color='gray', linestyle='--')

# Adiciona uma linha vertical indicando o tempo de assentamento de 5%
plt.axvline(x=ts, color='red', linestyle='--')

# Adiciona um texto com o valor do tempo de assentamento de 5%
plt.text(ts+0.1, 0.9, 'ts = %.2f s' % ts)

# Plota o diagrama de polos e zeros
plt.figure()
control.pzmap(G)
plt.grid()
plt.title('Diagrama de polos e zeros')

# Mostra os gráficos
plt.show()