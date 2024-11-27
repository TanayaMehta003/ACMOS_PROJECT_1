import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('ids_w_v_gm_id.csv')

# Extract the channel lengths from the column names
channel_lengths = [45, 135, 180, 225, 270, 315, 360, 405, 450, 495, 540, 585, 630, 675, 720]  # in nm

# Select specific channel lengths to plot in increasing order
selected_lengths = [45, 180, 360, 540, 720]  # in nm

# Map the selected lengths to their corresponding indices
selected_indices = [channel_lengths.index(length) for length in selected_lengths]

# Plot the data
plt.figure(figsize=(14, 8))

for idx in selected_indices:
    gm_ids = df.iloc[:, idx * 2]
    gm_rout = df.iloc[:, idx * 2 + 1]
    plt.plot(gm_ids, gm_rout, label=f'l_nmos={channel_lengths[idx]} nm')

plt.xlabel('gm/id')
plt.ylabel('id/w')
plt.title('pid_w vs pgm_id')
plt.legend(title='Channel Lengths')
plt.grid(True)
plt.show()
