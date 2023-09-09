import pygame
import numpy as np
import time

# Initialize Pygame mixer
pygame.mixer.init()

# Define the frequencies of musical notes (C4 to G4)
note_freqs = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88
}

# Define the notes and their durations for the melody
melody = [
    ('C4', 500),
    ('C4', 500),
    ('G4', 500),
    ('G4', 500),
    ('A4', 500),
    ('A4', 500),
    ('G4', 1000),
    ('F4', 500),
    ('F4', 500),
    ('E4', 500),
    ('E4', 500),
    ('D4', 500),
    ('D4', 500),
    ('C4', 1000)
]

# Function to generate a waveform for a given frequency and duration
def generate_waveform(frequency, duration_ms):
    sample_rate = 44100  # Standard audio sample rate (samples per second)
    duration_sec = duration_ms / 500.0
    t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), endpoint=False)
    waveform = 0.5 * 32767 * np.sin(2 * np.pi * frequency * t)
    return waveform.astype(np.int16)

# Play the melody
for note, duration in melody:
    frequency = note_freqs[note]
    waveform = generate_waveform(frequency, duration)
    sound = pygame.mixer.Sound(waveform.tobytes())
    sound.play()
    pygame.time.wait(duration)

# Pause briefly before exiting
time.sleep(1)

# Quit Pygame
pygame.quit()
