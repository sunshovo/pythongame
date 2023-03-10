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
EXIT = 4

# Define the word lists for each level
easy_words = ["apple", "banana", "cherry", "orange", "pear"]
medium_words = ["computer", "keyboard", "monitor", "mouse", "printer"]
hard_words = ["abacus", "algorithm", "binary", "compiler", "debugging"]

# Define the game variables
score = 0
time_remaining = 30
level = EASY

# Define the difficulty selection loop
difficulty_selected = False
while not difficulty_selected:

    # Clear the screen
    screen.fill(WHITE)

    # Draw the difficulty selection labels
    title_label = font.render("<Select Difficulty>", True, BLACK)
    easy_label = font.render("1 - Easy", True, BLACK)
    medium_label = font.render("2 - Medium", True, BLACK)
    hard_label = font.render("3 - Hard", True, BLACK)
    exit_game = font.render("4 - exit", True, BLACK)

    # Position the title label
    title_x = SCREEN_WIDTH // 2 - title_label.get_width() // 2
    title_y = SCREEN_HEIGHT // 3 - title_label.get_height() // 2 - 50
    screen.blit(title_label, (title_x, title_y))

    # Calculate the vertical spacing between labels
    label_spacing = (SCREEN_HEIGHT // 2) // 6

    # Position the difficulty labels
    easy_x = SCREEN_WIDTH // 2 - easy_label.get_width() // 2
    easy_y = SCREEN_HEIGHT // 2 - easy_label.get_height() // 2
    screen.blit(easy_label, (easy_x, easy_y))

    medium_x = SCREEN_WIDTH // 2 - medium_label.get_width() // 2
    medium_y = easy_y + label_spacing
    screen.blit(medium_label, (medium_x, medium_y))

    hard_x = SCREEN_WIDTH // 2 - hard_label.get_width() // 2
    hard_y = medium_y + label_spacing
    screen.blit(hard_label, (hard_x, hard_y))

    exit_x = SCREEN_WIDTH // 2 - exit_game.get_width() // 2
    exit_y = hard_y + label_spacing
    screen.blit(exit_game, (exit_x, exit_y))
   
    # Update the display
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            difficulty_selected = True
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isnumeric():
                num = int(event.unicode)
                if num == EASY:
                    level = EASY
                    difficulty_selected = True
                elif num == MEDIUM:
                    level = MEDIUM
                    difficulty_selected = True
                elif num == HARD:
                    level = HARD
                    difficulty_selected = True
                elif num == EXIT:
                    level = EXIT
                    difficulty_selected = True
                    pygame.quit()
                    sys.exit()

# Define the word list for the current level
if level == EASY:
    word_list = easy_words
elif level == MEDIUM:
    word_list = medium_words
else:
    word_list = hard_words
random_word = random.choice(word_list)

# Define label
label = font.render(random_word, True, BLACK)
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