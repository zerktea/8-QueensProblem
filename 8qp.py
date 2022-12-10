import random
import pygame
black = (0, 0, 0)
white = (255, 255, 255)

red = (255, 0, 0)
WIDTH = 50
HEIGHT = 50
MARGIN = 5
grid = []
SetOfIn = []
n = int(input('Enter the Number of individual : '))
for i in range(0, n):
    SetOfIn.append([])
    for j in range(0, 8):
        SetOfIn[i].append(random.randint(1, 8))


def Fitness(I):  # depends on selectioon
    count = 0
    for i in range(0, 8):
        for j in range(i+1, 8):
            if((SetOfIn[I][i] == SetOfIn[I][j]) or (SetOfIn[I][j] == SetOfIn[I][i]-(j-i)) or (SetOfIn[I][j] == SetOfIn[I][i]+(j-i))):
                count += 1
    return 28-count


def sumFitness():  # deppends on selection
    sumfitness = 0
    rouletteselec = []
    for i in range(n):
        sumfitness = sumfitness+Fitness(i)
        rouletteselec.append(sumfitness)

    return rouletteselec


def Solved():  # for the result and returns the index of the perfect individual
    for i in range(0, n):
        if(Fitness(i)==28):
            return i
    return -1


def selection():
    global SetOfIn
    SetOfrandomInd = []  # A sett ofof our selection
    selectset = sumFitness()

    for i in range(0, n):
        # a random number from 0 to the sum of Fitness function for the sett of Individuals
        rand = random.randint(0, selectset[n-1])

        if (rand == selectset[0] or (rand < selectset[0])):
            SetOfrandomInd.append(SetOfIn[0])
        else:
            for j in range(n-2, -1, -1):
                if(rand == selectset[j] or (rand > selectset[j])):
                    SetOfrandomInd.append(SetOfIn[j+1])
                    break

    SetOfIn = []
    SetOfIn = SetOfrandomInd


def Crossover():
    for i in range(0, n, 2):
        Crosspoint1 = random.randint(1, 7)
        Crosspoint2 = random.randint(1, 7)
        if(Crosspoint1 > Crosspoint2):
            Crosspoint1, Crosspoint2 = Crosspoint2, Crosspoint1
        for j in range(Crosspoint1, Crosspoint2+1):
            SetOfIn[i][j], SetOfIn[i+1][j] = SetOfIn[i+1][j], SetOfIn[i][j]


def mutation():
    
    MP = 1/100

    for i in range(n):
        for j in range(8):
            rand = random.random()
            if (rand <= MP):
                SetOfIn[i][j] = random.randint(1, 8)

calc=0
while(Solved() == -1):
    selection()
    Crossover()
    mutation()
    calc+=1
L = SetOfIn[Solved()]

print(L)
print('number of Iteration is: ',calc)
for row in range(8):
    grid.append([])
    for column in range(8):
        grid[row].append(0)

pygame.init()
window_size = [445, 445]
scr = pygame.display.set_mode(window_size)
pygame.display.set_caption("Grid")
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    scr.fill(black)
    for row in range(7, -1, -1):
        for column in range(8):
            color = white
            if(column+1 == L[row]):
                color = red
            pygame.draw.rect(scr,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    clock.tick(50)
    pygame.display.flip()
pygame.quit()
