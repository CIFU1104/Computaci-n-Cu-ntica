import matplotlib
matplotlib.use("Agg")  # backend sin interfaz gráfica
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

# ---------------------------
# 1. Crear el circuito
# ---------------------------
qc = QuantumCircuit(3, 3)

# Aplicar Hadamard a cada qubit
for qubit in range(3):
    qc.h(qubit)

# Obtener el statevector
stv = Statevector.from_instruction(qc)

# Medir cada qubit en su bit clásico correspondiente
for qubit in range(3):
    qc.measure(qubit, qubit)

# ---------------------------
# 2. Dibujar el circuito
# ---------------------------
fig_circuit = qc.draw("mpl")
fig_circuit.savefig("circuit.png", bbox_inches="tight")
plt.close(fig_circuit)

# ---------------------------
# 3. Dibujar el statevector
#    (versión mpl en vez de latex)
# ---------------------------
ax_state = stv.draw("mpl")
fig_state = ax_state.figure
fig_state.savefig("statevector.png", bbox_inches="tight")
plt.close(fig_state)

# ---------------------------
# 4. Simulación en qasm_simulator
# ---------------------------
backend = Aer.get_backend("qasm_simulator")
job = backend.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print("Resultados de las mediciones (counts):")
print(counts)

# ---------------------------
# 5. Histograma de resultados
# ---------------------------
fig_hist = plot_histogram(counts)
fig_hist.savefig("histogram.png", bbox_inches="tight")
plt.close(fig_hist)

print("Gráficas guardadas como circuit.png, statevector.png y histogram.png")
