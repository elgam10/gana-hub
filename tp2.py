# 1- Créons un graphique 2D 
from sympy import *
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(6,4)) 
ax = plt.axes()
ax.set_title("Axes 2D vides") 
ax.set_xlabel("Axe X") 
ax.set_ylabel("Axe Y") 
ax.grid(True) 
plt.tight_layout() 
plt.show() 

# 2- Tracés de la courbe
x = [0, 1, 2, 3] 
y = [1, 2, 1.5, 3]
fig = plt.figure(figsize=(6,4)); ax = plt.axes()
ax.plot(x, y, linestyle="-", marker="o", label="Données (4 points)")
ax.set_title("Courbe simple à partir de listes Python")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.grid(True); ax.legend()
plt.tight_layout(); plt.show()

# 3- Traçons la fonction y=sin(x) sur [-3,3]
import numpy as np
x = np.linspace(-3, 3, 200) 
y = np.sin(x) 
fig = plt.figure(figsize=(6,4)); ax = plt.axes()
ax.plot(x, y, label="y = sin(x)")
ax.set_title("Courbe lisse obtenue avec NumPy")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.grid(True); ax.legend()
plt.tight_layout(); plt.show()

# 4-Traçons la fonction y=x²-2x+1 sur [-3,3]
import numpy as np
x = np.linspace(-3, 3, 200) 
y = x**2-2*x+1
fig = plt.figure(figsize=(6,4)); ax = plt.axes()
ax.plot(x, y, label="y = x²-2x+1")
ax.set_title('Courbe lisse obtenue avec NumPy')
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.grid(True); ax.legend()
plt.tight_layout(); plt.show()
# le minimum c'est lorsque x=1 ça donne y=0

# 5- Creons 4 sous graphiques y=x² ; y=sin(x); y=cos(x); et y=e^-x²
import numpy as np
x = np.linspace(-3, 3, 200)
plt.figure(figsize=(8, 6))

plt.subplot(2, 2, 1)
plt.plot(x, x**2)
plt.title("y = x²")
plt.grid(True)
plt.subplot(2, 2, 2)
plt.plot(x, np.sin(x))
plt.title("y = sin(x)")
plt.grid(True)
plt.subplot(2, 2, 3)
plt.plot(x, np.cos(x))
plt.title("y = cos(x)")
plt.grid(True)
plt.subplot(2, 2, 4)
plt.plot(x, np.exp(-x**2))
plt.title("y = e^(-x²)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 6-Représentez le nombre complexe z = 3+2i par un point et un vecteur depuis l’origine
z = 3 + 2j
fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect("equal") 
ax.plot(z.real, z.imag, "bo", markersize=8)  
ax.arrow(0, 0, z.real, z.imag, head_width=0.15, head_length=0.15 )
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_xlabel("Partie réelle")
ax.set_ylabel("Partie imaginaire")
ax.set_title("Nombre complexe z = 3 + 2j")
plt.grid(True)
plt.tight_layout()
plt.show()

# 7-Plaçons z = 3 + 2 i et son conjugué sur le même repère et montrez la symetrie
z=3+2j
z_conj=z.conjugate()
fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect("equal")
ax.axhline(y=0, color="black", linewidth=0.5)
ax.axvline(x=0, color="black", linewidth=0.5)
ax.grid(True, alpha=0.3)
ax.plot(z.real, z.imag, "ro", markersize=8, label="z = z")
ax.plot(z_conj.real, z_conj.imag, "bo", markersize=8, label="conjugue= z_conjugue")
ax.arrow(0, 0, z.real, z.imag, head_width=0.15, head_length=0.15, fc="red",ec="red")
ax.arrow(0, 0, z_conj.real, z_conj.imag, head_width=0.15,head_length=0.15, fc="blue", ec="blue")
ax.set_xlabel("Partie reelle")
ax.set_ylabel("Partie imaginaire")
ax.set_title("Nombre complexe et son conjugue")
ax.legend()
ax.set_xlim(-1, 4)
ax.set_ylim(-3, 3)
plt.tight_layout()
plt.show()

#8- Illustrez la somme de z1 = 2 + i et z2 = 1 + 2 i selon la règle du parallélogramme
z1 = 2 + 1j
z2 = 1 + 2j
z_sum = z1 + z2  
fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect("equal")
ax.arrow(0, 0, z1.real, z1.imag, head_width=0.1, fc="blue", ec="blue", length_includes_head=True)
ax.arrow(0, 0, z2.real, z2.imag, head_width=0.1, fc="red", ec="red", length_includes_head=True)
ax.arrow(z1.real, z1.imag, z2.real, z2.imag, linestyle="--", color="gray", length_includes_head=True)
ax.arrow(z2.real, z2.imag, z1.real, z1.imag, linestyle="--", color="gray", length_includes_head=True)
ax.arrow(0, 0, z_sum.real, z_sum.imag, head_width=0.1, fc="green", ec="green", length_includes_head=True)
ax.plot([z1.real], [z1.imag], "bo")
ax.plot([z2.real], [z2.imag], "ro")
ax.plot([z_sum.real], [z_sum.imag], "go")
ax.text(z1.real+0.1, z1.imag, "z1 = 2 + i", color="blue")
ax.text(z2.real+0.1, z2.imag, "z2 = 1 + 2i", color="red")
ax.text(z_sum.real+0.1, z_sum.imag, "z1 + z2", color="green")
ax.axhline(0, color="black")
ax.axvline(0, color="black")
ax.grid(True)
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_xlabel("Partie réelle")
ax.set_ylabel("Partie imaginaire")
ax.set_title("Somme de z1 et z2 (règle du parallélogramme)")
plt.tight_layout()
plt.show()

# 9- Créez une figure finale combinant : (1) une courbe 2D, (2) une figure complexe
import numpy as np
import matplotlib.pyplot as plt

# --- Création de la figure finale avec 2 sous-graphes ---
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# =========================================================
# (1) Courbe 2D : y = sin(x) sur [-3, 3]
# =========================================================
x = np.linspace(-3, 3, 400)
y = np.sin(x)

axes[0].plot(x, y)
axes[0].set_title("Courbe 2D : y = sin(x)")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].grid(True)

# =========================================================
# (2) Figure complexe : représentation de z = 3 + 2i
# =========================================================
z = 3 + 2j
x_z = z.real
y_z = z.imag

# Axe réel et axe imaginaire
axes[1].axhline(0)
axes[1].axvline(0)

# Vecteur depuis l'origine vers z
axes[1].quiver(0, 0, x_z, y_z, angles='xy', scale_units='xy', scale=1)

# Point pour z
axes[1].scatter(x_z, y_z)
axes[1].text(x_z + 0.1, y_z, "z = 3 + 2i")

axes[1].set_title("Plan complexe : représentation de z")
axes[1].set_xlabel("Re(z)")
axes[1].set_ylabel("Im(z)")
axes[1].set_aspect("equal", adjustable="box")
axes[1].set_xlim(-1, 5)
axes[1].set_ylim(-1, 5)
axes[1].grid(True)

plt.tight_layout()
plt.show()
