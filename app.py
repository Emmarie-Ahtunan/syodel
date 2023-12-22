import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Streamlit app content
st.title("Sine Wave Animation")

# Slider widgets for user input
start = st.slider("Start", min_value=0.0, max_value=float(400), step=10.0)
stop = st.slider("Stop", min_value=0.0, max_value=float(400), step=10.0)
step = st.slider("Step", min_value=0.25, max_value=1.0, step=0.01)
pixel_size = st.slider("Pixel Size", min_value=1, max_value=4, step=1)

# Create a figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], 'o', markersize=pixel_size)

# Animation initialization function
def init():
    line.set_data([], [])
    return (line,)

# Set the axis limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)

# Main animation function
def animate(frame):
    i = start + frame * step
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x + i)
    line.set_data(x, y)
    return (line,)

# Calculate the number of frames as an integer
num_frames = max(int((stop - start) / step), 1)

# Collect frames in a list
frames = []
for frame in range(num_frames):
    animate(frame)
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8)
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (4,))[:, :, :3]
    frames.append(image)

# Display the animation frames in Streamlit
for frame in frames:
    st.image(frame)

# Start the Streamlit app
if __name__ == "__main__":
    st.write("Adjust sliders to control animation speed and pixel size.")