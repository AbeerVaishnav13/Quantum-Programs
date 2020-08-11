def bob_measure_qubit(bob_bases, qubit_index, qubit_circuit):
    ## WRITE YOUR CODE HERE
    if bob_bases[qubit_index] == '1':
        qubit_circuit.h(0)
        
    qubit_circuit.measure([0], [0])
    ## WRITE YOUR CODE HERE