import pygame
import numpy as np
colour_dead = (32, 43, 100)  #Цвет мертвой клетки
colour_grid = (40, 40, 40)   #Цвет сетки
colour_alive = (44, 212, 55) #Цвет живой клетки


def update(screen, cells, size, InProgress = False, generation:int=0, CountGens = False):
        font = pygame.font.SysFont('Trebuchet MS', 30)
        cells_updated = np.zeros((cells.shape[0], cells.shape[1]))        
        for row, column in np.ndindex(cells.shape):
            alive = np.sum(cells[row-1:row+2, column-1:column+2]) - cells[row, column]
            colour = (colour_dead) if cells [row, column] == 0 else (colour_alive)
            if cells[row, column] == 1:
                if 2 <= alive <= 3:
                    cells_updated[row, column] = 1
                    if InProgress:
                        colour = (colour_alive)            
            else:
                if alive == 3:
                    cells_updated[row, column] = 1
                    if InProgress:
                        colour = (colour_alive)

            pygame.draw.rect(screen, colour, (column*size, row * size, size - 1, size - 1))
        if CountGens:
            generation += 1
            text_surface = font.render(f"current generation: {generation}", False, (255, 255, 255))
            screen.blit(text_surface, (0,0))
        else:
            text_surface = font.render('Paused', False, (255, 255, 255))
            screen.blit(text_surface, (0,0))
        
        return cells_updated,generation

def main():
    igeneration=0 
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1600, 900))
    cells = np.zeros((90, 160))
    screen.fill(colour_grid)
    update(screen, cells, 10, generation=igeneration, CountGens = True)
    # pygame.display.flip()
    pygame.display.update()
    running = False
    pygame.display.set_caption("Game of life")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:   # По нажатии пробела ставим запускаем\останавливаем эволюцию
                    running = not running
                    _ , igeneration = update(screen, cells, 10, generation=igeneration, CountGens=True)
                    pygame.display.update()
                elif event.key == pygame.K_1:
                    position = pygame.mouse.get_pos()
                    try:
                        cells[position[1] // 10,      position[0]// 10    ] = 1  # Создаем на единицу глайдер
                        cells[position[1] // 10,      position[0]// 10 + 1] = 1
                        cells[position[1] // 10,      position[0]// 10 + 2] = 1
                        cells[position[1] // 10 - 2,  position[0]// 10 + 1] = 1
                        cells[position[1] // 10 - 1,  position[0]// 10 + 2] = 1
                        update(screen, cells, 10)
                        pygame.display.update()
                    except:
                        update(screen, cells, 10)
                        pygame.display.update()
                elif event.key == pygame.K_2:
                    position = pygame.mouse.get_pos()
                    try:
                        cells[position[1] // 10,     position[0] // 10    ] = 1
                        cells[position[1] // 10,     position[0] // 10 + 1] = 1
                        cells[position[1] // 10 - 2, position[0] // 10 + 1] = 1
                        cells[position[1] // 10 - 1, position[0] // 10 + 3] = 1 # Создаем "Желудь"
                        cells[position[1] // 10,     position[0] // 10 + 4] = 1
                        cells[position[1] // 10,     position[0] // 10 + 5] = 1
                        cells[position[1] // 10,     position[0] // 10 + 6] = 1
                        update(screen, cells, 10)
                        pygame.display.update()
                    except: 
                        update(screen, cells, 10)
                        pygame.display.update()
                elif event.key == pygame.K_3:
                    position = pygame.mouse.get_pos()
                    try:                    
                        cells[position[1] // 10, position[0] // 10    ] = 1
                        cells[position[1] // 10, position[0] // 10 + 1] = 1
                        cells[position[1] // 10, position[0] // 10 - 1] = 1 # Полоска 1х5
                        cells[position[1] // 10, position[0] // 10 + 2] = 1
                        cells[position[1] // 10, position[0] // 10 - 2] = 1
                        update(screen, cells, 10)
                        pygame.display.update()
                    except:
                        update(screen, cells, 10)
                        pygame.display.update()
                elif event.key == pygame.K_ESCAPE:
                    cells = np.zeros((90, 160))
                    igeneration = 0
                    _ , igeneration = update(screen, cells, 10, generation=igeneration)
                    pygame.display.update()

            elif pygame.mouse.get_pressed()[0]:            
                    position = pygame.mouse.get_pos()
                    cells[position[1] // 10, position[0] // 10] = 1  # Создаем живые клетки мышкой
                    update(screen, cells, 10)
                    pygame.display.update()
            elif pygame.mouse.get_pressed()[2]:
                    position = pygame.mouse.get_pos()        
                    cells[position[1] // 10, position[0] // 10] = 0  # Убираем живые клетки мышкой
                    update(screen, cells, 10)
                    pygame.display.update()       
            screen.fill(colour_grid)

        if running:                  
            cells, igeneration = update( screen, cells, 10, InProgress = True, generation=igeneration, CountGens = True)
            pygame.display.update()

if __name__ == '__main__':
    main()