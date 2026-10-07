
def convertir(valor, tipo_conversion):

    valor_convertido = 0

    match tipo_conversion:
        case "km_a_millas":
            valor_convertido = valor * 0.621371
        case "millas_a_km":
            valor_convertido = valor * 1.60934
        case "c_a_f":
            valor_convertido = valor * (9/5) + 32
        case "f_a_c":
            valor_convertido = (valor - 32) / 1.8
        case _:
            return "Opcion invalida"


    return round(valor_convertido,2)


print(convertir(1500,"km_a_millas"))
print(convertir(0, "c_a_f"))


    



