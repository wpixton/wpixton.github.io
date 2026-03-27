import pygame
import time
from wordle import Game, Status

# set up the game 
pygame.init()
WIDTH, HEIGHT = 800, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle in Pygame")

clock = pygame.time.Clock()

FONT = pygame.font.SysFont("arial", 48)
FONT_SMALL = pygame.font.SysFont("arial", 32)
KEY_FONT = pygame.font.SysFont("arial", 28)

# set the colors
COLOR_BG = (18, 18, 18)
COLOR_EMPTY = (40, 40, 40)
COLOR_BORDER = (90, 90, 90)
COLOR_CORRECT = (83, 141, 78)
COLOR_WRONG_PLACE = (181, 159, 59)
COLOR_GUESSED = (58, 58, 60)
COLOR_UNUSED_KEY = (120, 124, 126)
COLOR_TEXT = (255, 255, 255)

TILE_SIZE = 70
TILE_GAP = 10
GRID_TOP = 100
GRID_LEFT = (WIDTH - (TILE_SIZE * 5 + TILE_GAP * 4)) // 2

# on screen letter display
KEY_ROWS = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
KEY_WIDTH = 60
KEY_HEIGHT = 60
KEY_GAP = 8
KEYBOARD_TOP = 700



# Draw a tile

def draw_tile(x, y, letter, status):
    if status == Status.CORRECT:
        color = COLOR_CORRECT
    elif status == Status.WRONG_PLACEMENT:
        color = COLOR_WRONG_PLACE
    elif status == Status.GUESSED:
        color = COLOR_GUESSED
    else:
        color = COLOR_EMPTY

    rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, color, rect, border_radius=5)
    pygame.draw.rect(screen, COLOR_BORDER, rect, width=2, border_radius=5)

    if letter:
        text = FONT.render(letter.upper(), True, COLOR_TEXT)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)



# Draw keyboard

def draw_keyboard(game):
    start_x = (WIDTH - (10 * (KEY_WIDTH + KEY_GAP) - KEY_GAP)) // 2
    for row_idx, row in enumerate(KEY_ROWS):
        y = KEYBOARD_TOP + row_idx * (KEY_HEIGHT + KEY_GAP)
        row_offset = (10 - len(row)) * (KEY_WIDTH + KEY_GAP) // 2
        for col_idx, char in enumerate(row):
            x = start_x + col_idx * (KEY_WIDTH + KEY_GAP) + row_offset

            # Find status from letter dictionary
            status = Status.NOT_GUESSED
            for letter in game._dictionary.letter_list:
                if letter.name == char:
                    status = letter.status
                    break

            if status == Status.NOT_GUESSED:
                color = COLOR_UNUSED_KEY
            elif status == Status.CORRECT:
                color = COLOR_CORRECT
            elif status == Status.WRONG_PLACEMENT:
                color = COLOR_WRONG_PLACE
            else:
                color = COLOR_GUESSED

            rect = pygame.Rect(x, y, KEY_WIDTH, KEY_HEIGHT)
            pygame.draw.rect(screen, color, rect, border_radius=5)
            pygame.draw.rect(screen, COLOR_BORDER, rect, width=2, border_radius=5)

            key_text = KEY_FONT.render(char, True, COLOR_TEXT)
            key_rect = key_text.get_rect(center=rect.center)
            screen.blit(key_text, key_rect)



# Draw previous guesses

def draw_guesses(guesses):
    for row_idx, guess in enumerate(guesses):
        for col_idx, letter_obj in enumerate(guess.letter_list):
            x = GRID_LEFT + col_idx * (TILE_SIZE + TILE_GAP)
            y = GRID_TOP + row_idx * (TILE_SIZE + TILE_GAP)
            draw_tile(x, y, letter_obj.name, letter_obj.status)



# Draw current guess

def draw_current_guess(current_text, row_idx):
    for col_idx in range(5):
        x = GRID_LEFT + col_idx * (TILE_SIZE + TILE_GAP)
        y = GRID_TOP + row_idx * (TILE_SIZE + TILE_GAP)
        letter = current_text[col_idx].upper() if col_idx < len(current_text) else ""
        draw_tile(x, y, letter, Status.NOT_GUESSED)



# Flip animation

def flip_row(guess, row_idx):
    for col_idx, letter_obj in enumerate(guess.letter_list):
        x = GRID_LEFT + col_idx * (TILE_SIZE + TILE_GAP)
        y = GRID_TOP + row_idx * (TILE_SIZE + TILE_GAP)
        for scale in range(70, -1, -5):
            pygame.draw.rect(screen, COLOR_BG, (x, y, TILE_SIZE, TILE_SIZE))
            rect = pygame.Rect(x, y, TILE_SIZE, scale)
            pygame.draw.rect(screen, COLOR_EMPTY, rect, border_radius=5)
            pygame.display.flip()
            clock.tick(120)
        draw_tile(x, y, letter_obj.name, letter_obj.status)
        pygame.display.flip()
        pygame.time.delay(100)



# Main Game Loop

def main():
    game = Game()
    current_text = ""
    guesses = []
    won = False
    game_over = False
    shake = False

    running = True
    while running:
       
        # Handle Events
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not game_over and event.type == pygame.KEYDOWN:

                # A-Z typing
                if pygame.K_a <= event.key <= pygame.K_z:
                    if len(current_text) < 5:
                        current_text += event.unicode.lower()

                # Backspace
                if event.key == pygame.K_BACKSPACE:
                    current_text = current_text[:-1]

                # Submit guess
                if event.key == pygame.K_RETURN:
                    if len(current_text) == 5:
                        guess, won = game.submit_guess(current_text)
                        if guess:
                            guesses.append(guess)
                            flip_row(guess, len(guesses) - 1)
                            current_text = ""

                            if won:
                                game_over = True
                            elif len(guesses) >= 6:
                                game_over = True
                        else:
                            # Invalid word shake
                            shake = True

        # Drawing
     
        screen.fill(COLOR_BG)

        if shake:
            for dx in [-10, 10, -10, 10, 0]:
                screen.fill(COLOR_BG)
                draw_guesses(guesses)
                draw_current_guess(current_text, len(guesses))
                draw_keyboard(game)
                screen.blit(pygame.Surface((0, 0)), (dx, 0))
                pygame.display.flip()
                clock.tick(120)
            shake = False
        else:
            draw_guesses(guesses)
            if not game_over and len(guesses) < 6:
                draw_current_guess(current_text, len(guesses))
            draw_keyboard(game)

        # Win / Lose message
        if game_over:
            msg = "You Win!" if won else f"You Lose! Word: {game.get_correct_word().word_string.upper()}"
            text = FONT_SMALL.render(msg, True, COLOR_TEXT)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 650))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()