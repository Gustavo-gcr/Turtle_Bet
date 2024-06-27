import turtle
import time
import random


WIDTH, HEIGHT = 700, 600
CORES = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def numero_tartaruga():
	racers = 0
	while True:
		racers = input('Escolha o numero de competidoras (2 - 10): ')
		if racers.isdigit():
			racers = int(racers)
		else:
			print('Digite um número, tente novamente')
			continue

		if 2 <= racers <= 10:
			return racers
		else:
			print('Número não esta entre 2 e 10')

def corrida(cores):
	turtles = criar_tartarugas(cores)

	while True:
		for racer in turtles:
			distance = random.randrange(1, 20)
			racer.forward(distance)

			x, y = racer.pos()
			if y >= HEIGHT // 2 - 10:
				return cores[turtles.index(racer)]

def criar_tartarugas(cores):
	turtles = []
	spacingx = WIDTH // (len(cores) + 1)
	for i, color in enumerate(cores):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles

def init_turtle():
	screen = turtle.Screen()
	screen.setup(WIDTH, HEIGHT)
	screen.title('Turtle Racing!')

racers = numero_tartaruga()
init_turtle()

random.shuffle(CORES)
cores = CORES[:racers]

winner = corrida(cores)
print("A vencedora é a tartaruga da cor ", winner)
time.sleep(5)