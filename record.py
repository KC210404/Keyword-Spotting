import sounddevice as sd
import wave
import os
import random
import time

labels = ['right', 'no', 'up', 'left', 'go', 'stop', 'down', 'yes']
dictionary = {'right': 1, 'no': 2, 'up': 3, 'left': 4, 'go': 5, 'stop': 6, 'down': 7, 'yes': 8}
repeated_labels = labels * 30
random.shuffle(repeated_labels)

output_dir = 'recordings'
duration = 1  # seconds
sample_rate = 16000
no_labels = len(repeated_labels)

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

for i in range(no_labels):
    label = repeated_labels[i]
    print(f"{label}")
    time.sleep(1)
    print("recording")
    audio = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait() 

    sd.play(audio, samplerate=sample_rate)
    sd.wait()
    time.sleep(1)

    filename = os.path.join(output_dir, f"{i}.wav")
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio.tobytes())

    print(f"Saved recording for {label} to {filename}")

print("All recordings are complete.")

with open(os.path.join(output_dir,'labels.txt'), 'w') as lf:
    for label in repeated_labels:
        lf.write(f"{dictionary[label]}\n")

