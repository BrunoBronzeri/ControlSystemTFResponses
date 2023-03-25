import numpy as np
import matplotlib.pyplot as plt
import control

# Define a função de transferência
G = control.tf([1.3, 0.5005], [1, 1.5, 0.5005])
F = control.tf([0.385], [1, 0.385])
Y = control.tf([0.5005], [1, 1.5, 0.5005])

# Calcula a resposta ao degrau unitário
t, y = control.step_response(Y)

# Calcula o tempo de assentamento de 2%
info = control.step_info(Y) #rtol=0.05
ts = info['SettlingTime']
tmax = info['Overshoot']
print(ts)

# Plota a resposta ao degrau
plt.figure()
plt.plot(t, y)
plt.grid()
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Step Response')

# Adiciona uma linha horizontal indicando o nível de 2% do regime permanente
#plt.axhline(y=tmax, color='gray', linestyle='--')

# Adiciona uma linha vertical indicando o tempo de assentamento de 5%
plt.axvline(x=ts, color='green', linestyle='--')
plt.axvline(x=7.5, color='red', linestyle='--')
plt.axhline(y=0.95, color='red', linestyle='--')
plt.axhline(y=0.98, color='green', linestyle='--')

# Adiciona um texto com o valor do tempo de assentamento de 5%
#plt.text(ts+0.1, 0.9, 'ts = %.2f s' % ts)

# Plota o diagrama de polos e zeros
plt.figure()
control.pzmap(Y)
plt.grid()
plt.title('Diagrama de polos e zeros G(s)')

# Mostra os gráficos
plt.show()
