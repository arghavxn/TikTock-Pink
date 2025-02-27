# TikTock Pink - Real-Time Analog Clock 🕰️🎀

A customizable, real-time analog clock built with Python and Matplotlib.


## Overview

This project creates a realistic analog clock that displays the current local time with hour, minute, and second hands. The clock includes styling options and smooth animation for a visually appealing experience.

## Features

- Real-time display of current local time
- Smooth animation with 40ms update interval
- Customizable themes (including pastel pink)
- Realistic clock face with numbers and tick marks
- Hour, minute, and second hands with appropriate styling

## Requirements

- Python 3.x
- Required libraries:
  - numpy
  - matplotlib
  - datetime

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/analog-clock.git
cd analog-clock
```

2. Make sure you have the required dependencies:
```bash
pip install numpy matplotlib
```

## Usage

Run the script with Python:

```bash
python analog_clock.py
```

This will open a window displaying the analog clock. The clock will automatically display your computer's current local time.

## Customization

You can customize the clock's appearance by modifying the following parameters:

### Change the theme colors:
```python
# For a pastel pink theme
fig, ax = plt.subplots(figsize=(8, 8), facecolor='#FFE6EA')
ax.set_facecolor('#FFE6EA')
circle_outer = plt.Circle((0, 0), 1.05, color='#FF9AAD', fill=True, lw=0)
circle = plt.Circle((0, 0), 1, color='#FFF0F3', fill=True, lw=2, ec='#FFAEC0')
```

### Adjust the clock size:
```python
fig, ax = plt.subplots(figsize=(10, 10))  # Makes a larger clock
```

### Change the hand styling:
```python
hour_hand, = ax.plot([0, 0], [0, 0], color='#FF6F8B', lw=8, solid_capstyle='round')
minute_hand, = ax.plot([0, 0], [0, 0], color='#FF8DA1', lw=5, solid_capstyle='round')
second_hand, = ax.plot([0, 0], [0, 0], color='#FF4D6D', lw=2, solid_capstyle='round')
```

## How It Works

The analog clock uses several key components:

1. **Clock Face**: Created using matplotlib's Circle patches for the outer rim, main face, and center dot.

2. **Numbers and Ticks**: The hour numbers are placed around the clock face using trigonometry to calculate their positions. Tick marks are added for minutes, with special styling for hour and 5-minute marks.

3. **Hands**: Three Line2D objects represent the hour, minute, and second hands. Their positions are updated based on the current time.

4. **Animation**: The FuncAnimation class from matplotlib.animation is used to update the clock every 40ms, creating smooth movement.

5. **Time Calculation**: The datetime.datetime.now() function gets the current local time, which is converted to angles for the clock hands using trigonometry.

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by classic analog timepieces
- Built with [Matplotlib](https://matplotlib.org/) and [NumPy](https://numpy.org/)
- Developed as a Python animation exercise
