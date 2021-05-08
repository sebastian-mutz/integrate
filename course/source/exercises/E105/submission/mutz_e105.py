import numpy
import matplotlib.pyplot as plt
#
"""
Fixed Parameters
================

SB_SIGMA - Stefan-Boltzman constant in W/(m**2 K**4)
PI       - delicious old pi
"""
SB_SIGMA = 5.7E-8
PI = 3.141592653589793 


"""
Sun's Parameters
----------------
F_SOL - Temperature of the sun (K)
R_SOL - Radius of the sun (m)
"""
T_SOL = 5800
R_SOL = 6.96000E8


"""
Earth's Parameters
------------------
R - distance of Earth from sun (m)
"""
R = 1.5E11


"""
C_AT - heat capacity: atmosphere only
C_OS - heat capacity: ocean surface 50m (real ca. 70m) 
C_OU - heat capacity: upper ocean layer 250m (real ca. 360m)  
C_OD - heat capacity: ocean 3900m, 70% of Earth surface   

Note: Heat capacity is given in J/(K*m^2) to simplify calculations.

The specific heat capacity of air (Cp) is ~1000 J/(kg*K) or, given the density 
of air (ro) of 1 kg/m^3, the volumetric heat capacity Cv of ~1000 J/(K*m^3).
[ Cv=Cp*ro=1000 J/(K*m^3) ]. 

In ro*Cp*dT/dt=dQ/dx, Q is heat flow in W/m^2 or J/(s*m^2), which is given by 
f_net. To get dT, we need to divide heat flow by a unit of length. In this exercise,
volumetric heat capacity (c=ro*cp) is already multiplied by 10000 (m), i.e. the 
average thickness of the troposphere, and therefore skip the division of the heat  
flow by length.

Example:
C_AT= ro*Cp*H where H is the height of the troposphere (~10km).
"""
C_AT = 1.0E7 
C_OS = 2.0E8 
C_OU = 1.0E9 
C_OD = 1.6E10   


"""
ALBEDO_0  - albedo mean constant
TRANSM_0  - transmissivity mean constant
"""
ALBEDO_0 = 0.3 
TRANSM_0 = 0.64262


"""
Tasks for You!
==============

1) Calculate the sun's output F_SOL and radiative flux PHI_SOL
"""
F_SOL   = SB_SIGMA * T_SOL**4
PHI_SOL = F_SOL * 4 * PI * R_SOL**2
print("F_SOL:", F_SOL)
print("PHI_SOL:", PHI_SOL)


"""
2) Calculate F_SW_IN_0, the mean incoming shorwave radiation per area on Earth in W/m^2, i.e. the solar constant.
"""
E_0 = PHI_SOL / (4 * PI * R**2)  # solar constant
F_SW_IN_0 = E_0 / 4
print("E_0:", E_0)
print("F_SW_IN_0:", F_SW_IN_0)


"""
3) Calculate the predicted temperature on Earth T_EARTH assuming no atmosphere
"""
T_EARTH = ( ( E_0 * (1 - ALBEDO_0) ) / (4 * SB_SIGMA) )**(1/4)
print("T_EARTH:", T_EARTH)


"""
You'll notice that the temperature of task 3 deviates somewhat from the actual temperature on Earth. 
What we need is to consider greenhouse gas related transmissivity.


4) Let temperature evolve over time!
Initialise temperature and let it evolve over time until it reaches equilibrium. 
Make sure to include albedo and transmissivity in your calculations.

HINT: To calculate temperature change for a specific time step based on net incoming radiation,
remember dT (change in temperature) = dQ (change in heat/energy) / C (heat capacity), incoming 
radiation is measured in W/m^2 (J/(s*m^2)) and heat capacity is given in J/(K*m^2) here.

Note: When calculating the radiation emitted by Earth, a multiplication by the factor of 0.95 is
necessary to take into consideration the emissive propertiesof the Earth's surface.

4-a: Initialise temperature at 300K and let it evolve using a heat capacity of the atmosphere only.
4-b: Change the initial temperature, run your code again and see what happens. Does this make sense?
4-c: Pick a different heat capacity and see what happens. Does this make sense?
"""


# Simulation Parameters
i_dt  = 10                                # time step size in days
nt    = 50                                # number of time steps
dt    = 60*60*24*float(i_dt)              # time step size in SI units (s)
ck    = C_AT                              # selection of heat capacity 
#
# Initialisation
temp = [0.0]*nt                           # initialise temperature array
temp[0]=300                               # initial temperature
#
# run simulation
for i in range(0,nt-1):
    #
    # radiative fluxes
    f_sw_in  = F_SW_IN_0
    f_sw_out = ALBEDO_0 * f_sw_in
    f_lw_out = 0.95 * SB_SIGMA * temp[i]**4
    f_net    = f_sw_in - f_sw_out - f_lw_out * TRANSM_0
    #
    # temperature for next time step
    temp[i+1] = temp[i] + dt*(1/ck) * f_net
#    print(temp[i])    
#
# plotting everything
x = [0.0]*nt
y = temp
#
for i in range (1,nt):
    x[i] = x[i-1]+i_dt
#
# create plot
plt.figure(0)                          # number your figures
plt.plot(x, y)                         # create a simple x-y plot
plt.title('temperature evolution')     # set a title
plt.xlabel('days')                     # label the x axis
plt.ylabel('temperature (K)')          # label the y axis
#plt.axis([0, nt, 280, 300])            # give x and y bounds
plt.show()
