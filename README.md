# Multi Stimuli Sync Tasks

**Multi Stimuli Sync Tasks** is a Python-based application designed to present synchronized auditory and visual stimuli for cognitive and motor coordination experiments. It allows researchers to run controlled experiments with configurable in-phase, anti-phase, and inter-phase stimulus patterns, record responses, and save detailed timestamped data.

---

## Features

- **Multisensory Stimuli**: Visual (colored squares) and auditory (tones) stimuli.
- **Coordination Modes**: Supports `In-phase`, `Inter-phase`, and `Anti-phase` patterns.
- **User Input Logging**: Tracks keypresses for both right and left hand (Ctrl keys).
- **Data Recording**: Saves experimental data in CSV files with timestamps.
- **Customizable Settings**: Adjust experiment parameters via `settings.py`.
- **Two Execution Modes**:
  - **Trial Mode** (`-t`): Randomized stimulus presentation for familiarization.
  - **Main Experiment Mode**: Full control over stimulus type, coordination, and data saving.

---

## Installation

### Prerequisites

- Python 3.10 or above
- Pip package manager

### Steps

1. Download Python: [https://www.python.org/downloads](https://www.python.org/downloads)  
2. Install Python and ensure you check **Add Python to PATH** during installation.  
3. Open Command Prompt (cmd) and verify installation:

```bash
python --version
````

4. Navigate to the project directory:

```bash
cd D:\Works\Python\MultiStimuliSync
```

5. Install required Python packages:

```bash
pip install -r requirements.txt
```

---

## Usage

### Trial Mode (Familiarization)

Randomized coordination and stimulus selection:

```bash
python application.py -t
```

Trial mode with data saving:

```bash
python application.py -t -s folder_name
```

### Main Experiment Mode

Run experiment with full control over stimuli and coordination:

```bash
python application.py
```

With data saving:

```bash
python application.py -s folder_name
```

### Keyboard Controls

| Key        | Function                   |
| ---------- | -------------------------- |
| Right Ctrl | Select right-hand stimulus |
| Left Ctrl  | Select left-hand stimulus  |
| Space      | Between-phase selection    |
| Esc        | Exit experiment            |

---

## Configuration

All experiment parameters can be adjusted in `settings.py`:

| Parameter                        | Default             | Description                             |
| -------------------------------- | ------------------- | --------------------------------------- |
| `SCREEN_WIDTH` / `SCREEN_HEIGHT` | Full screen         | Dimensions of application window        |
| `BG_COLOR`                       | `(255, 255, 255)`   | Background color (RGB)                  |
| `SQUARE_COLOR`                   | `(255, 0, 0)`       | Visual stimulus color                   |
| `TEXT_COLOR`                     | `(0, 0, 0)`         | Text color                              |
| `SQUARE_WIDTH` / `SQUARE_HEIGHT` | `2.5`               | Size of visual stimulus (cm)            |
| `SQUARE_DISTANCE_FROM_CENTER`    | `5`                 | Distance from screen center (cm)        |
| `STIMULUS_DURATION`              | `40`                | Duration of each stimulus (ms)          |
| `STIMULUS_REPETITION`            | `5`                 | Number of repetitions per stimulus      |
| `INTERVAL_DELAY`                 | `1000`              | Delay between stimulus repetitions (ms) |
| `STOP_DURATION`                  | `2000`              | Duration of `Stop` message (ms)         |
| `MAX_DURATION`                   | `20`                | Maximum duration of one experiment (s)  |
| `RIGHT_HAND_SOUND_NAME`          | `"500hz.wav"`       | Right-hand auditory stimulus            |
| `LEFT_HAND_SOUND_NAME`           | `"4000.wav"`        | Left-hand auditory stimulus             |
| `FONT_PATH`                      | `"fonts/Vazir.ttf"` | Path to font file                       |
| `FONT_SIZE`                      | `40`                | Font size for messages                  |
| `LANGUAGE`                       | `"fa"`              | Language for messages (`fa` or `en`)    |

Customizable messages are stored in the `messages` dictionary for both **Persian** and **English**.

---

## Data Output

* **Stimulus Data**: `data-<coordination>-<stimulus>.csv`
* **Timestamp Data**: `timestamp-<coordination>-<stimulus>.csv`

Each CSV contains:

* Coordination mode
* Stimulus type (Visual / Auditory)
* Stimulus repetition count
* Stimulus duration and delay
* Timestamp of keypresses (Left / Right Ctrl)
* Start / Stop markers

> **Important:** Use a separate folder for each participant to avoid overwriting previous data.

---

## Tutorials

* Persian Tutorial PDF: [./docs/README.pdf](./docs/README.pdf)

---

## License

This project is for **research purposes** and is currently **unpublished**. Please contact the author for collaboration.

---

## References

* [Python Official Website](https://www.python.org/)
* Sound stimuli source:

  * [500 Hz tone](https://www.neurobs.com/ex_files/expt_view?id=72&tree_item_url=500.wav.lnk&item_id=500.wav.lnk)
  * [4000 Hz tone](https://www.neurobs.com/ex_files/expt_view?id=72&tree_item_url=4000.wav.lnk&item_id=4000.wav.lnk)
* Based on custom experimental protocols for multisensory coordination tasks.



## 👤 Author

**Mohammad Alaei**
AI Researcher & Computer Engineer 
🔗 [https://alaeimo.ir](https://alaeimo.ir) 