import numpy as np
import matplotlib.pyplot as plt
# define 2 vectors
v1=np.array([3,2])
v2=np.array([1,4])
#basic vector operation 
print("V1:",v1)
print("V2:",v2)
print("V1+V2 =",v1+v2)  #vector addition
print("V1 dot V2 =", np.dot(v1, v2)) #dot product
print("|v1 (magnitude)=", np.linalg.norm(v1)) #lehght of v1

#  matric multiplication 
A  = np.array([[2,0],
               [1,3]])

B  = np.array([[1,3],
               [2,4]])
print("\nA * B =\n", A @ B) # @ is the matrix mutlipacation operator in .py
# plot the vecotrs 
fig, ax = plt.subplots(figsize=(6,6))
origin = np.array([0, 0])

#draw v1 in blue
ax.annotate("",xy=v1 ,xytext=origin,
            arrowprops=dict(arrowstyle="->",color="blue", lw=2))
ax.text(v1[0]+0.1,v1[1]+0.1, "v1=(3,2)", color="blue", fontsize=12)
#draw v2 in red 
ax.annotate("",xy=v2 ,xytext=origin,
            arrowprops=dict(arrowstyle="->",color="red",lw=2))
ax.text(v2[0]+.01,v2[1]+0.1, "v2=(1,4)", color="red",fontsize=12)
# Draw v1+v2 in green
ax.annotate("", xy=v1+v2, xytext=origin,
            arrowprops=dict(arrowstyle="->", color="green", lw=2))
ax.text((v1+v2)[0]+0.1, (v1+v2)[1]+0.1, "v1+v2=(4,6)", color="green", fontsize=12)


ax.set_xlim(-1,6)
ax.set_ylim(-1,7)
ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)
ax.grid(True ,alpha=0.3)
ax.set_title("Day 1 - vectors in 2D",fontsize=14)
plt.tight_layout()
plt.savefig("DAY-1_vectors.png")
plt.show
print("\nplot saved as DAY-1_vectors.png")