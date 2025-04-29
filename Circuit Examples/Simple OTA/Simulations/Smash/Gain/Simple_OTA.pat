* Simulation of the simple OTA designed with the corresponding Jupyter Notebook
* Check of the small-signal open-loop gain and noise
.LIB ekv018.mdl
.INCLUDE size_bias.par
.INCLUDE simulation.par

.OPTION DAT
.OP
.DC LIN VID.Value {Vidmin} {Vidmax} {dVid} compress=no compressCoeff=1 compressTolX=0 compressTolY=1u
.TRACE DC {Vout = V(out)} 
.MEASURE NAME=Voffset WAVEFORM=Vout ANALYSIS=DC EXTRACT=X ATY=0.9 CROSS=UP OCCUR=1
.MEASURE NAME=Vomax WAVEFORM=Vout ANALYSIS=DC EXTRACT=MAX
.MEASURE NAME=Vomin WAVEFORM=Vout ANALYSIS=DC EXTRACT=MIN
.MEASURE NAME=Vosw ANALYSIS=DC VALUE=Vomax-Vomin

.AC dec 41 10 100MEG op=no
.TRACE  AC     DB(V(out)) DB(V(2)) 
.TRACE  AC     P(V(out)) 
.MEASURE NAME=Adc WAVEFORM=VDB(out) ANALYSIS=AC EXTRACT=MAX
.MEASURE NAME=GBW WAVEFORM=VDB(out) ANALYSIS=AC EXTRACT=X ATY=0 CROSS=DOWN OCCUR=1
.MEASURE NAME=Phase WAVEFORM=P(V(out)) ANALYSIS=AC EXTRACT=Y ATX=GBW CROSS=DOWN OCCUR=1
.MEASURE NAME=PM ANALYSIS=AC VALUE=180+Phase
.MEASURE NAME=fp1 WAVEFORM=P(V(out)) ANALYSIS=AC EXTRACT=X ATY=-45 CROSS=DOWN OCCUR=1
.MEASURE NAME=fp2 WAVEFORM=P(V(out)) ANALYSIS=AC EXTRACT=X ATY=-135 CROSS=DOWN OCCUR=1
.MEASURE NAME=fp3 WAVEFORM=P(V(out)) ANALYSIS=AC EXTRACT=X ATY=-225 CROSS=DOWN OCCUR=1

.NOISE V(OUT) VID 41 10 100MEG op=no compress=no compressCoeff=1 compressTolX=0 compressTolY=1u
.TRACE  Noise  {SnindBv = 20 * log10(INOISE)} {SninthdBv = 20 * log10(ITHN)} {SninfldBv = 20 * log10(IFLN)}
.TRACE  Noise  {SnintotdBv = 20 * log10(INOISE)} {SninM1dBv = 20 * log10(sqrt(IN(M1a.INOISE)^2 + IN(M1b.INOISE)^2))} {SninM2dBv = 20 * log10(sqrt(IN(M2a.INOISE)^2 + IN(M2b.INOISE)^2))}
.TRACE  Noise  {SninthtotdBv = 20 * log10(ITHN)} {SninthM1dBv = 20 * log10(sqrt(IN(M1a.ITHN)^2 + IN(M1b.ITHN)^2))} {SninthM2dBv = 20 * log10(sqrt(IN(M2a.ITHN)^2 + IN(M2b.ITHN)^2))}
.TRACE  Noise  {SninfltotdBv = 20 * log10(IFLN)} {SninflM1dBv = 20 * log10(sqrt(IN(M1a.IFLN)^2 + IN(M1b.IFLN)^2))} {SninflM2dBv = 20 * log10(sqrt(IN(M2a.IFLN)^2 + IN(M2b.IFLN)^2))}
.MEASURE NAME=fk WAVEFORM=SninfldBv ANALYSIS=NOISE EXTRACT=X ATY=-144.16 CROSS=DOWN OCCUR=1
