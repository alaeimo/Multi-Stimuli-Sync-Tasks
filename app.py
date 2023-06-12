import arabic_reshaper
from bidi.algorithm import get_display
import math
import pygame
import random
import time
import pandas as pd
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
    text = get_bidi_text(messages[LANGUAGE]["start"])
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

    pygame.time.delay(500)

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

    draw_text(get_bidi_text(messages[LANGUAGE]["inter"]), font, TEXT_COLOR, inter_text_x, inter_text_y)
    draw_text(get_bidi_text(messages[LANGUAGE]["anti"]), font, TEXT_COLOR, anti_text_x, anti_text_y)
    draw_text(get_bidi_text(messages[LANGUAGE]["inphase"]), font, TEXT_COLOR, inphase_text_x, inphase_text_y)


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

    pygame.time.delay(500)

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

    draw_text(get_bidi_text(messages[LANGUAGE]["aud_stimulus"]), font, TEXT_COLOR, aud_text_x, aud_text_y)
    draw_text(get_bidi_text(messages[LANGUAGE]["vis_stimulus"]), font, TEXT_COLOR, vis_text_x, vis_text_y)


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
                                      
# Function to run a trial
def run_trial(coordination, stimulus):
    left_stimuli_times = []
    right_stimuli_times = []
    press_times_left = []
    press_times_right = []
    start_time = time.time()

    counter = 0
    while time.time() - start_time < MAX_DURATION:
        if counter >= STIMULUS_REPETITION:
            break
        counter += 1
        screen.fill(BG_COLOR)

        # Display the green cross in the middle
        draw_text("x", font, (0, 255, 0), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        pygame.display.flip()
        pygame.time.delay(INTERVAL_DELAY)

        if coordination == "INPHASE":
            if stimulus == "VIS":
                draw_square(SCREEN_WIDTH / 2 + centimeter_to_pixel(5), 
                            SCREEN_HEIGHT / 2 - centimeter_to_pixel(1.25))
                right_stimuli_time = time.time()

                pygame.time.delay(STIMULI_DELAY[coordination])

                draw_square(SCREEN_WIDTH / 2 - (centimeter_to_pixel(5) + centimeter_to_pixel(2.5)), 
                            SCREEN_HEIGHT / 2 - centimeter_to_pixel(1.25))
                left_stimuli_time = time.time()

                right_stimuli_times.append((right_stimuli_time - start_time))
                left_stimuli_times.append((left_stimuli_time - start_time))
                
            elif stimulus == "AUD":
                play_sound("500hz.wav")
                right_stimuli_time = time.time()

                pygame.time.delay(STIMULI_DELAY[coordination])

                play_sound("4000hz.wav")
                left_stimuli_time = time.time()

                right_stimuli_times.append((right_stimuli_time - start_time))
                left_stimuli_times.append((left_stimuli_time - start_time))

        elif coordination == "ANTI":
            if stimulus == "VIS":
                draw_square(SCREEN_WIDTH / 2 + centimeter_to_pixel(5), 
                            SCREEN_HEIGHT / 2 - centimeter_to_pixel(1.25))
                right_stimuli_time = time.time()

                pygame.time.delay(STIMULI_DELAY[coordination])

                draw_square(SCREEN_WIDTH / 2 - (centimeter_to_pixel(5) + centimeter_to_pixel(2.5)), 
                            SCREEN_HEIGHT / 2 - centimeter_to_pixel(1.25))
                left_stimuli_time = time.time()

                right_stimuli_times.append((right_stimuli_time - start_time))
                left_stimuli_times.append((left_stimuli_time - start_time))

            elif stimulus == "AUD":
                play_sound("500hz.wav")
                right_stimuli_time = time.time()

                pygame.time.delay(STIMULI_DELAY[coordination])

                play_sound("4000hz.wav")
                left_stimuli_time = time.time()

                right_stimuli_times.append((right_stimuli_time - start_time))
                left_stimuli_times.append((left_stimuli_time - start_time))

        elif coordination == "INTER":
            if stimulus == "VIS":
                draw_square(SCREEN_WIDTH / 2 + centimeter_to_pixel(5), 
                            SCREEN_HEIGHT / 2 - centimeter_to_pixel(1.25))
                right_stimuli_time = time.time()

                pygame.time.delay(STIMULI_DELAY[coordination])

                draw_square(SCREEN_WIDTH / 2 - (centimeter_to_pixel(5) + centimeter_to_pixel(2.5)), 
                            SCREEN_HEIGHT / 2 - centimeter_to_pixel(1.25))
                left_stimuli_time = time.time()

                right_stimuli_times.append((right_stimuli_time - start_time))
                left_stimuli_times.append((left_stimuli_time - start_time))

            elif stimulus == "AUD":
                play_sound("500hz.wav")
                right_stimuli_time = time.time()

                pygame.time.delay(STIMULI_DELAY[coordination])

                play_sound("4000hz.wav")
                left_stimuli_time = time.time()

                right_stimuli_times.append((right_stimuli_time - start_time))
                left_stimuli_times.append((left_stimuli_time - start_time))
        
        pygame.display.flip()

        # Check for key presses
        st = time.time()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RCTRL:
                press_times_right.append((time.time() - right_stimuli_time))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
                press_times_left.append((time.time() - left_stimuli_time))
        print(time.time() - st)
        pygame.time.delay(STIMULUS_DURATION)

    return right_stimuli_times, left_stimuli_times, press_times_right, press_times_left

# Function to run the main program
def main():

    show_instructions()
    coordination = get_coordination()
    stimulus = get_stimulus_type()
    right_stimuli_times, left_stimuli_times, press_times_right, press_times_left = run_trial(coordination, stimulus)

    # Print the recorded times
    print("Right Stimuli Times:", right_stimuli_times)
    print("Left Stimuli Times:", left_stimuli_times)
    print("Right CTRL Press Times:", press_times_right)
    print("Left CTRL Press Times:", press_times_left)

    pygame.quit()

# Run the program
if __name__ == "__main__":
    main()
