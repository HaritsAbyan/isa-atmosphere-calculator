import math
print("""
 == Standard Atmosphere Calculator ==""")

def main_calc (altitude, temperature):
    P_res = 101325
    T_kel = 288.15 
    R_gas = 287.05
    g = 9.80665
    P_eleven = 22632
    po = 1.225
    
    if altitude <= 11000:
        status ='Troposphere'
        final_temp = temperature - (0.0065 * altitude)
        final_pressure = P_res * (1 - 0.0065 * altitude/T_kel)**5.25588
    else:
        status ='Stratosphere'
        final_temp = temperature - 56.5
        mid_pressure = (-g *(altitude - 11000)/ (R_gas * 216.65))
        final_pressure = round(P_eleven * math.exp(mid_pressure))
    
    final_temp_K = round(final_temp + 273.15)
    h_pres = round(altitude * 3.28084, 2)
    Dense_alt = h_pres + (120 *(temperature - final_temp))
    Dense_alt_m = round(Dense_alt / 3281 * 1000, 2)

    air_density = round(final_pressure / (R_gas * final_temp_K), 5)
    relative_density = round(air_density / po, 6)
    sonic_speed = round(math.sqrt(1.4 * R_gas * final_temp_K),2)
    
    mu_0 = 1.716e-5 
    Suther = 110.4
    T_ref = 273.15

    viscosity = mu_0 * ((T_ref + Suther)/(final_temp_K + Suther)) * (final_temp_K/T_ref)**1.5

    return f"""
    === Flight Data Report ===    
    Plane is in {status}
    Calculated temperature: {final_temp} C 
    Calculated pressure   : {final_pressure} Pa
    Dense Altitude        : {Dense_alt} Feet or {Dense_alt_m} M
    Air Density           : {air_density} kg/m3
    Relative Density      : {relative_density} (SL ISA=1)
    Sonic Speed           : {sonic_speed} MS
    Viscosity             : {viscosity:.8f} Pa.s
    """
        
altitude = float(input('Please insert your current altitude (m): '))
temperature = float(input('Please insert your current temperature (C): '))

print(main_calc(altitude, temperature))
