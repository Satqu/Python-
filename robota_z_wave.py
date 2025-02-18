import wave
import numpy as np
import matplotlib.pyplot as plt

with wave.open('Nikow.wav', 'rb') as wav_file:
    print("Кількість каналів: ", wav_file.getnchannels())
    print("Частота дискретизації: ", wav_file.getframerate())
    print("Кількість фреймів: ", wav_file.getnframes())
    print("Бітрейт: ", wav_file.getsampwidth() * 8)

with wave.open('Nikow.wav', 'rb') as wav_file:
    frames = wav_file.readframes(100)
    print("Перші 100 фреймів: ", frames)

with wave.open('Nikow.wav', 'rb') as wav_file:
    frames = wav_file.readframes(-1)
    signal = np.frombuffer(frames, dtype=np.int16)
    print("Амплітуди: ", signal[:100])

plt.plot(signal[:1000])
plt.title("Аудіохвиля")
plt.xlabel("Фрейми")
plt.ylabel("Амплітуда")
plt.show()