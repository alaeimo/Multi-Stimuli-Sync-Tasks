from screeninfo import get_monitors
import math

messages = {"fa":{
                  "start":"برای ادامه شروع را بزنید.",
                  "start_btn":"شروع",
                  "get_coordination":"لطفا یکی از حالت‌های هماهنگی زیر را انتخاب کنید:",
                  "get_stimulus_type":"لطفا یکی از حالت‌های محرک‌ها را انتخاب کنید:",
                  "inphase":"بین مرحله‌ای",
                  "anti":"برون مرحله‌ای",
                  "inter":"درون مرحله‌ای",
                  "vis_stimulus":"محرک بصری",
                  "aud_stimulus":"محرک صوتی",
                  "display_right_stimulus":'Display Right Stimulus',
                  "display_left_stimulus":'Display Left Stimulus',
                  "right_ctrl_press":'Right CTRL Press',
                  "left_ctrl_press":'Left CTRL Press',
                  "display_stop":"Display Stop",
                  "quit_btn":"خروج",
                  "stop":"Stop",
                },
          "en":{
              "start":"To continue, press Start.",
              "start_btn":"Start",
              "get_coordination":"Please select one of the following coordination modes:",
              "get_stimulus_type":"Please select one of the stimulus modes:",
              "inphase":"INPHASE",
              "anti":"ANTI",
              "inter":"INTER",
              "vis_stimulus":"Visual",
              "aud_stimulus":"Auditory",
              "display_right_stimulus":'Display Right Stimulus',
              "display_left_stimulus":'Display Left Stimulus',
              "right_ctrl_press":'Right CTRL Press',
              "left_ctrl_press":'Left CTRL Press',
              "display_stop":"Display Stop",
              "quit_btn":"Quit",
              "stop":"Stop"
              }
          }

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

# Constants
monitor = get_monitors()[0]
SCREEN_WIDTH = monitor.width
SCREEN_HEIGHT = monitor.height
BG_COLOR = (255, 255, 255)
SQUARE_COLOR = (255, 0, 0)
TEXT_COLOR = (0, 0, 0)
BUTTON_COLOR = (135, 206, 250)  
QUIT_BUTTON_COLOR = (220, 20, 60)
START_BUTTON_COLOR = (34, 139, 34)

SQUARE_WIDTH  = 2.5 #cm
SQUARE_HEIGHT = 2.5 #cm
SQUARE_DISTANCE_FROM_CENTER = 5 #cm

SQUARE_WIDTH_PIXEL = centimeter_to_pixel(SQUARE_WIDTH)
SQUARE_HEIGHT_PIXEL = centimeter_to_pixel(SQUARE_HEIGHT)
SQUARE_DISTANCE_FROM_CENTER_PIXEL = centimeter_to_pixel(SQUARE_DISTANCE_FROM_CENTER)
SQUARE_HALF_WIDTH_PIXEL = centimeter_to_pixel(SQUARE_WIDTH/2)
SQUARE_HALF_HEIGHT_PIXEL = centimeter_to_pixel(SQUARE_HEIGHT/2)


STIMULUS_DURATION = 40  #milliseconds
MAX_DURATION = 20  #seconds
STIMULUS_REPETITION = 5
INTERVAL_DELAY = 1000 #milliseconds
STOP_DURATION = 2000 #milliseconds
STIMULI_DELAY = {"INPHASE":0, "ANTI":500, "INTER":250}

FONT_PATH = "fonts/Vazir.ttf" 
FONT_SIZE = 24
APP_NAME = "Multi Stimuli Sync Tasks"
LANGUAGE = "fa" #en or fa