import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

def generate_wav_file(frequency, volume, duration, filename):
    # Parámetros generales
    sample_rate = 44100  # Tasa de muestreo
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # Tiempo

    # Generar señal sinusoidal
    audio_data = volume * np.sin(2 * np.pi * frequency * t)

    # Asegurar que los datos estén dentro de un rango apropiado para WAV
    audio_data = np.int16(audio_data * 32767)

    # Guardar el archivo como .wav
    write(filename, sample_rate, audio_data)

    # Reproducir el sonido generado (opcional)
    sd.play(audio_data, sample_rate)
    sd.wait()  # Esperar hasta que termine de reproducirse

# Ejemplo de uso
frequency = 440  # Frecuencia en Hz (A4)
volume = 0.5     # Volumen (0.0 a 1.0)
duration = 2.0   # Duración en segundos
filename = "output.wav"  # Nombre del archivo de salida
frecuenccia=[i for i in range(8000,21000,1000)]
for i in frecuenccia:
    generate_wav_file(i, 1, 10, f"{i}.wav")
print(f"Archivo {filename} generado exitosamente.")
