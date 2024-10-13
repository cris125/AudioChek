import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

def generate_stereo_wav_file(frequency, volume, duration, filename):
    # Parámetros generales
    sample_rate = 44100  # Tasa de muestreo
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # Tiempo

    # Generar la misma señal sinusoidal para ambos canales
    audio_data = volume * np.sin(2 * np.pi * frequency * t)

    # Crear un array estéreo duplicando la misma señal para ambos canales
    audio_stereo = np.column_stack((audio_data, audio_data))

    # Asegurar que los datos estén dentro de un rango apropiado para WAV
    audio_stereo = np.int16(audio_stereo * 32767)

    # Guardar el archivo como .wav estéreo
    write(filename, sample_rate, audio_stereo)

    # Reproducir el sonido generado (opcional)
     # Esperar hasta que termine de reproducirse

# Ejemplo de uso
for i in [8000,10000,12000,15000,16000,17000,19000,20000]:
    generate_stereo_wav_file(i, 1, 10, f'{i}.wav')



