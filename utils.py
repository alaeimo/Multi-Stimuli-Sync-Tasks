
import pandas as pd

class Experiment:
    def __init__(self):
        self.coordination = None
        self.stimulus = None
        self.right_stimuli_times = []
        self.left_stimuli_times = []
        self.right_ctrl_press_times = []
        self.left_ctrl_press_times = []