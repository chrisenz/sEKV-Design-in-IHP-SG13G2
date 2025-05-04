# Design of a Cascode Gain Stage with Bias

This examples shows how to design a simple cascode gain stage for specifications on the gain-bandwidth product and on the DC gain. It illustrates all the benefits of the cascode stage such as:
* A DC voltage gain equivalent to a two-stage circuit and
* A high output resistance 

without degradation of the noise. These features are achieved at the cost of voltage headroom. The driver transistor is biased in weak inversion for maximum current efficiency. The cascode transistor is also biased in weak inversion to minimize the the voltage headroom reduction. The design is performed for the IHP SG13G2 BiCMOS process with a particular attention to the biasing circuit. The results are presented in the [pdf report](/Circuit%20Examples/Cascode%20Gain%20Stage%20with%20Bias/Cascode_gain_stage.pdf).
