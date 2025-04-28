# sEKV-Design-in-IHP-SG13G2

Examples of  analog circuit design with sEKV for the [open source IHP 130nm technology](https://github.com/IHP-GmbH/IHP-Open-PDK).

The sEKV parameters are extracted for nMOS and pMOS separately using the extraction Jupyter Notebooks you find in the [sEKV Parameter Extraction directory](/sEKV Parameter Extraction/)


[PSP Verilog-A directory](/PSP/Verilog-A/) 
The examples are ran in either Jupyter (.pynb) or quarto  Notebooks (.qmd). I edit and run them in Visual Studio Code (VS Code) after having intalled the appropriate Juypter and Quarto extensions.
The simulations are performed by ngspice (version 43) using the [PSP 103.6 MOSFET compact model](https://www.cea.fr/cea-tech/leti/pspsupport). In order to run the simulation from the Juypter or Quarto Notebooks, you need to install things properly as described below.
