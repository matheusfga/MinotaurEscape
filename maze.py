# Usando o Algoritmo de Prim num grafo conectado não-direcionado de pesos aleatórios, forma-se uma MST diferente a cada vez que roda o algoritmo
# Depois, usando uma biblioteca de processamento de imagens para colorir o grafo, a MST gerada assemelha-se à um labirinto
# Autor: Matheus Oliveira

from PIL import Image, ImageColor
import numpy as np
import random

class Maze:
    def __init__(self, width = 31, height = 15):
        self._width = width
        self._height = height
        self.grid = np.zeros((width, height), dtype=bool)
        # Gera-se uma matriz com todos as células com valor False, o que indica
        # que todas as células são uma barreira do labirinto no início. Troca para True quando a célula se tornar passagem.

        start, end = self.generate()
        self.create_image(start, end)
        print("Novo labirinto criado em ./assets/maze.jpg")

    # Explicação do Algoritmo:
    # Primeiro passo: escolha um nó qualquer como ponto de partida e o marque como passagem (ou seja, mude seu valor na matriz para true)
    # Segundo passo: crie uma lista com todas as fronteiras do nó atual (lista de candidatos no Prim), isso é, todos os nós dentro do grid que estejam marcados 
        # como barriera (valor false na matriz), e que estejam a distância 2 do nó atual (a distancia serve para a formação correta do labirinto, visto que
        # cada célula pode ser ou uma passagem ou uma barreira)
    # Terceiro passo: enquanto a lista de fronteiras não estiver vazia:
        # escolhe um nó aleatório da lista de fronteiras e o marque como passagem (esse nó aleatório seria como o nó com a aresta de menor peso em Prim)
        # escolha um vizinho qualquer desse nó:
            # um vizinho é qualquer nó a distancia 2, que esteja marcado como passagem
        # conecte o nó atual com esse vizinho, por marcar a célula entre eles como passagem
        # coloque todas as fronteiras do nó atual na lista de fronteiras e retire o nó atual dessa lista

    def frontiers(self, x, y):
        frontier_list = []
        
        if x + 2 < self._width and not self.grid[x + 2, y]:
            frontier_list.append((x + 2, y))
        if x - 2 >= 0 and not self.grid[x - 2, y]:
            frontier_list.append((x - 2, y))
        if y + 2 < self._height and not self.grid[x, y + 2]:
            frontier_list.append((x, y + 2))
        if y - 2 >= 0 and not self.grid[x, y - 2]:
            frontier_list.append((x, y - 2))

        return frontier_list


    def neighbor(self, x, y):
        neighbor_list = []
        
        if x + 2 < self._width and self.grid[x + 2, y]:
            neighbor_list.append((x + 2, y))
        if x - 2 >= 0 and self.grid[x - 2, y]:
            neighbor_list.append((x - 2, y))
        if y + 2 < self._height and self.grid[x, y + 2]:
            neighbor_list.append((x, y + 2))
        if y - 2 >= 0 and self.grid[x, y - 2]:
            neighbor_list.append((x, y - 2))
        
        return neighbor_list[random.randint(0, len(neighbor_list) - 1)]


    def connect(self, x, y):
        # Recebe a fronteira(candidato) sendo computado como x, y
        to_be_connected = self.neighbor(x, y)
        bridge_x = int(((x - to_be_connected[0]) / 2) + to_be_connected[0])
        bridge_y = int(((y - to_be_connected[1]) / 2) + to_be_connected[1])
        bridge = (bridge_x, bridge_y)
        self.grid[to_be_connected] = True
        self.grid[bridge] = True
        return to_be_connected


    def generate(self):
        starting_node = (1, random.randint(1, self._height - 2))
        self.grid[starting_node] = True
        all_frontiers_set = set()
        all_frontiers_set = all_frontiers_set.union(self.frontiers(*starting_node))
        end = starting_node
        while all_frontiers_set:
            # i = random.randint(0, len(all_frontiers_set) - 1)
            chosen_node = all_frontiers_set.pop()
            self.grid[chosen_node] = True
            # print(chosen_node)
            chosen_neighbor = self.connect(*chosen_node)
            try:
                all_frontiers_set.remove(chosen_neighbor)
            except:
                pass
            all_frontiers_set = all_frontiers_set.union(self.frontiers(*chosen_node))
            end = chosen_node

        return starting_node, end
        
        
    def create_image(self, start, end):
        img = Image.new('RGB', (self._width, self._height))
        pixels = img.load()
        for i in range(self._width):
            for j in range(self._height):
                if self.grid[i, j]:
                    pixels[i, j] = (187, 217, 124)
                else:
                    pixels[i, j] = (16, 84, 34)

        pixels[start] = (18, 154, 222)
        pixels[end] = (222, 18, 18)
        newsize = (self._width * 40, self._height * 40)
        img = img.resize(newsize, resample=Image.BOX)
        img.save("assets/maze.jpg")

def main():
    maze = Maze()
    # starting_node = (0, random.randint(1, 14))
    # print(starting_node)
    # print(type(starting_node))
    # print(frontiers[0], frontiers[1])
    # print(frontiers[0][0] - frontiers[0][1])
    # pass_frontier = frontiers[random.randint(0, 3)]
    # print(pass_frontier)
    # print(pass_frontier[1])


if __name__ == "__main__":
    main()