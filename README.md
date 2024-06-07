# bike-configurator

Bike Configurator es una aplicación basada en Python que ayuda a los usuarios a configurar bicicletas según su presupuesto y requisitos específicos. La aplicación ofrece varios tipos de bicicletas, incluyendo MTB (Mountain Bike), Road, y Paseo (Cruiser Bike). Garantiza que los componentes seleccionados sean compatibles y se ajusten al presupuesto del usuario.

## Tabla de Contenidos
- [Instalación](#instalación)
- [Uso](#uso)
- [Componentes](#componentes)
- [Opciones de Configuración](#opciones-de-configuración)
- [Manejo de Errores](#manejo-de-errores)

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/fjavifp4/bike-configurator.git
    cd bike-configurator/configurator
    ```

2. Ejecuta la aplicación:
    ```bash
    python3 App.py
    ```

## Uso

1. **Introducir Presupuesto**: Ingresa el presupuesto máximo para tu bicicleta.

2. **Seleccionar Tipo de Bicicleta**: Elige entre MTB, Road o Paseo.

3. **Seleccionar Opciones Adicionales**:
    - Para MTB, puedes optar por incluir suspensión delantera y/o trasera.
    
4. **Configurar**: Haz clic en el botón 'Configurar' para generar la mejor configuración posible de la bicicleta dentro de tu presupuesto.

5. **Ver Configuración**: Se mostrará la configuración resultante de la bicicleta junto con el precio total.

6. **Salir**: Utiliza el botón 'Salir' para cerrar la aplicación.

## Componentes

La aplicación utiliza componentes predefinidos para bicicletas categorizados en cuadros, ruedas, piñones, platos, suspensiones y frenos. Cada componente tiene un tipo y un precio asociado. Los componentes se seleccionan en función de la compatibilidad y las restricciones presupuestarias.

## Opciones de Configuración

- **MTB**: Opción para incluir suspensión delantera y/o trasera.
- **Road**: Sin opciones de suspensión.
- **Paseo**: Bicicletas cómodas tipo cruiser sin opciones de suspensión.

## Manejo de Errores

La aplicación proporciona mensajes de error detallados para varios escenarios:
- Presupuesto inválido.
- Presupuesto demasiado bajo para la configuración seleccionada.
- Presupuesto demasiado alto para la configuración seleccionada.
- Incompatibilidad entre los componentes seleccionados.