import numpy as np
import matplotlib.pyplot as plt
import helpers

randomH = helpers.generateRandomBinaryMask(avg1sPerRow = 300, plot=False)
hadamardH = helpers.createHadamardMatrix(shape=randomH.shape, plot=False)

helpers.packageMaskMatrix(randomH, 'randomH')
helpers.packageMaskMatrix(hadamardH,'hadamardH')
brightness = 90

def idealReconstruction(H, matrixName, s, X=32, Y=32, realImaging=False):
    i = np.dot(np.linalg.inv(H),s)
    if realImaging:
        i = helpers.noiseMassage(i, H)

    i2D = i.reshape((32,32))
    plt.imshow(i2D[1:,1:], cmap="gray", interpolation="nearest")
    plt.title("Reconstructed Image, Using %s" % matrixName)
    plt.show()
# Run scan
# run1: python capture_image.py --mask randomH_packaged.npy --out sensor_readingsrandomH --width 32 --height 32 --brightness 90

def reconstruct_randomH():
    sr = np.load('sensor_readingsrandomH_%s_0.npy' % str(brightness))
    oest_randomH, s_randomH = helpers.getOffsetEstimateAndS(sWithOffsetCalibration = sr)  # Estimate the offset
    randomH = np.load('randomH.npy')
    idealReconstruction(H = randomH, matrixName = 'randomH', s = s_randomH - oest_randomH)

# or run2: python capture_image.py --mask hadamardH_packaged.npy --out sensor_readingshadamardH --width 32 --height 32 --brightness $brightness
def reconstruct_hadamardH():
    sr = np.load('sensor_readingshadamardH_%s_0.npy' % str(brightness))
    oest_hadamardH, sRow0Split = helpers.getOffsetEstimateAndS(sWithOffsetCalibration = sr)  # Estimate the offset
    s_hadamardH = helpers.getHadamardS(sRow0Split)  # Combine rows 0a, 0b of `s`
    hadamardH = np.load('hadamardH.npy')
    idealReconstruction(H = hadamardH, matrixName = 'hadamardH', s = s_hadamardH - oest_hadamardH)

reconstruct_hadamardH()
