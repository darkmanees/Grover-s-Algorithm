# Grover-s-Algorithm

A mini project on implementation of Grover's Algorithm to search a particular number in a diary containing 4 numbers.

Problem Statement:
Consider an unstructured phone book with 4 pages. Each of the pages, 1 through4, contains a phone number of different person. Let x={1,2,3,4}be the page numbers and x= 2 mark the phone number of your mom. (This means your mom’s phone number is located in page 2.)

1.Classical Approach:
Classically, on average, you create af or loop on python, for example, and go through the phone book pages one by one before finding your mon’s phone number. How many trials do you need on average classicaly? How many trials do you need in the worst case?

On average we have to do N/2 trials while the worst-case scenario is N trials.

2. Quantum Approach:
   There exist a quantum algorithm that provides quadratic speedup (N^1/2) in searching over databases. We can use this algorithm for the above problem. You can learn more about Grover's Algorithm here.(https://learning.quantum-computing.ibm.com/course/fundamentals-of-quantum-algorithms/grovers-algorithm)

For this problem, four pages number is encoded in quantum register {|00〉,|01〉,|10〉,|11〉}.
a. Since, the target phone number is in page 2, the target state will be represented by state |01〉.
b. Superposition of these 4 states with equal amplitudes is raised|+〉=1√2^2(|00〉+|01〉+|10〉+|11〉). (N raised to the power of 2 in the amplitude for the number of qubits )
