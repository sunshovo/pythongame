import pygame
import random
import sys
from difficulty import DifficultySelector
from quitbutton import Button


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

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.total_time = 30000  # in milliseconds
        self.user_input = ""
        self.word_list = []
        self.random_word = ""
        self.label = None
        self.word_rect = None
        self.difficulty_selector = DifficultySelector(self.screen)

    def run(self):
        # Run the difficulty selection loop
        self.word_list = self.difficulty_selector.run()

        # Set random_word
        self.random_word = random.choice(self.word_list)
        self.label = self.font.render(self.random_word, True, BLACK)
        self.word_rect = self.label.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        # Get the start time
        start_time = pygame.time.get_ticks()

        # Create an exit button
        exit_button = Button(self.screen, "QUIT", self.font, RED, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 50, 80, 40)

        # Start the game loop with selected word list
        running = True
        while running:
            for event in pygame.event.get():
                exit_button.handle_event(event)
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    exit_button.handle_event(event)
                    if event.unicode.isalpha():
                        if len(self.user_input) < len(self.random_word):
                            self.user_input += event.unicode
                        if self.user_input == self.random_word:
                            # Increment the score and reset user input
                            self.score += 1
                            self.user_input = ""

                            # Check if there is still time remaining
                            time_passed = pygame.time.get_ticks() - start_time
                            if time_passed < self.total_time:
                                # Add 1 second to the remaining time
                                start_time += 1000
                                # Choose a new random word
                                self.random_word = random.choice(self.word_list)
                                self.label = self.font.render(self.random_word, True, BLACK)
                                self.word_rect = self.label.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                            else:
                                # No time remaining, end the game loop
                                running = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.user_input = self.user_input[:-1]

            # Get the current time remaining
            time_remaining = max(0, self.total_time - (pygame.time.get_ticks() - start_time))

            # Clear the screen
            self.screen.fill(WHITE)

            # Draw the score and timer labels
            score_label = self.font.render("Score: " + str(self.score), True, BLACK)
            self.screen.blit(score_label, (10, 10))
            time_label = self.font.render("Time: " + str(time_remaining // 1000), True, BLACK)
            self.screen.blit(time_label, (SCREEN_WIDTH - time_label.get_width() - 10, 10))

            # Draw the random word label
            self.screen.blit(self.label, self.word_rect)

            # Draw the user input label
            user_input_label = self.font.render(self.user_input, True, BLUE)
            user_input_rect = user_input_label.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 10))
            self.screen.blit(user_input_label, user_input_rect)

            # Increase time remaining every second
            if pygame.time.get_ticks() % 1000 == 0 and time_remaining > 0:
                time_remaining -= 1000

            # Draw the exit button
            exit_button.draw()

            # Update the display
            pygame.display.flip()

        # Game over, display final score
        self.screen.fill(WHITE)
        game_over_label = self.font.render("Game Over", True, BLACK)
        score_label = self.font.render("Final Score: " + str(self.score), True, BLACK)
        game_over_rect = game_over_label.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        score_rect = score_label.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(game_over_label, game_over_rect)
        self.screen.blit(score_label, score_rect)
        pygame.display.flip()

        # Wait for a key press before quitting
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

        # Quit pygame
        pygame.quit()
        sys.exit()