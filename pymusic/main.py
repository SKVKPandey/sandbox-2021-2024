import pygame
import numpy as np
import time

# Initialize Pygame mixer
pygame.mixer.init()

# Define the frequencies of the seven musical notes (C, D, E, F, G, A, B)
note_freqs = {
    'C': 261.63,  # Frequency for C (in Hz)
    'D': 293.66,  # Frequency for D (in Hz)
    'E': 329.63,  # Frequency for E (in Hz)
    'F': 349.23,  # Frequency for F (in Hz)
    'G': 392.00,  # Frequency for G (in Hz)
    'A': 440.00,  # Frequency for A (in Hz)
    'B': 493.88   # Frequency for B (in Hz)
}

# Function to generate a stereo waveform for a given frequency and duration
def generate_waveform(frequency, duration_ms):
    sample_rate = 44100  # Standard audio sample rate (samples per second)
    duration_sec = duration_ms / 1000.0
    t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), endpoint=False)
    left_waveform = 0.5 * 32767 * np.sin(2 * np.pi * frequency * t)
    right_waveform = 0.5 * 32767 * np.sin(2 * np.pi * frequency * t)
    stereo_waveform = np.column_stack((left_waveform, right_waveform))
    return stereo_waveform.astype(np.int16)

# Play each note for 1 second
for note in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
    waveform = generate_waveform(note_freqs[note], 1000)  # 1000 ms (1 second) duration
    sound = pygame.sndarray.make_sound(waveform)
    sound.play()
    pygame.time.wait(1000)  # Delay for 1 second

# Pause briefly before exiting
time.sleep(1)

# Quit Pygame
pygame.quit()
