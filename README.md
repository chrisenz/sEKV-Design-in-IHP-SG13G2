# sEKV-Design-in-IHP-SG13G2

Examples of  analog circuit design with sEKV for the [open source IHP 130nm technology](https://github.com/IHP-GmbH/IHP-Open-PDK).

The sEKV parameters are extracted for nMOS and pMOS separately using the extraction Jupyter Notebooks you find in the [sEKV Parameter Extraction directory](/sEKV%20Parameter%20Extraction/). The pdf outputs are available for [nMOS](/sEKV%20Parameter%20Extraction/sEKV_IHP130nm_nmos.pdf) and [pMOS](/sEKV%20Parameter%20Extraction/sEKV_IHP130nm_pmos.pdf). The Jupyter Notebooks generate an Excel file for nMOS and pMOS.

The sEKV design methodology is illustrated with several simple examples you can find in the [Circuit Examples directory](/Circuit%20Examples/).

The theoretical predictions are validated using ngspice and the models provided by the IHP PDK for the PSP compact model. In order to run the example in the Jupyter or Quarto Notebooks you need to install ngspice according to the instruction given in the [ngspice installation file](ngspice_installation.md).
