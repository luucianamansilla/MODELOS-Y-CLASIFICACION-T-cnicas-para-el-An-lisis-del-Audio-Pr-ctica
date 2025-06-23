#%%
# Librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from IPython.display import Audio

audio_file_path = ""# RUTA

#%%
# Cargar audio y mostrar informacion (Punto 4)
audio, sr = sf.read(audio_file_path)

print("Vector de la senal (primeros 100 elementos):")
print(audio[:100])

print(f"Cantidad de elementos de la muestra: {len(audio)}")
print(f"Frecuencia de Muestreo: {sr} Hz")
print(f"Duracion del audio: {len(audio) / sr:.3f} segundos")

#%%
# Imprimir la senal sonora (Punto 5)
plt.figure(figsize=(14, 6))
plt.plot(audio)
plt.title('Senal Sonora')
plt.xlabel('Muestra')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()

#%%
# Reproducir senal original (Punto 6)
print("Reproduciendo: Senal original")
Audio(audio, rate=sr)

#%%
# Modificar frecuencia de muestreo (Punto 7)

print("Reproduciendo: Mas rapido")
Audio(audio, rate=sr * 2)

print("Reproduciendo: Mas lento")
Audio(audio, rate=sr * 0.5)

#%%
# Bajar calidad del audio (Punto 8)
print("Reproduciendo: Baja calidad de audio")

audio_baja_calidad = (audio * 127).astype(np.int8)
Audio(audio_baja_calidad, rate=sr)