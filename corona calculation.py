Corona Calculation in Power Systems-II
Using Peek's Formula

import math

def calculate_air_density_factor(pressure, temperature):
"""
Calculate air density factor.

pressure    : Atmospheric pressure in cm of Hg
temperature : Temperature in degree Celsius
"""
delta = (3.92 * pressure) / (273 + temperature)
return delta


def calculate_disruptive_critical_voltage(m0, delta, radius, spacing):
"""
Calculate disruptive critical voltage using Peek's formula.

m0      : Surface irregularity factor
delta   : Air density factor
radius  : Conductor radius in cm
spacing : Conductor spacing in cm

Returns:
    Critical disruptive voltage in kV
"""
if radius <= 0 or spacing <= 0:
    raise ValueError("Radius and spacing must be positive.")

if spacing <= radius:
    raise ValueError("Spacing must be greater than conductor radius.")

voltage = 21.1 * m0 * delta * radius * math.log(spacing / radius)
return voltage


print("==============================================")
print(" CORONA CALCULATION - POWER SYSTEMS II")
print("==============================================")

try:
radius = float(input("Enter conductor radius (cm): "))
spacing = float(input("Enter conductor spacing (cm): "))
pressure = float(input("Enter atmospheric pressure (cm of Hg): "))
temperature = float(input("Enter temperature (°C): "))
m0 = float(input("Enter surface irregularity factor (m0): "))

if pressure <= 0:
    print("Atmospheric pressure must be positive.")

elif m0 <= 0:
    print("Surface irregularity factor must be positive.")

else:
    delta = calculate_air_density_factor(pressure, temperature)

    critical_voltage = calculate_disruptive_critical_voltage(
        m0, delta, radius, spacing
    )

    print("\n--------------- RESULTS ----------------")
    print(f"Air density factor       : {delta:.4f}")
    print(f"Disruptive critical voltage: {critical_voltage:.2f} kV")
    print("----------------------------------------")


except ValueError as error:
print(f"Error: {error}")
