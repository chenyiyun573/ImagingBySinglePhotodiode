import numpy as np
import matplotlib.pyplot as plt

# imaging real pictures
H = np.eye(30*40)
H_alt = np.random.permutation(H)

np.save('H.npy', H)
np.save('H_alt.npy', H_alt)

#######
# Then:Step2:
# in terminal run: python capture_image.py --mask H.npy --out sensor_readingsH
# or run: python capture_image.py --mask H_alt.npy --out sensor_readingsH

# Sensor readings
def reconstruct():
    sr = np.load('sensor_readingsH_100_0.npy')
    H = np.load('H.npy')
    # H_alt = np.load('H_alt.npy')
    iv = np.dot(np.linalg.inv(H),sr)
    # iv = np.dot(np.linalg.inv(H_alt), sr)
    img = np.reshape(iv, (30, 40))
    plt.figure(figsize = (8, 8))
    plt.imshow(img, cmap = 'gray', interpolation="nearest")
    plt.show()

reconstruct()