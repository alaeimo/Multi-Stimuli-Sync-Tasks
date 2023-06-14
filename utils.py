
import pandas as pd
from dataclasses import dataclass, field
from screeninfo import get_monitors

@dataclass 
class TimeStamp:
    label: str = field(repr=True)
    time: float = field(repr=True)

@dataclass
class Trial:
    coordination:str = field(default=None, repr=True) #INPHASE, ANTI, INTER
    stimulus_type:str = field(default=None, repr=True) #VIS, AUD
    stimulus_repetition:int = field(default=5, repr=True) #times
    stimulus_duration:int = field(default=40, repr=True) #milliseconds
    stimuli_delay: int = field(default=0, repr=True) #milliseconds
    interval_delay:int = field(default=1000, repr=True) #milliseconds
    stop_duration:int = field(default=2000, repr=True) #milliseconds
    max_duration: int = field(default=20, repr=True) #seconds
    right_stimuli_times:list = field(default_factory=list, repr=True)
    left_stimuli_times:list = field(default_factory=list, repr=True)
    right_ctrl_press_times:list = field(default_factory=list, repr=True)
    left_ctrl_press_times:list = field(default_factory=list, repr=True)
    timestamp: list = field(default_factory=list, repr=True)
    start_time: int = field(default=0, repr=True)
    stop: bool= False

    def save_csv(self, file_name):
        data = {
                'coordination': [self.coordination],
                'stimulus_type': [self.stimulus_type],
                'stimulus_repetition': [self.stimulus_repetition],
                'stimulus_duration': [self.stimulus_duration],
                'stimuli_delay': [self.stimuli_delay],
                'interval_delay': [self.interval_delay],
                'stop_duration': [self.stop_duration],
                'max_duration': [self.max_duration],
                'right_stimuli_time': [round((time - self.start_time)*1000,3) for time in self.right_stimuli_times],
                'left_stimuli_time': [round((time - self.start_time)*1000,3) for time in self.left_stimuli_times],
                'right_ctrl_press_time': [round((time - self.start_time)*1000,3) for time in self.right_ctrl_press_times],
                'left_ctrl_press_time': [round((time - self.start_time)*1000,3) for time in self.left_ctrl_press_times],
            }
        max_length = max(len(v) for v in data.values())
        data = {k:v + [None] * (max_length - len(v)) for k,v in data.items()}
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False, encoding="utf-8")

    def save_timestamp(self, file_name):
        data = {str(idx) + ": " + ts.label: round((ts.time - self.start_time)*1000,3)  for idx , ts in enumerate(sorted(self.timestamp, key=lambda ts:ts.time))}
        df = pd.DataFrame([data])
        df.to_csv(file_name, index=False, encoding='utf-8-sig')



def get_screen_dpi():
    monitor = get_monitors()[0]
    screen_width, screen_height = monitor.width, monitor.height
    physical_width, physical_height = monitor.width_mm / 25.4, monitor.height_mm / 25.4
    dpi_x = screen_width / physical_width
    dpi_y = screen_height / physical_height
    return dpi_x, dpi_y

def centimeter_to_pixel_x(centimeters):
    inches = centimeters / 2.54
    dpi_x, _ = get_screen_dpi()
    pixels = inches * dpi_x
    return int(pixels)

def centimeter_to_pixel_y(centimeters):
    inches = centimeters / 2.54
    _, dpi_y = get_screen_dpi()
    pixels = inches * dpi_y
    return int(pixels)