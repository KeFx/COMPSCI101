wave_name = ["Radio", "Microwave", "Infrared",  "Visible",     "Ultraviolet", "X-Ray",  "Gamma"]
wavelength = [1,      10**(-3),    7.5*10**(-7), 3.8*10**(-7), 10**(-8),      10**(-11), 0]

look_up_table = dict(zip(wave_name, wavelength))
print(look_up_table)

{
    # Wave : wavelength(in meters)
    'Radio': 1, 
    'Microwave': 0.001, 
    'Infrared': 7.5e-07, 
    'Visible': 3.7999999999999996e-07, 
    'Ultraviolet': 1e-08, 
    'X-Ray': 1e-11, 
    'Gamma': 0
}

def determine_article(word) :
    if word[0] in "aeiouxAEIOUX" :
        return "an"
    else:
        return "a"

input_wavelength = float(input("Enter the wavelength: "))

for wave in look_up_table:
    if input_wavelength >= look_up_table[wave] :
        print(f"A wavelength of {input_wavelength} m corresponds to {determine_article(wave)} {wave} wave.")
        break