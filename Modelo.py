import BCbicicletas as BC

class Bicicleta:
    def __init__(self, lista_Base):
        self.cuadro = lista_Base[0]
        self.rueda = lista_Base[1]
        self.piñon = lista_Base[2]
        self.plato = lista_Base[3]
        self.amortiguador_delantero = lista_Base[4]
        self.amortiguador_trasero = lista_Base[5]
        self.freno = lista_Base[6]

    def getCuadro(self):
        return self.cuadro

    def getRueda(self):
        return self.rueda

    def getPiñon(self):
        return self.piñon

    def getPlato(self):
        return self.plato

    def getAmortiguadorDelantero(self):
        return self.amortiguador_delantero

    def getAmortiguadorTrasero(self):
        return self.amortiguador_trasero

    def getFreno(self):
        return self.freno

    def GetPrecio(self):
        precio = (self.cuadro.precio + self.rueda.precio + self.piñon.precio + 
                  self.plato.precio + self.amortiguador_delantero.precio + 
                  self.amortiguador_trasero.precio + self.freno.precio)
        return precio

    def setCuadro(self, cuadro):
        self.cuadro = cuadro

    def setRueda(self, rueda):
        self.rueda = rueda

    def setPiñon(self, piñon):
        self.piñon = piñon

    def setPlato(self, plato):
        self.plato = plato

    def setAmortiguadorDelantero(self, amortiguador_delantero):
        self.amortiguador_delantero = amortiguador_delantero

    def setAmortiguadorTrasero(self, amortiguador_trasero):
        self.amortiguador_trasero = amortiguador_trasero

    def setFreno(self, freno):
        self.freno = freno


class Model:
    def __init__(self):
        self.datos = []
        self.explica = []

    def getMTB(self, diseno, precio, famortiguador_delantero, famortiguador_trasero):
        cuadro_pct = 0.2 * precio
        rueda_pct = 0.2 * precio
        piñon_pct = 0.1 * precio
        plato_pct = 0.1 * precio
        freno_pct = 0.1 * precio

        amortiguador_delantero_pct = 0
        amortiguador_trasero_pct = 0

        if famortiguador_delantero:
            amortiguador_delantero_pct = 0.1 * precio
        if famortiguador_trasero:
            amortiguador_trasero_pct = 0.1 * precio

        total_amortiguadores_pct = amortiguador_delantero_pct + amortiguador_trasero_pct
        cuadro_pct -= total_amortiguadores_pct * 0.2
        rueda_pct -= total_amortiguadores_pct * 0.2
        piñon_pct -= total_amortiguadores_pct * 0.1
        plato_pct -= total_amortiguadores_pct * 0.1
        freno_pct -= total_amortiguadores_pct * 0.1

        for i in BC.cuadros():
            if i.precio <= cuadro_pct and i.tipo == "MTB":
                if famortiguador_trasero and not i.compatible_amortiguador_trasero:
                    continue
                diseno.setCuadro(i)

        for i in BC.ruedas():
            if i.precio <= rueda_pct and i.tipo == "MTB":
                diseno.setRueda(i)

        for i in BC.piñons():
            if i.precio <= piñon_pct:
                diseno.setPiñon(i)

        for i in BC.platos():
            if i.precio <= plato_pct:
                diseno.setPlato(i)

        if famortiguador_delantero:
            for i in BC.amortiguadores():
                if i.precio <= amortiguador_delantero_pct and i.tipo == "Delantero":
                    diseno.setAmortiguadorDelantero(i)

        if famortiguador_trasero:
            for i in BC.amortiguadores():
                if i.precio <= amortiguador_trasero_pct and i.tipo == "Trasero":
                    diseno.setAmortiguadorTrasero(i)

        for i in BC.frenos():
            if i.precio <= freno_pct:
                diseno.setFreno(i)

        return diseno

    def getRoad(self, diseno, precio):
        cuadro_pct = 0.3 * precio
        rueda_pct = 0.3 * precio
        piñon_pct = 0.15 * precio
        plato_pct = 0.15 * precio
        freno_pct = 0.1 * precio

        for i in BC.cuadros():
            if i.precio <= cuadro_pct and i.tipo == "Road":
                diseno.setCuadro(i)

        for i in BC.ruedas():
            if i.precio <= rueda_pct and i.tipo == "Road":
                diseno.setRueda(i)

        for i in BC.piñons():
            if i.precio <= piñon_pct:
                diseno.setPiñon(i)

        for i in BC.platos():
            if i.precio <= plato_pct:
                diseno.setPlato(i)

        for i in BC.frenos():
            if i.precio <= freno_pct:
                diseno.setFreno(i)

        return diseno

    def getPaseo(self, diseno, precio):
        cuadro_pct = 0.25 * precio
        rueda_pct = 0.25 * precio
        piñon_pct = 0.15 * precio
        plato_pct = 0.15 * precio
        freno_pct = 0.2 * precio

        for i in BC.cuadros():
            if i.precio <= cuadro_pct and i.tipo == "Paseo":
                diseno.setCuadro(i)

        for i in BC.ruedas():
            if i.precio <= rueda_pct and i.tipo == "Paseo":
                diseno.setRueda(i)

        for i in BC.piñons():
            if i.precio <= piñon_pct:
                diseno.setPiñon(i)

        for i in BC.platos():
            if i.precio <= plato_pct:
                diseno.setPlato(i)

        for i in BC.frenos():
            if i.precio <= freno_pct:
                diseno.setFreno(i)

        return diseno

    def Especificar(self, precio, tipo, famortiguador_delantero, famortiguador_trasero):
        if not precio:
            return None, True, True, "Por favor, introduce un presupuesto válido."

        if tipo == "MTB":
            lista_base = BC.mtb(famortiguador_delantero, famortiguador_trasero)
        elif tipo == "Road":
            lista_base = BC.road()
        elif tipo == "Paseo":
            lista_base = BC.paseo()
        else:
            return None, True, True, "Tipo de bicicleta no reconocido."

        bicicleta = Bicicleta(lista_base)
        ferror = False
        fprecio = False
        precio = int(precio)

        return bicicleta, ferror, fprecio, ""

    def Verificar(self, bicicleta, precio, tipo):
        fprecio = False
        ftipo = True
        fprecio_bajo = True
        fvalor = True

        if bicicleta.GetPrecio() > int(precio):
            fvalor = False
            fprecio = True
        if bicicleta.GetPrecio() < (int(precio) - 50):
            fvalor = False
            fprecio_bajo = False
        if bicicleta.getCuadro().tipo != bicicleta.getRueda().tipo:
            fvalor = False
            ftipo = False

        return fprecio, ftipo, fprecio_bajo, fvalor

    def cambiarComponente(self, diseno, precio, tipo, componente):
        componente_actual = getattr(diseno, f"get{componente}")()
        lista_componentes = getattr(BC, componente.lower() + "s")()
        numero = lista_componentes.index(componente_actual) + 1
        precio_diseno = diseno.GetPrecio()

        if componente_actual.modelo != lista_componentes[-1].modelo:
            for i in range(numero, len(lista_componentes)):
                nuevo_componente = lista_componentes[i]
                nuevo_precio = precio_diseno - componente_actual.precio + nuevo_componente.precio
                if nuevo_precio <= precio:
                    if componente == "Cuadro" or componente == "Rueda":
                        if nuevo_componente.tipo == tipo:
                            if componente == "Cuadro" and diseno.getAmortiguadorTrasero().precio > 0:
                                if not nuevo_componente.compatible_amortiguador_trasero:
                                    continue
                            getattr(diseno, f"set{componente}")(nuevo_componente)
                            break
                    else:
                        getattr(diseno, f"set{componente}")(nuevo_componente)
                        break

        return diseno

    def optimizarPrecio(self, diseno, precio, tipo):
        componentes = ["Piñon", "Plato", "Cuadro", "Rueda", "Freno"]
        for componente in componentes:
            while diseno.GetPrecio() < precio:
                precio_diseno_anterior = diseno.GetPrecio()
                diseno = self.cambiarComponente(diseno, precio, tipo, componente)
                if diseno.GetPrecio() == precio_diseno_anterior:
                    break
        return diseno

    def bajarPrecio(self, diseno, precio, tipo):
        for componente in ["Piñon", "Plato", "Cuadro", "Rueda", "Freno"]:
            diseno = self.cambiarComponente(diseno, precio, tipo, componente)
        return diseno

    def Criticar(self, fprecio, ftipo, fprecio_bajo, fvalor):
        Lista_acciones = []
        if fprecio:
            Lista_acciones.append(self.bajarPrecio)
        if fprecio_bajo == False:
            Lista_acciones.append(self.optimizarPrecio)
        if ftipo == False:
            Lista_acciones.append(self.cambiarComponente)

        return Lista_acciones

    def Seleccionar(self, Lista_acciones):
        if Lista_acciones:
            return Lista_acciones.pop()
        return None

    def Modificar(self, accion, diseno, precio, tipo):
        if accion:
            diseno = accion(diseno, precio, tipo)
        return diseno

    def Proponer(self, diseno, precio, tipo, famortiguador_delantero, famortiguador_trasero):
        if tipo == "MTB":
            lista_base = BC.mtb(famortiguador_delantero, famortiguador_trasero)
            diseno_nuevo = Bicicleta(lista_base)
            diseno_nuevo = self.getMTB(diseno, precio, famortiguador_delantero, famortiguador_trasero)
        elif tipo == "Road":
            lista_base = BC.road()
            diseno_nuevo = Bicicleta(lista_base)
            diseno_nuevo = self.getRoad(diseno, precio)
        elif tipo == "Paseo":
            lista_base = BC.paseo()
            diseno_nuevo = Bicicleta(lista_base)
            diseno_nuevo = self.getPaseo(diseno, precio)
        else:
            diseno_nuevo = diseno

        return diseno_nuevo

    def configuracion(self, precio, tipo, famortiguador_delantero, famortiguador_trasero):
        if not precio:
            return None, True, True, "Por favor, introduce un presupuesto válido."

        fprecio = False
        ftipo = True
        fprecio_bajo = True
        fvalor = True
        lista_acciones = []

        precio = int(precio)
        diseno_esquetal, ferror, fprecio, mensaje_error = self.Especificar(precio, tipo, famortiguador_delantero, famortiguador_trasero)
        if ferror:
            return diseno_esquetal, ferror, fprecio, mensaje_error

        diseno_final = self.Proponer(diseno_esquetal, precio, tipo, famortiguador_delantero, famortiguador_trasero)
        fprecio, ftipo, fprecio_bajo, fvalor = self.Verificar(diseno_final, precio, tipo)

        if not fvalor:
            lista_acciones = self.Criticar(fprecio, ftipo, fprecio_bajo, fvalor)
            while not fvalor and lista_acciones:
                accion = self.Seleccionar(lista_acciones)
                diseno_final = self.Modificar(accion, diseno_final, precio, tipo)
                fprecio, ftipo, fprecio_bajo, fvalor = self.Verificar(diseno_final, precio, tipo)

        if diseno_final.GetPrecio() > precio:
            return diseno_final, True, True, "El presupuesto es demasiado bajo para la configuración solicitada."

        if diseno_final.GetPrecio() < precio * 0.5:
            return diseno_final, True, True, "El presupuesto es demasiado alto para la configuración solicitada."

        return diseno_final, ferror, fprecio, ""
