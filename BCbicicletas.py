class Componente:
    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio

class Cuadro(Componente):
    def __init__(self, modelo, precio, tipo, compatible_amortiguador_trasero=False):
        super().__init__(modelo, precio)
        self.tipo = tipo
        self.compatible_amortiguador_trasero = compatible_amortiguador_trasero

class Rueda(Componente):
    def __init__(self, modelo, precio, tipo):
        super().__init__(modelo, precio)
        self.tipo = tipo

class Piñon(Componente):
    def __init__(self, modelo, precio, velocidad):
        super().__init__(modelo, precio)
        self.velocidad = velocidad

class Plato(Componente):
    def __init__(self, modelo, precio, dientes):
        super().__init__(modelo, precio)
        self.dientes = dientes

class Amortiguador(Componente):
    def __init__(self, modelo, precio, tipo):
        super().__init__(modelo, precio)
        self.tipo = tipo  # Delantero, Trasero

class Freno(Componente):
    def __init__(self, modelo, precio, tipo):
        super().__init__(modelo, precio)
        self.tipo = tipo  # Disco, V-brake

class Vacio(Componente):
    def __init__(self, modelo, precio):
        super().__init__(modelo, precio)

# Instancias

# Cuadros
Cuadro1 = Cuadro("Specialized Rockhopper", 200, "MTB")
Cuadro2 = Cuadro("Cannondale Synapse", 300, "Road")
Cuadro3 = Cuadro("Trek Marlin", 300, "MTB")
Cuadro4 = Cuadro("Giant Contend", 400, "Road")
Cuadro5 = Cuadro("Scott Aspect", 450, "MTB")
Cuadro6 = Cuadro("Santa Cruz Chameleon", 500, "MTB", compatible_amortiguador_trasero=True)
Cuadro7 = Cuadro("Cannondale CAAD13", 550, "Road")
Cuadro8 = Cuadro("Specialized Allez", 700, "Road")
Cuadro9 = Cuadro("Trek X-Caliber", 600, "MTB", compatible_amortiguador_trasero=True)
Cuadro10 = Cuadro("BMC Teammachine", 800, "Road")
Cuadro11 = Cuadro("Giant Anthem", 1000, "MTB", compatible_amortiguador_trasero=True)
Cuadro12 = Cuadro("Canyon Ultimate", 900, "Road")
Cuadro13 = Cuadro("Electra Cruiser", 200, "Paseo")
Cuadro14 = Cuadro("Schwinn Wayfarer", 300, "Paseo")
Cuadro15 = Cuadro("Gazelle EasyFlow", 400, "Paseo")
Cuadro16 = Cuadro("Linus Dutchi", 500, "Paseo")
Cuadro17 = Cuadro("Priority Classic", 600, "Paseo")
Cuadro18 = Cuadro("Raleigh Detour", 700, "Paseo")

# Ruedas
Rueda1 = Rueda("Maxxis Ardent", 80, "MTB")
Rueda2 = Rueda("Continental Grand Prix", 100, "Road")
Rueda3 = Rueda("Schwalbe Racing Ralph", 100, "MTB")
Rueda6 = Rueda("Vittoria Corsa", 140, "Road")
Rueda5 = Rueda("Kenda Nevegal", 120, "MTB")
Rueda4 = Rueda("Michelin Power", 150, "Road")
Rueda7 = Rueda("WTB Trail Boss", 180, "MTB")
Rueda8 = Rueda("Pirelli P Zero", 220, "Road")
Rueda9 = Rueda("Hutchinson Toro", 200, "MTB")
Rueda10 = Rueda("Zipp 303", 250, "Road")
Rueda11 = Rueda("Maxxis Minion DHF", 300, "MTB")
Rueda12 = Rueda("Mavic Ksyrium", 350, "Road")
Rueda13 = Rueda("Schwalbe Marathon", 80, "Paseo")
Rueda14 = Rueda("Continental Contact", 100, "Paseo")
Rueda15 = Rueda("Michelin Protek", 120, "Paseo")
Rueda16 = Rueda("Vittoria Randonneur", 130, "Paseo")
Rueda17 = Rueda("Kenda Kwest", 150, "Paseo")
Rueda18 = Rueda("Maxxis Overdrive", 170, "Paseo")

# Piñons
Piñon1 = Piñon("Shimano Altus 7 velocidades", 25, 7)
Piñon2 = Piñon("SRAM X4 7 velocidades", 30, 7)
Piñon3 = Piñon("Shimano Acera 8 velocidades", 30, 8)
Piñon4 = Piñon("SRAM X5 8 velocidades", 35, 8)
Piñon5 = Piñon("Shimano Alivio 9 velocidades", 40, 9)
Piñon6 = Piñon("SRAM X7 9 velocidades", 45, 9)
Piñon7 = Piñon("Shimano Deore 10 velocidades", 50, 10)
Piñon8 = Piñon("SRAM GX 10 velocidades", 70, 10)
Piñon9 = Piñon("Shimano SLX 11 velocidades", 60, 11)
Piñon10 = Piñon("SRAM NX Eagle 12 velocidades", 80, 12)
Piñon11 = Piñon("Shimano Nexus 7 velocidades", 35, 7)
Piñon12 = Piñon("SRAM Automatix 2 velocidades", 40, 2)

# Platos
Plato1 = Plato("Shimano Deore 30 dientes", 25, 30)
Plato2 = Plato("SRAM GX 32 dientes", 30, 32)
Plato3 = Plato("Race Face 34 dientes", 35, 34)
Plato4 = Plato("Shimano XT 36 dientes", 40, 36)
Plato5 = Plato("SRAM X1 38 dientes", 45, 38)
Plato6 = Plato("Absolute Black 40 dientes", 50, 40)
Plato7 = Plato("Rotor Q-Ring 42 dientes", 55, 42)
Plato8 = Plato("Shimano Ultegra 44 dientes", 60, 44)
Plato9 = Plato("SRAM Red 46 dientes", 65, 46)
Plato10 = Plato("Shimano Dura-Ace 48 dientes", 70, 48)
Plato11 = Plato("FSA Tempo 30 dientes", 30, 30)
Plato12 = Plato("Truvativ E400 32 dientes", 35, 32)

# Amortiguadores
Amortiguador1 = Amortiguador("SR Suntour XCR", 120, "Delantero")
Amortiguador2 = Amortiguador("RockShox Monarch", 100, "Trasero")
Amortiguador3 = Amortiguador("Fox 32 Float", 150, "Delantero")
Amortiguador4 = Amortiguador("Manitou Markhor", 180, "Delantero")
Amortiguador5 = Amortiguador("RockShox Pike", 200, "Delantero")
Amortiguador6 = Amortiguador("Fox Float DPS", 250, "Trasero")
Amortiguador7 = Amortiguador("RockShox Deluxe", 300, "Trasero")
Amortiguador8 = Amortiguador("Fox 36 Factory", 220, "Delantero")
Amortiguador9 = Amortiguador("RockShox Super Deluxe", 350, "Trasero")
Amortiguador10 = Amortiguador("Fox DHX2", 400, "Trasero")

# Frenos
Freno1 = Freno("Shimano Altus V-brake", 30, "V-brake")
Freno2 = Freno("Tektro M530 V-brake", 40, "V-brake")
Freno3 = Freno("Shimano Deore V-brake", 50, "V-brake")
Freno4 = Freno("SRAM Level V-brake", 60, "V-brake")
Freno5 = Freno("Avid BB7 V-brake", 70, "V-brake")
Freno6 = Freno("Shimano MT200 Disco", 80, "Disco")
Freno7 = Freno("SRAM Level T Disco", 110, "Disco")
Freno8 = Freno("Shimano SLX Disco", 120, "Disco")
Freno9 = Freno("Magura MT5 Disco", 130, "Disco")
Freno10 = Freno("SRAM Guide R Disco", 150, "Disco")

# Vacíos
Vacio1 = Vacio("Sin amortiguador", 0)

# Funciones para crear listas de componentes

def cuadros():
    return [Cuadro1, Cuadro2, Cuadro3, Cuadro4, Cuadro5, Cuadro6, Cuadro7, Cuadro8, Cuadro9, Cuadro10, Cuadro11, Cuadro12, Cuadro13, Cuadro14, Cuadro15, Cuadro16, Cuadro17, Cuadro18]

def ruedas():
    return [Rueda1, Rueda2, Rueda3, Rueda4, Rueda5, Rueda6, Rueda7, Rueda8, Rueda9, Rueda10, Rueda11, Rueda12, Rueda13, Rueda14, Rueda15, Rueda16, Rueda17, Rueda18]

def piñons():
    return [Piñon1, Piñon2, Piñon3, Piñon4, Piñon5, Piñon6, Piñon7, Piñon8, Piñon9, Piñon10, Piñon11, Piñon12]

def platos():
    return [Plato1, Plato2, Plato3, Plato4, Plato5, Plato6, Plato7, Plato8, Plato9, Plato10, Plato11, Plato12]

def amortiguadores():
    return [Amortiguador1, Amortiguador2, Amortiguador3, Amortiguador4, Amortiguador5, Amortiguador6, Amortiguador7, Amortiguador8, Amortiguador9, Amortiguador10]

def frenos():
    return [Freno1, Freno2, Freno3, Freno4, Freno5, Freno6, Freno7, Freno8, Freno9, Freno10]

# Funciones para crear diseño esqueletal

def mtb(famortiguador_delantero, famortiguador_trasero):
    if famortiguador_delantero and famortiguador_trasero:
        return [Cuadro6, Rueda1, Piñon1, Plato1, Amortiguador1, Amortiguador2, Freno1]
    elif famortiguador_delantero:
        return [Cuadro1, Rueda1, Piñon1, Plato1, Amortiguador1, Vacio1, Freno1]
    elif famortiguador_trasero:
        return [Cuadro6, Rueda1, Piñon1, Plato1, Vacio1, Amortiguador2, Freno1]
    else:
        return [Cuadro1, Rueda1, Piñon1, Plato1, Vacio1, Vacio1, Freno1]

def road():
    return [Cuadro2, Rueda2, Piñon1, Plato1, Vacio1, Vacio1, Freno1]

def paseo():
    return [Cuadro13, Rueda13, Piñon1, Plato1, Vacio1, Vacio1, Freno1]
