import arabic_reshaper
from bidi.algorithm import get_display
import threading
import math
import pygame
from pynput import keyboard
import time
from utils import Result
from config import *

def get_screen_dpi():
    monitor = get_monitors()[0]
    screen_width, screen_height =  monitor.width, monitor.height
    physical_width, physical_height = monitor.width_mm/25.4 , monitor.height_mm/25.4
    diagonal_pixels = math.sqrt(screen_width ** 2 + screen_height ** 2)
    diagonal_inches = math.sqrt(physical_width ** 2 + physical_height ** 2)
    dpi = diagonal_pixels / diagonal_inches
    return dpi

def centimeter_to_pixel(centimeters):
    inches = centimeters / 2.54
    dpi = get_screen_dpi()
    pixels = inches * dpi
    return int(pixels)


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(APP_NAME)
font = pygame.font.Font(FONT_PATH, FONT_SIZE)

# Function to display text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Function to draw a square on the screen
def draw_square(x, y):
    pygame.draw.rect(screen, 
                     (255, 0, 0), 
                     pygame.Rect(x, y, (centimeter_to_pixel(2.5)),centimeter_to_pixel(2.5)))

# Function to play a sound
def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def get_bidi_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

# Function to show the instructions
def show_instructions():
    screen.fill(BG_COLOR)
    text = get_bidi_text(language_messages[LANGUAGE]["start"])
    draw_text(text, font, (0, 0, 0), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL or event.key == pygame.K_RETURN:
                    return

def get_coordination():
    screen.fill(BG_COLOR)
    # Display the green cross in the middle
    draw_text("x", font, (0, 255, 0), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    pygame.time.wait(500)

    # Button variables
    button_width, button_height = 200, 50
    button_x = (SCREEN_WIDTH - button_width) // 2
    button_y = (SCREEN_HEIGHT - button_height) // 2

    corner_radius = 10

    inter_button_rect = pygame.Rect(button_x - 220, button_y + 60, button_width, button_height)
    anti_button_rect = pygame.Rect(button_x, button_y + 60, button_width, button_height)
    inphase_button_rect = pygame.Rect(button_x + 220, button_y + 60, button_width, button_height)

    # Draw buttons with rounded corners
    pygame.draw.rect(screen, BUTTON_COLOR, inphase_button_rect, border_radius=corner_radius)
    pygame.draw.rect(screen, BUTTON_COLOR, anti_button_rect, border_radius=corner_radius)
    pygame.draw.rect(screen, BUTTON_COLOR, inter_button_rect, border_radius=corner_radius)

    # Calculate text position
    inphase_text_x = inphase_button_rect.centerx
    inphase_text_y = inphase_button_rect.centery
    anti_text_x = anti_button_rect.centerx
    anti_text_y = anti_button_rect.centery
    inter_text_x = inter_button_rect.centerx
    inter_text_y = inter_button_rect.centery

    draw_text(get_bidi_text(language_messages[LANGUAGE]["inter"]), font, TEXT_COLOR, inter_text_x, inter_text_y)
    draw_text(get_bidi_text(language_messages[LANGUAGE]["anti"]), font, TEXT_COLOR, anti_text_x, anti_text_y)
    draw_text(get_bidi_text(language_messages[LANGUAGE]["inphase"]), font, TEXT_COLOR, inphase_text_x, inphase_text_y)


    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if inphase_button_rect.collidepoint(event.pos):
                        return "INPHASE"
                    elif anti_button_rect.collidepoint(event.pos):
                        return "ANTI"
                    elif inter_button_rect.collidepoint(event.pos):
                        return "INTER"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL:
                    return "INPHASE"
                if event.key == pygame.K_SPACE:
                    return "ANTI"
                if event.key == pygame.K_LCTRL:
                    return "INTER"

def get_stimulus_type():
    screen.fill(BG_COLOR)
    # Display the green cross in the middle
    draw_text("x", font, (0, 255, 0), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    pygame.time.wait(500)

    # Button variables
    button_width, button_height = 200, 50
    button_x = (SCREEN_WIDTH - button_width) // 2
    button_y = (SCREEN_HEIGHT - button_height) // 2

    corner_radius = 10

    aud_button_rect = pygame.Rect(button_x - 110, button_y + 60, button_width, button_height)
    vis_button_rect = pygame.Rect(button_x + 110, button_y + 60, button_width, button_height)
    # Draw buttons with rounded corners
    pygame.draw.rect(screen, BUTTON_COLOR, vis_button_rect, border_radius=corner_radius)
    pygame.draw.rect(screen, BUTTON_COLOR, aud_button_rect, border_radius=corner_radius)

    # Calculate text position
    vis_text_x = vis_button_rect.centerx
    vis_text_y = vis_button_rect.centery
    aud_text_x = aud_button_rect.centerx
    aud_text_y = aud_button_rect.centery

    draw_text(get_bidi_text(language_messages[LANGUAGE]["aud_stimulus"]), font, TEXT_COLOR, aud_text_x, aud_text_y)
    draw_text(get_bidi_text(language_messages[LANGUAGE]["vis_stimulus"]), font, TEXT_COLOR, vis_text_x, vis_text_y)


    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if vis_button_rect.collidepoint(event.pos):
                        return "VIS"
                    elif aud_button_rect.collidepoint(event.pos):
                        return "AUD"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL:
                    return "VIS"
                if event.key == pygame.K_LCTRL:
                    return "AUD"


def display_stimuli(coordination, stimulus, start_time, result):
    counter = 0
    stimuli_finished = threading.Event()

    while not stimuli_finished.is_set():
        if time.time() - start_time >= MAX_PHASE_DURATION:
            stimuli_finished.set()
            break
        if counter >= STIMULUS_REPETITION:
            stimuli_finished.set()
            break

        counter += 1
        screen.fill(BG_COLOR)

        # Display the green cross in the middle
        draw_text("x", font, (0, 255, 0), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        pygame.display.flip()
        pygame.time.wait(INTERVAL_DELAY)

        if coordination == "INPHASE":
            if stimulus == "VIS":
                draw_square(SCREEN_WIDTH / 2 + centimeter_to_pixel(5), 
                            SCREEN_HEIGHT / 2 - centimeter_to_pixel(1.25))
                right_stimuli_time = time.time()

                pygame.time.wait(INPHASE_DELAY)

                draw_square(SCREEN_WIDTH / 2 - (centimeter_to_pixel(5) + centimeter_to_pixel(2.5)), 
                            SCREEN_HEIGHT / 2 - centimeter_to_pixel(1.25))
                left_stimuli_time = time.time()

                result.right_stimuli_times.append((right_stimuli_time))
                result.left_stimuli_times.append((left_stimuli_time))
                
            elif stimulus == "AUD":
                play_sound("500hz.wav")
                right_stimuli_time = time.time()

                pygame.time.wait(INPHASE_DELAY)

                play_sound("4000hz.wav")
                left_stimuli_time = time.time()

                result.right_stimuli_times.append((right_stimuli_time))
                result.left_stimuli_times.append((left_stimuli_time))

        elif coordination == "ANTI":
            if stimulus == "VIS":
                draw_square(SCREEN_WIDTH / 2 + centimeter_to_pixel(5), 
                            SCREEN_HEIGHT / 2 - centimeter_to_pixel(1.25))
                right_stimuli_time = time.time()

                pygame.time.wait(ANTI_DELAY)

                draw_square(SCREEN_WIDTH / 2 - (centimeter_to_pixel(5) + centimeter_to_pixel(2.5)), 
                            SCREEN_HEIGHT / 2 - centimeter_to_pixel(1.25))
                left_stimuli_time = time.time()

                result.right_stimuli_times.append((right_stimuli_time))
                result.left_stimuli_times.append((left_stimuli_time))

            elif stimulus == "AUD":
                play_sound("500hz.wav")
                right_stimuli_time = time.time()

                pygame.time.wait(ANTI_DELAY)

                play_sound("4000hz.wav")
                left_stimuli_time = time.time()

                result.right_stimuli_times.append((right_stimuli_time))
                result.left_stimuli_times.append((left_stimuli_time))

        elif coordination == "INTER":
            if stimulus == "VIS":
                draw_square(SCREEN_WIDTH / 2 + centimeter_to_pixel(5), 
                            SCREEN_HEIGHT / 2 - centimeter_to_pixel(1.25))
                right_stimuli_time = time.time()

                pygame.time.wait(INTER_DELAY)

                draw_square(SCREEN_WIDTH / 2 - (centimeter_to_pixel(5) + centimeter_to_pixel(2.5)), 
                            SCREEN_HEIGHT / 2 - centimeter_to_pixel(1.25))
                left_stimuli_time = time.time()

                result.right_stimuli_times.append((right_stimuli_time))
                result.left_stimuli_times.append((left_stimuli_time))

            elif stimulus == "AUD":
                play_sound("500hz.wav")
                right_stimuli_time = time.time()

                pygame.time.wait(INTER_DELAY)

                play_sound("4000hz.wav")
                left_stimuli_time = time.time()

                result.right_stimuli_times.append((right_stimuli_time))
                result.left_stimuli_times.append((left_stimuli_time))
        
        pygame.display.flip()
        pygame.time.wait(STIMULUS_DURATION)

    
    screen.fill(BG_COLOR)
    text = get_bidi_text(language_messages[LANGUAGE]["stop"])
    draw_text(text, font, (0, 0, 0), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.flip()
    pygame.time.wait(DISPLAY_STOP)

def wait_for_input(start_time, result):
    input_finished= threading.Event()
    def on_press(key):
        if key == keyboard.Key.ctrl_l:
            result.left_ctrl_press_times.append(time.time())
        elif key == keyboard.Key.ctrl_r:
            result.right_ctrl_press_times.append(time.time())

    with keyboard.Listener(on_press=on_press) as listener:
        while not input_finished.is_set():
            if time.time() - start_time >= MAX_PHASE_DURATION:
                input_finished.set()
                break
# Function to run a trial
def run_trial(coordination, stimulus):

    start_time = time.time()
    result = Result()
    stimuli_thread = threading.Thread(target=display_stimuli, args=(coordination, stimulus,start_time, result))
    input_thread = threading.Thread(target=wait_for_input, args=(start_time,result))

    stimuli_thread.start()
    input_thread.start()

    # Wait for both threads to finish
    stimuli_thread.join()
    input_thread.join()

    return result
# Function to run the main program
def main():
    show_instructions()
    coordination = get_coordination()
    stimulus = get_stimulus_type()
    try:
        result = run_trial(coordination, stimulus)

        # Print the recorded times
        print("Right Stimuli Times:", result.right_stimuli_times)
        print("Left Stimuli Times:", result.left_stimuli_times)
        print("Right CTRL Press Times:", result.right_ctrl_press_times)
        print("Left CTRL Press Times:", result.left_ctrl_press_times)
    finally:
        pygame.quit()

# Run the program
if __name__ == "__main__":
    main()
