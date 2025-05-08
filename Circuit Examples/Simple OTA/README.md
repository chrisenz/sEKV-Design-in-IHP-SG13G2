# Design of the Simple 5 Transistors OTA

This example presents the analysis, design and simulation of the simple 5 transistors OTA using the inversion coefficient approach and the sEKV model. The design is performed for the IHP SG13G2 BiCMOS process. We have chosen this process because IHP offers an open source PDK. The simulations are performed with the ngspice simulator with the PSP compact model and the parameters provided by the open source PDK.

The design and verification is performed in the [Quarto notebook](Simple_OTA.qmd). A design example is given in the [pdf file](Simple_OTA.pdf). An Excel file listing the size and all the variables (namely drain current, small-signal parameters, noise parameters and parasitic capacitances) of each transistor of the circuit.

In order to perfom a new design you need to set the variable newDesign to True and if you wnt to run the simulation you need to set the variable newSim to True.
