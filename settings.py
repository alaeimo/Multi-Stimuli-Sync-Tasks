from utils import get_monitors, centimeter_to_pixel_x, centimeter_to_pixel_y

messages = {"fa":{
                  "start":"Start",
                  "start_btn":"شروع",
                  "get_coordination":"لطفا یکی از حالت‌های هماهنگی را انتخاب کنید",
                  "get_stimulus_type":"لطفا یکی از انواع محرک‌ها را انتخاب کنید",
                  "inphase":"درون مرحله‌ای",
                  "inter":"بین مرحله‌ای",
                  "anti":"برون مرحله‌ای",
                  "vis_stimulus":"محرک بصری",
                  "aud_stimulus":"محرک صوتی",
                  "exit_btn":"خروج",
                  "stop":"Stop",
                },
          "en":{
              "start":"To continue, press Start",
              "start_btn":"Start",
              "get_coordination":"Please select one of the following coordination modes",
              "get_stimulus_type":"Please select one of the stimulus modes",
              "inphase":"INPHASE",
              "inter":"INTER",
              "anti":"ANTI",
              "vis_stimulus":"Visual",
              "aud_stimulus":"Auditory",
              "exit_btn":"Exit",
              "stop":"Stop"
              }
          }

# Constants
monitor = get_monitors()[0]
SCREEN_WIDTH = monitor.width  #pixel. e.g. 800
SCREEN_HEIGHT = monitor.height #pixel. e.g. 600

BG_COLOR = (255, 255, 255) #RGB
SQUARE_COLOR = (255, 0, 0) #RGB

TEXT_COLOR = (0, 0, 0) #RGB
BUTTON_COLOR = (135, 206, 250) #RGB  

EXIT_BUTTON_COLOR = (220, 20, 60) #RGB
START_BUTTON_COLOR = (34, 139, 34) #RGB

SQUARE_WIDTH  = 2.5 #cm
SQUARE_HEIGHT = 2.5 #cm
SQUARE_DISTANCE_FROM_CENTER = 5 #cm

SQUARE_WIDTH_PIXEL = centimeter_to_pixel_x(SQUARE_WIDTH)
SQUARE_HEIGHT_PIXEL = centimeter_to_pixel_y(SQUARE_HEIGHT)
SQUARE_DISTANCE_FROM_CENTER_PIXEL = centimeter_to_pixel_x(SQUARE_DISTANCE_FROM_CENTER)
SQUARE_HALF_WIDTH_PIXEL = centimeter_to_pixel_x(SQUARE_WIDTH/2)
SQUARE_HALF_HEIGHT_PIXEL = centimeter_to_pixel_y(SQUARE_HEIGHT/2)

DISPLAY_START_EXIT_BUTTONS = False
DISPLAY_GET_COOR_STI_MSGS = True


STIMULUS_DURATION = 40  #milliseconds
MAX_DURATION = 20  #seconds
STIMULUS_REPETITION = 5
INTERVAL_DELAY = 1000 #milliseconds
STOP_DURATION = 2000 #milliseconds
STIMULI_DELAY = {"INPHASE":0, "INTER":250, "ANTI":500}

RIGHT_HAND_SOUND_NAME = "500hz.wav"
LEFT_HAND_SOUND_NAME = "4000hz.wav"

FONT_PATH = "fonts/Vazir.ttf" 
FONT_SIZE = 40
APP_NAME = "Multi Stimuli Sync Tasks"
LANGUAGE = "fa" #en or fa