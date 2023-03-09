import pygame
import random
import time

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the font
font = pygame.font.Font(None, 36)

# Define the difficulty levels
EASY = 1
MEDIUM = 2
HARD = 3

# Define the word lists for each level
easy_words = ["apple", "banana", "cherry", "orange", "pear"]
medium_words = ["computer", "keyboard", "monitor", "mouse", "printer"]
hard_words = ["abacus", "algorithm", "binary", "compiler", "debugging"]

# Define the game variables
score = 0
time_remaining = 30
level = EASY

# Define the word list for the current level
if level == EASY:
    word_list = easy_words
elif level == MEDIUM:
    word_list = medium_words
else:
    word_list = hard_words
random_word = random.choice(word_list)

# Define label
label = font.render("Word", True, BLACK)
word_rect = label.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Define the timer event
TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 1000)

# Define user_input
user_input = ""

# Define the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                if len(user_input) < len(random_word):
                    user_input += event.unicode
                if user_input == random_word:
                    score += 1
                    user_input = ""
                    if time_remaining > 0:
                        random_word = random.choice(word_list)
                        label = font.render(random_word, True, BLACK)
                        word_rect = label.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                        time_remaining += 1
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
        elif event.type == TIMER_EVENT:
            time_remaining -= 1
            if time_remaining == 0:
                running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the score and timer labels
    score_label = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_label, (10, 10))
    time_label = font.render("Time: " + str(time_remaining), True, BLACK)
    screen.blit(time_label, (SCREEN_WIDTH - time_label.get_width() - 10, 10))

    # Draw the random word label
    screen.blit(label, word_rect)

    # Draw the user input label
    user_input_label = font.render(user_input, True, BLUE)
    screen.blit(user_input_label, (10, SCREEN_HEIGHT - user_input_label.get_height() - 10))

    # Update the display
    pygame.display.flip()

pygame.quit()