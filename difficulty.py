import pygame
import sys

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define the difficulty levels
EASY = 1
MEDIUM = 2
HARD = 3
EXIT = 4

# Define the word lists for each level
easy_words = ["apple", "banana", "cherry", "orange", "pear"]
medium_words = ["computer", "keyboard", "monitor", "mouse", "printer"]
hard_words = ["abacus", "algorithm", "binary", "compiler", "debugging"]

class DifficultySelector:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.title_label = self.font.render("<Select Difficulty>", True, BLACK)
        self.easy_label = self.font.render("1 - Easy", True, BLACK)
        self.medium_label = self.font.render("2 - Medium", True, BLACK)
        self.hard_label = self.font.render("3 - Hard", True, BLACK)
        self.exit_game = self.font.render("4 - Exit", True, BLACK)
        self.selected_difficulty = None

    def draw(self):
        self.screen.fill(WHITE)

        # Position the title label
        title_x = SCREEN_WIDTH // 2 - self.title_label.get_width() // 2
        title_y = SCREEN_HEIGHT // 3 - self.title_label.get_height() // 2 - 50
        self.screen.blit(self.title_label, (title_x, title_y))

        # Calculate the vertical spacing between labels
        label_spacing = (SCREEN_HEIGHT // 2) // 6

        # Position the difficulty labels
        easy_x = SCREEN_WIDTH // 2 - self.easy_label.get_width() // 2
        easy_y = SCREEN_HEIGHT // 2 - self.easy_label.get_height() // 2
        self.screen.blit(self.easy_label, (easy_x, easy_y))

        medium_x = SCREEN_WIDTH // 2 - self.medium_label.get_width() // 2
        medium_y = easy_y + label_spacing
        self.screen.blit(self.medium_label, (medium_x, medium_y))

        hard_x = SCREEN_WIDTH // 2 - self.hard_label.get_width() // 2
        hard_y = medium_y + label_spacing
        self.screen.blit(self.hard_label, (hard_x, hard_y))

        exit_x = SCREEN_WIDTH // 2 - self.exit_game.get_width() // 2
        exit_y = hard_y + label_spacing
        self.screen.blit(self.exit_game, (exit_x, exit_y))

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.selected_difficulty = EASY
                elif event.key == pygame.K_2:
                    self.selected_difficulty = MEDIUM
                elif event.key == pygame.K_3:
                    self.selected_difficulty = HARD
                elif event.key == pygame.K_4:
                    pygame.quit()
                    sys.exit()

    def run(self):
        while self.selected_difficulty is None:
            self.draw()
            self.get_input()
            pygame.display.flip()

        if self.selected_difficulty == EASY:
            return easy_words
        elif self.selected_difficulty == MEDIUM:
            return medium_words
        elif self.selected_difficulty == HARD:
            return hard_words