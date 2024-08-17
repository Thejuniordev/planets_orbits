import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import get_body, solar_system_ephemeris
from astropy.time import Time


# Função para obter a posição dos planetas em graus e suas distâncias
def get_planet_positions():
    # Tempo atual
    t = Time.now()

    # Dados dos planetas
    planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
    positions = []

    with solar_system_ephemeris.set('builtin'):
        for planet in planets:
            body = get_body(planet, t)
            # Converte a posição para graus e obtém a distância
            ra = body.ra.deg
            distance = body.distance.au
            positions.append((planet, ra, distance))

    return positions


# Função para desenhar o gráfico
def plot_planet_positions():
    # Obter posições dos planetas
    positions = get_planet_positions()

    # Configuração do gráfico
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, polar=True)

    # Adicionar a posição do Sol
    ax.scatter([0], [0], color='yellow', s=200, label='Sol')

    # Adicionar planetas
    for planet, ra, distance in positions:
        angle = np.deg2rad(ra % 360)  # Convertendo graus para radianos
        ax.scatter([angle], [distance], label=planet, s=100)

    # Configurações adicionais do gráfico
    ax.set_yticks(np.linspace(0, max(p[2] for p in positions), 6))  # Marcas radiais
    ax.set_yticklabels([f"{int(d)} AU" for d in np.linspace(0, max(p[2] for p in positions), 6)])

    # Adicionar legenda
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2))

    plt.title('Posições dos Planetas ao Redor do Sol com Distâncias')
    plt.show()


# Executar a função para desenhar o gráfico
plot_planet_positions()
