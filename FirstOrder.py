import numpy as np
import matplotlib.pyplot as plt
import control

# Define a função de transferência malha aberta
G = control.tf([1], [5, 1])

# Define a funçao de transferência do controlador
C = control.tf([1.3, 0.5005], [1, 0])

# Define a função de transferência da malha fechada sem filtro
MF = control.tf([1.3, 0.5005], [1, 1.5, 0.5005])

# Define função de transferência filtro
F = control.tf([0.385], [1, 0.385])

# Define a função de transferência da malha fechada com filtro
MFF = control.tf([0.5005], [1, 1.5, 0.5005])

# Calcula a resposta ao degrau unitário
t1, y1 = control.step_response(G)
t2, y2 = control.step_response(MF)
t3, y3 = control.step_response(MFF)

# Calcula o tempo de assentamento de 2%
info = control.step_info(G) #rtol=0.05
ts1 = info['SettlingTime']
tmax = info['SettlingMax']

info1 = control.step_info(MF) #rtol=0.05
ts2 = info['SettlingTime']

info2 = control.step_info(MFF) #rtol=0.05
ts3 = info['SettlingTime']

# Plota a resposta ao degrau
plt.figure()
plt.plot(t1, y1, label='G')
plt.grid()
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Resposta ao degrau (G)')
plt.axvline(ts1, color='r', linestyle='--', label='Tempo de assent. de 2%')
plt.legend()

# Adiciona uma linha horizontal indicando o nível de 2% do regime permanente
plt.axhline(y=tmax*0.98, color='gray', linestyle='--')

# Adiciona uma linha vertical indicando o tempo de assentamento de 5%
plt.axvline(x=ts1, color='red', linestyle='--')

# Adiciona um texto com o valor do tempo de assentamento de 5%
plt.text(ts1+0.1, 0.9, 'ts = %.2f s' % ts1)

# Plota a resposta ao degrau MF
plt.figure()
plt.plot(t2, y2, label='MF')
plt.grid()
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Resposta ao degrau (MF)')
plt.axvline(ts2, color='r', linestyle='--', label='Tempo de assent. de 2%')
plt.legend()

# Adiciona uma linha vertical indicando o tempo de assentamento de 5%
plt.axvline(x=ts2, color='red', linestyle='--')

# Adiciona um texto com o valor do tempo de assentamento de 5%
plt.text(ts2+0.1, 0.9, 'ts = %.2f s' % ts2)

# Plota a resposta ao degrau MF
plt.figure()
plt.plot(t3, y3, label='MFF')
plt.grid()
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Resposta ao degrau (MF com filtro)')
plt.axvline(ts3, color='r', linestyle='--', label='Tempo de assent. de 2%')
plt.legend()

# Adiciona uma linha vertical indicando o tempo de assentamento de 5%
plt.axvline(x=ts3, color='red', linestyle='--')

# Adiciona um texto com o valor do tempo de assentamento de 5%
plt.text(ts3+0.1, 0.9, 'ts = %.2f s' % ts3)

# Plota o diagrama de polos e zeros
plt.figure()
control.pzmap(G)
plt.grid()
plt.title('Diagrama de polos e zeros')

# Mostra os gráficos
plt.show()
