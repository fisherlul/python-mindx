import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize = (6,6))
t = np.linspace(tmin,tmax,100) # 100 pts suffisent !
ax.plot(x(t),y(t),color='black')
lim = (-(R+1),R+1); ax.set_xlim(lim); ax.set_ylim(lim)
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.grid() # affiche une grille
plt.show()

fig, ax = plt.subplots(figsize = (6,6),
                       subplot_kw={"projection":"3d"})
t = np.linspace(tmin,tmax,200) # 200 pts suffisent !
ax.plot(x(t),y(t),z(t),color='black')
ax.set_xlabel("x");ax.set_ylabel("y");ax.set_zlabel("z")
lim = (-(R+1),R+1)
ax.set_xlim(lim); ax.set_ylim(lim); ax.set_zlim(lim)
plt.show()

# Calcul de la longueur d'une ligne polygonale
def long_ligne_poly(tmin,tmax,x,y,z,N):
    t = np.linspace(tmin,tmax,N) # sub. de [tmin,tmax] 
    longueur = 0 # Initialisation du calcul
    for i in range(N-1):
        # CoordonnÃ©es de 2 points consÃ©cutifs
        OM1 = np.array([x(?),y(?),z(?)])
        OM2 = np.array([x(?),y(?),z(?)])
        # Longueur du segment reliant ces 2 pts
        dl = np.linalg.norm(OM2-OM1)
        longueur = longueur + ?
    return longueur # longueur de la ligne polygonale

def vecteur_tangent_2D(ax,t0,x,y,dxdt,dydt):
    # ReprÃ©sentation du point M(t0)
    M = np.array([x(?),y(?)])
    ax.scatter(M[0],M[1],marker='o',color='blue')
    # Vecteur tangent Ã  la courbe en M(t0)
    T = np.array([dxdt(?),dydt(?)])
    # ReprÃ©sentation du vecteur tangent en M(t0)
    ax.quiver(M[0],M[1],T[0],T[1],
              angles='xy',scale_units='xy',scale=1,
              color='blue',width=0.01)

def vecteur_tangent_3D(ax,t0,x,y,z,dxdt,dydt,dzdt):
    # ReprÃ©sentation du point M(t0)
    M = np.array([x(?),y(?),z(?)])
    ax.scatter(M[0],M[1],M[2],marker='o',color='blue')
    # Vecteur tangent Ã  la courbe en M(t0)
    T = np.array([dxdt(?),dydt(?),dzdt(?)])
    # ReprÃ©sentation du vecteur tangent en M(t0)
    norme_T = np.linalg.norm(T)
    ax.quiver(M[0],M[1],M[2],T[0],T[1],T[2],
              color='blue',length=norme_T,
              pivot='tail',linewidth=3)