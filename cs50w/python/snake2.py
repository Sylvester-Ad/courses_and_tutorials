
import pygame
import random

# Initialize the game
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up the snake
snake_block_size = 20
snake_speed = 10

# Define the snake's movement directions
direction = "right"

# Define the font for displaying the score
font_style = pygame.font.SysFont(None, 50)

def display_score(score):
    """
    Function to display the current score on the game window.

    Parameters:
    - score: int
        The current score to be displayed.
    """

    score_text = font_style.render("Score: " + str(score), True, black)
    window.blit(score_text, [10, 10])

def draw_snake(snake_block_size, snake_list):
    """
    Function to draw the snake on the game window.

    Parameters:
    - snake_block_size: int
        The size of each block of the snake.
    - snake_list: list
        The list containing the coordinates of each block of the snake.
    """

    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block_size, snake_block_size])

def game_loop():
    """
    Function to start and run the game loop.
    """

    # Initialize the game over flag
    game_over = False

    # Initialize the game clock
    clock = pygame.time.Clock()

    # Initialize the snake's starting position and length
    snake_list = []
    snake_length = 1

    # Generate the initial position of the snake
    x1 = window_width / 2
    y1 = window_height / 2

    # Define the change in position for each movement
    x1_change = 0
    y1_change = 0

    # Generate the initial position of the food
    food_x = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0

    # Start the game loop
    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    y1_change = snake_block_size
                    x1_change = 0

        # Update the snake's position
        x1 += x1_change
        y1 += y1_change

        # Check for collision with the boundaries of the window
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_over = True

        # Update the game window
        window.fill(white)
        pygame.draw.rect(window, red, [food_x, food_y, snake_block_size, snake_block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with the snake's body
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        # Draw the snake and the score
        draw_snake(snake_block_size, snake_list)
        display_score(snake_length - 1)

        # Update the food position and increase the snake's length
        pygame.display.update()
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0
            snake_length += 1

        # Set the game speed
        clock.tick(snake_speed)

    # Quit the game
    pygame.quit()

# Start the game
game_loop()
                    