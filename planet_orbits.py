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


# Função para desenhar o gráfico e a tabela
def plot_planet_positions():
    # Obter posições dos planetas
    positions = get_planet_positions()

    # Configuração da figura e dos eixos
    fig, (ax_polar, ax_table) = plt.subplots(1, 2, figsize=(15, 8), gridspec_kw={'width_ratios': [2, 1]})

    # Configuração do gráfico polar
    ax_polar = plt.subplot(121, polar=True)
    ax_polar.set_title('Posições dos Planetas ao Redor do Sol com Distâncias')

    # Adicionar a posição do Sol
    ax_polar.scatter([0], [0], color='yellow', s=200, label='Sol')

    # Adicionar planetas
    for planet, ra, distance in positions:
        angle = np.deg2rad(ra % 360)  # Convertendo graus para radianos
        ax_polar.scatter([angle], [distance], label=planet, s=100)

    # Configurações adicionais do gráfico
    ax_polar.set_yticks(np.linspace(0, max(p[2] for p in positions), 6))  # Marcas radiais
    ax_polar.set_yticklabels([f"{int(d)} AU" for d in np.linspace(0, max(p[2] for p in positions), 6)])

    # Configuração da Tabela
    table_data = [(planet, f"{ra:.2f}°", f"{distance:.2f} AU") for planet, ra, distance in positions]
    column_labels = ["Planeta", "RA (Degrees)", "Distância (AU)"]

    # Criação da tabela
    ax_table.axis('tight')
    ax_table.axis('off')
    table = ax_table.table(cellText=table_data, colLabels=column_labels, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    plt.show()


# Executar a função para desenhar o gráfico e a tabela
plot_planet_positions()
