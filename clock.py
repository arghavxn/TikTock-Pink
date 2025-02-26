import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime
import time

# Set up the plot with a different figure size and background color
fig, ax = plt.subplots(figsize=(8, 8), facecolor='#FFE6EA')  # Pastel pink background
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis("off")  # Hide axes
ax.set_facecolor('#FFE6EA')  # Pastel pink background

# Draw the clock face with pastel pink theme
circle_outer = plt.Circle((0, 0), 1.05, color='#FF9AAD', fill=True, lw=0)  # Darker pink outer edge
circle = plt.Circle((0, 0), 1, color='#FFF0F3', fill=True, lw=2,
                    ec='#FFAEC0')  # Light pink face with medium pink border
circle_inner = plt.Circle((0, 0), 0.05, color='#FF9AAD', fill=True, lw=0)  # Pink center dot
ax.add_artist(circle_outer)
ax.add_artist(circle)
ax.add_artist(circle_inner)

# Add numbers to the clock face with a more elegant font
for number in range(1, 13):
    angle = np.pi / 2 - 2 * np.pi * (number / 12)  # Angle for each number
    x = 0.75 * np.cos(angle)  # Position inside the circle
    y = 0.75 * np.sin(angle)
    ax.text(x, y, str(number), color='#FF6F8B', fontsize=20, ha='center', va='center',
            fontweight='bold', fontfamily='serif')  # Pink-colored numbers

# Add minute ticks with improved styling
for tick in range(60):
    angle = np.pi / 2 - 2 * np.pi * (tick / 60)

    # Different styles for hour, minute, and second ticks
    if tick % 15 == 0:  # Hour markers at 3, 6, 9, 12
        inner_r = 0.85
        outer_r = 1
        lw = 3
        color = '#FF6F8B'  # Darker pink for hour markers
    elif tick % 5 == 0:  # Every 5 minutes
        inner_r = 0.9
        outer_r = 1
        lw = 2
        color = '#FF8DA1'  # Medium pink for 5-minute markers
    else:  # Regular minute ticks
        inner_r = 0.95
        outer_r = 1
        lw = 1
        color = '#FFAEC0'  # Light pink for minute ticks

    ax.plot([inner_r * np.cos(angle), outer_r * np.cos(angle)],
            [inner_r * np.sin(angle), outer_r * np.sin(angle)],
            color=color, lw=lw)

# Create clock hands with cute pastel pink styling
hour_hand, = ax.plot([0, 0], [0, 0], color='#FF6F8B', lw=8, solid_capstyle='round')  # Darker pink hour hand
minute_hand, = ax.plot([0, 0], [0, 0], color='#FF8DA1', lw=5, solid_capstyle='round')  # Medium pink minute hand
second_hand, = ax.plot([0, 0], [0, 0], color='#FF4D6D', lw=2, solid_capstyle='round')  # Bright pink second hand


# Function to initialize the animation
def init():
    hour_hand.set_data([0, 0], [0, 0])
    minute_hand.set_data([0, 0], [0, 0])
    second_hand.set_data([0, 0], [0, 0])
    return hour_hand, minute_hand, second_hand


# Function to update the hands for each frame using computer's local time
def update(frame):
    # Get current local time
    now = datetime.datetime.now()
    hours, minutes, seconds = now.hour, now.minute, now.second
    milliseconds = now.microsecond / 1000000  # For smoother second hand movement

    # Convert to 12-hour format for the clock
    hours = hours % 12

    # Calculate angles for each hand with smoother movement
    second_angle = np.pi / 2 - 2 * np.pi * ((seconds + milliseconds) / 60)
    minute_angle = np.pi / 2 - 2 * np.pi * ((minutes + seconds / 60) / 60)
    hour_angle = np.pi / 2 - 2 * np.pi * ((hours + minutes / 60) / 12)

    # Update hand positions - ensure they start from origin
    second_hand.set_data([0, 0.9 * np.cos(second_angle)], [0, 0.9 * np.sin(second_angle)])
    minute_hand.set_data([0, 0.75 * np.cos(minute_angle)], [0, 0.75 * np.sin(minute_angle)])
    hour_hand.set_data([0, 0.5 * np.cos(hour_angle)], [0, 0.5 * np.sin(hour_angle)])

    return hour_hand, minute_hand, second_hand


# Force initial update to ensure hands are drawn immediately
init_time = datetime.datetime.now()
hours = init_time.hour % 12
minutes = init_time.minute
seconds = init_time.second

# Pre-calculate initial positions so hands appear immediately
second_angle = np.pi / 2 - 2 * np.pi * (seconds / 60)
minute_angle = np.pi / 2 - 2 * np.pi * ((minutes + seconds / 60) / 60)
hour_angle = np.pi / 2 - 2 * np.pi * ((hours + minutes / 60) / 12)

# Set initial positions explicitly
second_hand.set_data([0, 0.9 * np.cos(second_angle)], [0, 0.9 * np.sin(second_angle)])
minute_hand.set_data([0, 0.75 * np.cos(minute_angle)], [0, 0.75 * np.sin(minute_angle)])
hour_hand.set_data([0, 0.5 * np.cos(hour_angle)], [0, 0.5 * np.sin(hour_angle)])

# Create the animation with real-time updates
ani = FuncAnimation(fig, update, init_func=init, interval=40, blit=True)

# Add a title
plt.suptitle('Real-Time Analog Clock', y=0.95, fontsize=22, fontweight='bold', fontfamily='serif', color='#FF6F8B')

plt.tight_layout()
plt.show()