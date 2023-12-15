import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_pdf import PdfPages
from PyPDF2 import PdfMerger

# Creazione del grafico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
z = [1, 2, 3, 4, 5]

ax.scatter(x, y, z)

ax.set_xlabel('Asse X')
ax.set_ylabel('Asse Y')
ax.set_zlabel('Asse Z')

# Creazione del grafico con la sinusoide
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)

ax2.plot(x, y)
ax2.set_xlabel('Asse X')
ax2.set_ylabel('Sinusoide')

# Creazione del documento PDF
pdf = PdfPages('documento.pdf')

pdf.savefig(fig)  # Aggiungi il grafico 3D al documento PDF
pdf.savefig(fig2)  # Aggiungi il grafico con la sinusoide al documento PDF

pdf.close()

# Unisci i documenti PDF
merger = PdfMerger()
merger.append('documento.pdf')
merger.write('documento_finale.pdf')
merger.close()