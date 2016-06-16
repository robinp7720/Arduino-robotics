import sys
import pygame
import serial

bluetoothSerial = serial.Serial('/dev/ttyUSB1', baudrate=9600)

pygame.init()

size = width, height = 320, 240
white = 255, 255, 255

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            print(event)
            if (event.unicode == "w"):
                bluetoothSerial.write("255\n")
            if (event.unicode == "a"):
                bluetoothSerial.write("1950\n")
            if (event.unicode == "d"):
                bluetoothSerial.write("2050\n")

    screen.fill(white)
    pygame.display.flip()
