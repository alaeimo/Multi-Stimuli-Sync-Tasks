from screeninfo import get_monitors

language_messages = {"fa":{
                            "start":"برای ادامه Start را بزنید.",
                            "inphase":"بین مرحله‌ای",
                            "anti":"برون مرحله‌ای",
                            "inter":"درون مرحله‌ای",
                            "vis_stimulus":"محرک بصری",
                            "aud_stimulus":"محرک صوتی",
                            "stop":"Stop",
                          },
                    "en":{
                        "start":"To continue, press Start.",
                        "inphase":"INPHASE",
                        "anti":"ANTI",
                        "inter":"INTER",
                        "vis_stimulus":"Visual",
                        "aud_stimulus":"Auditory",
                        "stop":"stop"
                        }
                    }



# Constants
monitor = get_monitors()[0]
SCREEN_WIDTH = 800 #monitor.width
SCREEN_HEIGHT = 600 #monitor.height
BG_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
BUTTON_COLOR = (135, 206, 250)  

STIMULUS_DURATION = 40  #milliseconds
MAX_PHASE_DURATION = 20  #seconds
STIMULUS_REPETITION = 5
DISPLAY_STOP = 2000 #millisecond
INTERVAL_DELAY = 1000 #milliseconds
STOP_DURATION = 2000 #milliseconds
INPHASE_DELAY = 0 #milliseconds
ANTI_DELAY = 500 #milliseconds
INTER_DELAY = 250 #milliseconds

FONT_PATH = "fonts/Vazir-Bold.ttf" 
FONT_SIZE = 24
APP_NAME = "Multi Stimuli Sync Tasks"
LANGUAGE = "fa" #en or fa