from qiskit.quantum_info import Operator
from qiskit import QuantumCircuit
import numpy as np



# We define oracle

def phase_oracle(n,page_to_be_located,name='Oracle'):# n=no. of qubits
    qc=QuantumCircuit(n,name=name)   # Creates a Quantum Circuit with n qubits
    oracle_matrix=np.identity(2**n)  # Constructs identity matrix of dimension n x n.
    for i in page_to_be_located:    
        oracle_matrix[i,i]=-1        # Locate -1 to required point as such only desired bit is flipped
    qc.unitary(Operator(oracle_matrix),range(n))   # Converts our matrix into unitary operator
    return qc

# We define function of diffuser
def diffuser(n):
    qc=QuantumCircuit(n,name='Diffuser') # Constructs a circuit named 'Diffuser'
    qc.h(range(n))                       #applies Hadamard gates to input gate
    qc.append(phase_oracle(n,[0]),range(n))
    qc.h(range(n))
    return qc

# Bring back both Oracle and Diffuser to a single cicuit
def Grover(n,marked):   # n,marked = Input values to our function
    qc=QuantumCircuit(n,n)  # Constructs circuits
    print(f'{n} qubits, page_we_want_to_locate: {mark}')
    qc.h(range(n))                   # Applies Hadamard gates to obtain superpostion states of all states
    qc.append(phase_oracle(n,marked),range(n))   # adds phase oracle circuit on qc
    qc.append(diffuser(n),range(n))              # adds diffuser cicuit on qc  
    qc.measure(range(n),range(n))                # measures output and stores in Classical register
    return qc

# Now, we input to the Grover's function
n=2
mark=1
marked=[1]
qc=Grover(n,marked)


from qiskit import Aer, execute
simulator = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=simulator, shots=1000).result().get_counts(qc)
from qiskit.visualization import plot_histogram
plot_histogram(counts)