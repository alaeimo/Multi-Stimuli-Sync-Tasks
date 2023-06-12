import os , argparse, time, threading, random
import arabic_reshaper
from bidi.algorithm import get_display
import pygame
from pynput import keyboard
from utils import Trial, TimeStamp
from config import *


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
def draw_square(x, y, color):
    pygame.draw.rect(screen,
                     color, 
                     pygame.Rect(x, y, SQUARE_WIDTH_PIXEL , SQUARE_HEIGHT_PIXEL))

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
    # Button variables
    button_width, button_height = 110, 50
    button_x = (SCREEN_WIDTH - button_width) // 2
    button_y = (SCREEN_HEIGHT - button_height) // 2

    corner_radius = 10

    start_button_rect = pygame.Rect(button_x + 70, button_y + 50, button_width, button_height) 
    quit_button_rect =  pygame.Rect(button_x - 70, button_y + 50, button_width, button_height)
    # Draw buttons with rounded corners
    pygame.draw.rect(screen, START_BUTTON_COLOR, start_button_rect, border_radius=corner_radius)
    pygame.draw.rect(screen, QUIT_BUTTON_COLOR, quit_button_rect, border_radius=corner_radius)


    # Calculate text position
    start_text_x = start_button_rect.centerx
    start_text_y = start_button_rect.centery
    quit_text_x = quit_button_rect.centerx
    quit_text_y = quit_button_rect.centery

    draw_text(get_bidi_text(messages[LANGUAGE]["start_btn"]), font, TEXT_COLOR, start_text_x, start_text_y)
    draw_text(get_bidi_text(messages[LANGUAGE]["quit_btn"]), font, TEXT_COLOR, quit_text_x, quit_text_y)

    pygame.display.flip()
    pygame.event.clear()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL or event.key == pygame.K_RETURN:
                    return False
                if event.key == pygame.K_ESCAPE:
                    return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if start_button_rect.collidepoint(event.pos):
                        return False
                    elif quit_button_rect.collidepoint(event.pos):
                        return True

def get_coordination(test):
    if test: return random.choice(["INPHASE", "ANTI","INTER"])
    screen.fill(BG_COLOR)
    draw_text("x", font, (0, 255, 0), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.flip()
    pygame.time.delay(500)
    # Display the green cross in the middle
    text = get_bidi_text(messages[LANGUAGE]["get_coordination"])
    draw_text(text, font, (0, 0, 0), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60)

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

def get_stimulus_type(test):
    if test: return random.choice(["VIS", "AUD"])
    screen.fill(BG_COLOR)
    draw_text("x", font, (0, 255, 0), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.flip()
    pygame.time.delay(500)
    text = get_bidi_text(messages[LANGUAGE]["get_stimulus_type"])
    draw_text(text, font, (0, 0, 0), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60)

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


def display_stimuli(trial:Trial, start_time: float):
    counter = 0
    stimuli_finished = threading.Event()
    # Display the green cross in the middle
    while not stimuli_finished.is_set():
        if time.time() - start_time >= trial.max_duration:
            stimuli_finished.set()
            trial.stop = True
            break
        if counter >= trial.stimulus_repetition:
            stimuli_finished.set()
            break

        screen.fill(BG_COLOR)
        pygame.display.flip()
        pygame.time.delay(trial.interval_delay)
        counter += 1
        if trial.stimulus_type == "VIS":
            draw_square(SCREEN_WIDTH / 2 + SQUARE_DISTANCE_FROM_CENTER_PIXEL, 
                        SCREEN_HEIGHT / 2 - SQUARE_HALF_HEIGHT_PIXEL,
                        SQUARE_COLOR)
            pygame.display.flip()
            right_stimuli_time = time.time()

            if trial.coordination != "INPHASE": 
                pygame.time.delay(trial.stimulus_duration)
                screen.fill(BG_COLOR)
                pygame.display.flip()

            pygame.time.delay(trial.stimuli_delay-trial.stimulus_duration)

            draw_square(SCREEN_WIDTH / 2 - (SQUARE_DISTANCE_FROM_CENTER_PIXEL + SQUARE_WIDTH_PIXEL), 
                        SCREEN_HEIGHT / 2 - SQUARE_HALF_HEIGHT_PIXEL,
                        SQUARE_COLOR)
            pygame.display.flip()
            left_stimuli_time = time.time()

            pygame.time.delay(trial.stimulus_duration)

        elif trial.stimulus_type == "AUD":
            play_sound("500hz.wav")
            right_stimuli_time = time.time()

            pygame.time.delay(trial.stimuli_delay)

            play_sound("4000hz.wav")
            left_stimuli_time = time.time()

        trial.timestamp.append(TimeStamp(messages[LANGUAGE]['display_right_stimulus'],right_stimuli_time))
        trial.timestamp.append(TimeStamp(messages[LANGUAGE]['display_left_stimulus'],left_stimuli_time))
        trial.right_stimuli_times.append((right_stimuli_time))
        trial.left_stimuli_times.append((left_stimuli_time))

    screen.fill(BG_COLOR)
    text = get_bidi_text(messages[LANGUAGE]["stop"])
    draw_text(text, font, (0, 0, 0), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.flip()
    trial.timestamp.append(TimeStamp(messages[LANGUAGE]["display_stop"],time.time()))
    pygame.time.delay(trial.stop_duration)
    trial.stop = True

def wait_for_input(trial: Trial, start_time:float):
    input_finished= threading.Event()
    def on_press(key):
        if key == keyboard.Key.ctrl_l:
            left_ctrl_press = time.time()
            trial.left_ctrl_press_times.append(left_ctrl_press)
            trial.timestamp.append(TimeStamp(messages[LANGUAGE]["left_ctrl_press"],left_ctrl_press))
            
        elif key == keyboard.Key.ctrl_r:
            right_ctrl_press = time.time()
            trial.right_ctrl_press_times.append(right_ctrl_press)
            trial.timestamp.append(TimeStamp(messages[LANGUAGE]["right_ctrl_press"],right_ctrl_press))

    with keyboard.Listener(on_press=on_press) as listener:
        while not input_finished.is_set():
            if time.time() - start_time >= trial.max_duration:
                input_finished.set()
                break
            if trial.stop:
                input_finished.set()
                break
    
# Function to run a trial
def run_trial(trial: Trial):

    start_time = time.time()
    trial.start_time = start_time
    trial.timestamp.append(TimeStamp("Start", start_time))
    stimuli_thread = threading.Thread(target=display_stimuli, args=(trial, start_time))
    input_thread = threading.Thread(target=wait_for_input, args=(trial, start_time))

    input_thread.start()
    stimuli_thread.start()

    # Wait for both threads to finish
    input_thread.join()
    stimuli_thread.join()

    return trial
# Function to run the main program
def main(save, data_path, test):
    
    while True:
        quit = show_instructions()
        if not quit:
            coordination = get_coordination(test)
            stimulus_type = get_stimulus_type(test)
            trial = Trial(coordination = coordination,
                        stimulus_type = stimulus_type,
                        stimuli_delay=STIMULI_DELAY[coordination])
            trial.stop = False

            try:
                trial = run_trial(trial)
                if save:
                    trail_data_csv = os.path.join(data_path,f"data-{coordination.lower()}-{stimulus_type.lower()}.csv")
                    trail_timestamp_csv = os.path.join(data_path,f"timestamp-{coordination.lower()}-{stimulus_type.lower()}.csv")
                    trial.save_csv(trail_data_csv)
                    trial.save_timestamp(trail_timestamp_csv)
            finally:
                if test: 
                    pygame.quit()
                    break
        else:
            pygame.quit()
            break 

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--save', action='store_true',  help='Save CSV data?')
    parser.add_argument('--folder', help='Folder path to save CSV data')
    parser.add_argument('--test', action='store_true', help='Enable test mode')
    return parser.parse_args()

def create_folder_if_not_exists(folder_name):
    if not folder_name:
        raise ValueError("Folder name cannot be empty")

    base_path = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(base_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    elif os.listdir(folder_path):
        raise ValueError("Folder is not empty. Please choose an empty folder.")

    return folder_path
# Run the program
if __name__ == "__main__":
    args = parse_arguments()
    folder_name = args.folder
    if args.save:
        folder_path = create_folder_if_not_exists(folder_name)
    main(args.save, folder_name, args.test)
