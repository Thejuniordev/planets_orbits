import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import get_body, solar_system_ephemeris
from astropy.time import Time


# Função para obter a posição dos planetas em graus
def get_planet_positions():
    # Tempo atual
    t = Time.now()

    # Dados dos planetas
    planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
    positions = []

    with solar_system_ephemeris.set('builtin'):
        for planet in planets:
            body = get_body(planet, t)
            # Converte a posição para graus
            ra = body.ra.deg
            positions.append((planet, ra))

    return positions


# Função para desenhar o gráfico
def plot_planet_positions():
    # Obter posições dos planetas
    positions = get_planet_positions()

    # Configuração do gráfico
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)

    # Definir o Sol no centro (0 graus)
    ax.set_yticklabels([])
    ax.set_xticks(np.linspace(0, 2 * np.pi, len(positions), endpoint=False))

    # Adicionar a posição do Sol
    ax.scatter([0], [0], color='yellow', s=200, label='Sol')

    # Adicionar planetas
    for planet, pos in positions:
        angle = np.deg2rad(pos % 360)  # Convertendo graus para radianos
        ax.scatter([angle], [1], label=planet)

    # Configurações adicionais do gráfico
    ax.set_ylim(0, 1.5)
    ax.set_yticklabels([])
    ax.set_xticks(np.linspace(0, 2 * np.pi, len(positions), endpoint=False))
    ax.set_xticklabels([f'{planet[0]}°' for planet, _ in positions])

    # Adicionar legenda
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2))

    plt.title('Posições dos Planetas ao Redor do Sol')
    plt.show()


# Executar a função para desenhar o gráfico
plot_planet_positions()
