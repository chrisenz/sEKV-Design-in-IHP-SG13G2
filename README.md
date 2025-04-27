# sEKV-Design-in-IHP-SG13G2
Examples of  analog circuit design with sEKV for the open source IHP 130nm technology

1) Introduction
The examples are ran in either Jupyter (.pynb) or quarto  Notebooks (.qmd). I edit and run them in Visual Studio Code (VS Code) after having intalled the appropriate Juypter and Quarto extensions.
The simulations are performed with ngspice (version 43). In order to run the simulation from the Juypter or Qûarto Notebooks, you need to install things properly.

2) ngspice installation
You can down load ngspice from the official ngspice site. It is a good idea to also download the user manual from the same site.

Install the  ngspice folder named Spice64 where you want. I created a NGSpice folder in the C:\Program Files\ folder and copied the Spice64 folder in it. So for my installation, the path to the ngspice binary is C:\Program Files\NGSpice\Spice64\bin\. Now you can choose any other installation location.
Then you need to add a few variables to the Windows Environment variables. In order to do this in Windows 10 or Windows 11, open Settings>Sytem>About. On the right panel click Advanced system settings. You will see this dialog box

![Edit system variables.](system_variables.png)



Once you have installed (copied) ngspice, you need to copy the PSP 103.6  osdi file that contains the EKV2.6 MOSFET model that is used for the simulation. Add it to the folder <your ngspice installation path>\Spice64\lib\ngspice\. There are already other default osdi for other models in the same directory.

You then need to modify the spinit file of ngspice that is in the follwoing folder <your ngspice installation path>\Spice64\share\ngspice\scripts\. You can replace it by the following spinit file. This file is run each time ngspice is started. It will load the ekv26.osdi file for running simulations with the EKV2.6 compact model. Note that the other osdi models have been disabled by adding the star at the beginning of the line. If you want to use of these models you just remove the start on the corresponding line.
