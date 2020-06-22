import librosa
import matplotlib.pyplot as plt
import librosa.display

filePath = 'C:\\Users\\linho\\Desktop\\VeServe\\speaker_diarization\\' + 'done.wav'
y, sr = librosa.load(filePath, sr = None)

mfcc = librosa.feature.mfcc(y=y, sr=sr)

plt.figure(figsize=(10, 4))
librosa.display.specshow(mfcc, x_axis= 'time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()