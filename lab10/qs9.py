def get_wave_type(wavelength):
    if wavelength < 1e-11:
        return("a Gamma wave")
    elif 1e-11 <= wavelength < 1e-8:
        return("an X-Ray wave")
    elif 1e-8 <= wavelength < 3.8e-7:
        return("an Ultraviolet wave")
    elif 3.8e-7 <= wavelength < 7.5e-7:
        return("a Visible wave")
    elif 7.5e-7 <= wavelength < 1e-3:
        return("an Infrared wave")
    elif 1e-3 <= wavelength < 1:
        return("a Microwave wave")
    else:
        return("a Radio wave")