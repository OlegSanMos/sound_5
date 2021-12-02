import numpy as np
import matplotlib.pyplot as plt

def speedOfSound(temperature, h2oX, co2Max):
    
    co2Max /= 100 #перевод в СИ
    temperature += 273.15
    
    xh2o = h2oX * (1 - co2Max) #обьемная доля водяного пара
    uh2o = 18.01 * xh2o #молярная масса воды
    cph2o = 1.863 * uh2o #коэффициент
    cvh2o = 1.403 * uh2o

    
    uco2 = 44.01 * co2Max #молярка углекислого г
    cpco2 = 0.838 * uco2 #коэффициент
    cvco2 = 0.249 * uco2 #коэффициент
  
    uv = 28.97 * (1 - xh2o) #молярка воздуха
    cpv =  1.0036 * uv #коэффициент
    cvv = 0.7166 * uv
    
    y = (cpv + cph2o + cpco2) / (cvv + cvh2o + cvco2) #показатель адиабаты
    
    soundSpeed = (y * 8.314 * temperature * 1000 / (uv + uh2o + uco2)) ** 0.5 #расчет по формуле
    
    return soundSpeed

temp = 23.3
h2oX = 0.005 #абс влажность
conc = np.linspace(0, 5, 10) #создаем массив х
speed = speedOfSound(temp, h2oX, conc) #массив скоростей
conc *= 100 #механика массива
k = np.polyfit(speed, conc, 1) #массив коэфф апроксимации(перевода скорости в конц)
speed1 = 344.7
speed2 = 342.6
conc1 = np.polyval(k, speed1) #перевод в концентрацию(подстановка)
conc2 = np.polyval(k, speed2)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
ax.plot(conc, speed,'k',label='Аналитическая зависимость', linewidth=1.5)

ax.plot(conc1, speed1, marker = 'D', label = 'Значение в воздухе: {:.1f} [м/с], {:.1f} [%]'.format(speed1, conc1), markersize=5, linewidth=0)
ax.plot(conc2, speed2, marker = 'D', label = 'Значение в выдохе: {:.1f} [м/с], {:.1f} [%]'.format(speed2, conc2), markersize=5, linewidth=0)

ax.legend(fontsize=12)

ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", linestyle='--', linewidth=0.25)
plt.minorticks_on()

ax.axis([0 - 0.2, 5 + 0.2, speed.min() - 0.2, speed.max() + 0.2]) #перделы

ax.set_title('Зависимость скорости звука\n от концентрации CO2', loc='center', fontsize=15)
ax.set_ylabel('Скорость звука [м/с]', loc='center', fontsize=10)
ax.set_xlabel('Концентрация CO2 [%]', loc='center', fontsize=10)

plt.show()

fig.savefig("sound_speed.png")

