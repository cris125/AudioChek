import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

def generate_wav_file(frequency, volume, duration, filename):
    sample_rate = 44100  # Tasa de muestreo
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Generar señal sinusoidal con volumen más alto
    audio_data = volume * np.sin(2 * np.pi * frequency * t)

    # Normalizar la señal para que ocupe el rango máximo sin distorsión
    audio_data = audio_data / np.max(np.abs(audio_data))

    # Convertir a rango de 16 bits
    audio_data = np.int16(audio_data * 32767)

    # Guardar el archivo como .wav
    write(filename, sample_rate, audio_data)

    # Reproducir el sonido generado


# Ejemplo de uso
frequency = 20000  # Frecuencia en Hz (20 kHz)
volume = 1.0       # Volumen máximo
duration = 2.0     # Duración en segundos
filename = "output_20000Hz.wav"

for i in [8000,10000,12000,15000,16000,17000,18000,190000,20000]:
    
    generate_wav_file(i, 1, 10, f"{i}.wav")

