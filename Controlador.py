import Modelo

def control(precio, tipo, famortiguador_delantero, famortiguador_trasero):
    """
    Función control, trabaja como intermediaria entre la vista y el modelo
    """
    x = Modelo.Model()
    bicicleta, ferror, fprecio, mensaje_error = x.configuracion(precio, tipo, famortiguador_delantero, famortiguador_trasero)

    if ferror:
        return f"Error: {mensaje_error}"

    if fprecio:
        return "Error: No se puede configurar una bicicleta con ese presupuesto."

    cad = ""
    cuadro = bicicleta.getCuadro()
    rueda = bicicleta.getRueda()
    piñon = bicicleta.getPiñon()
    plato = bicicleta.getPlato()
    amortiguador_delantero = bicicleta.getAmortiguadorDelantero()
    amortiguador_trasero = bicicleta.getAmortiguadorTrasero()
    freno = bicicleta.getFreno()

    cad = (f"Cuadro: {cuadro.modelo}   ---> {cuadro.precio} euros\n"
           f"Rueda: {rueda.modelo}   ---> {rueda.precio} euros\n"
           f"Piñon: {piñon.modelo}   ---> {piñon.precio} euros\n"
           f"Plato: {plato.modelo}   ---> {plato.precio} euros\n"
           f"Amortiguador Delantero: {amortiguador_delantero.modelo}   ---> {amortiguador_delantero.precio} euros\n"
           f"Amortiguador Trasero: {amortiguador_trasero.modelo}   ---> {amortiguador_trasero.precio} euros\n"
           f"Freno: {freno.modelo}   ---> {freno.precio} euros\n"
           f"___________________________________________________\n"
           f"Precio final: {bicicleta.GetPrecio()} euros")

    return cad
