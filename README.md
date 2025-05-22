# sEKV-Design-in-IHP-SG13G2

This repository presents some examples of analog circuit design using the EKV design methodology with the inversion coefficient. The examples are designed for the [open source IHP SG13G2 130nm BiCMOS technology](https://github.com/IHP-GmbH/IHP-Open-PDK).

The sEKV parameters are extracted for nMOS and pMOS separately using the extraction Jupyter Notebooks you find in the [sEKV Parameter Extraction directory](/sEKV%20Parameter%20Extraction/). The pdf outputs are available for [nMOS](/sEKV%20Parameter%20Extraction/sEKV_IHP130nm_nmos.pdf) and [pMOS](/sEKV%20Parameter%20Extraction/sEKV_IHP130nm_pmos.pdf). The Jupyter Notebooks generate an Excel file for nMOS and pMOS.

The sEKV design methodology is illustrated with several simple examples you can find in the [Circuit Examples directory](/Circuit%20Examples/). It currently includes:
* [Common-source gain stage optimization](/Circuit%20Examples/CS%20Optimization/) for minimum current consumption.
* [Cascode Gain Stage with Bias](/Circuit%20Examples/Cascode%20Gain%20Stage%20with%20Bias/).
* [Five transistors simple OTA](/Circuit%20Examples/Simple%20OTA/).
* [Symmetrical Cascode OTA](/Circuit%20Examples/Symmetrical%20OTA/).
* [Miller OTA](/Circuit%20Examples/Miller%20OTA/).
* [Telescopic OTA](/Circuit%20Examples/Telescopic%20OTA/).
* [Folded cascode OTA](/Circuit%20Examples/Folded%20Cascode%20OTA/).

The theoretical predictions are validated using ngspice and the models provided by the IHP PDK for the PSP compact model. In order to run the example in the Jupyter or Quarto Notebooks you need to install ngspice according to the instruction given in the [ngspice installation file](ngspice_installation.md).
