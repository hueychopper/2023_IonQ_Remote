import cirq
import qiskit
import numpy as np


def encode_qiskit(image,cIndex):
    qc = qiskit.QuantumCircuit(3)
    for i in range(len(image)):
        t = np.unique(image[i], return_index=True)
        # print(t)
        if labels[cIndex] == False:
            qc.x(0)
    return qc


def decode(hist):
    for key in hist.keys():
        if hist[key][0] == 1.0:
            print(True)
        else:
            print(False)