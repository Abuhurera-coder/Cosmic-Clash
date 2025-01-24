import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cosmic Clash")


clock = pygame.time.Clock()


background_img = pygame.image.load( r"D:\space backgroung.jpg")  # Replace with your background image
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

spaceship_img = pygame.image.load(r"D:\Battleship.webp")  # Replace with your spaceship image
spaceship_img = pygame.transform.scale(spaceship_img, (100, 100))  # Adjust size if needed

asteroid_img = pygame.image.load(r"D:\UFO.png")  # Replace with your asteroid image
asteroid_img = pygame.transform.scale(asteroid_img, (70, 70))  # Adjust size if needed
 
bullet_img = pygame.image.load(r"D:\missile.jpg")  # Optional: Replace with your bullet image
bullet_img = pygame.transform.scale(bullet_img, (10, 20))  # Adjust size if needed


spaceship_x = WIDTH // 100
spaceship_y = HEIGHT - 100
spaceship_speed = 5


bullets = []
bullet_speed = 7


asteroids = []
asteroid_speed = 5


score = 0
font = pygame.font.SysFont("Arial", 24)


def draw_score():
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


running = True
while running:
    screen.blit(background_img, (0, 0))  

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                bullet_x = spaceship_x + 20  
                bullet_y = spaceship_y
                bullets.append([bullet_x, bullet_y])

   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_x > 0:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT] and spaceship_x < WIDTH - 50:
        spaceship_x += spaceship_speed

    
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:  
            bullets.remove(bullet)

   
    if random.randint(1, 50) == 1:  
        asteroid_x = random.randint(0, WIDTH - 50)
        asteroid_y = -50
        asteroids.append([asteroid_x, asteroid_y])

  
    for asteroid in asteroids[:]:
        asteroid[1] += asteroid_speed
        if asteroid[1] > HEIGHT:  
            asteroids.remove(asteroid)
       
        elif (
            asteroid[0] < spaceship_x + 50
            and asteroid[0] + 50 > spaceship_x
            and asteroid[1] < spaceship_y + 40
            and asteroid[1] + 50 > spaceship_y
        ):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    
    for bullet in bullets[:]:
        for asteroid in asteroids[:]:
            if (
                bullet[0] < asteroid[0] + 50
                and bullet[0] + 10 > asteroid[0]
                and bullet[1] < asteroid[1] + 50
                and bullet[1] + 20 > asteroid[1]
            ):
                bullets.remove(bullet)
                asteroids.remove(asteroid)
                score += 10

    
    screen.blit(spaceship_img, (spaceship_x, spaceship_y))

   
    for bullet in bullets:
        screen.blit(bullet_img, (bullet[0], bullet[1]))

   
    for asteroid in asteroids:
        screen.blit(asteroid_img, (asteroid[0], asteroid[1]))

  
    draw_score()

   
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
