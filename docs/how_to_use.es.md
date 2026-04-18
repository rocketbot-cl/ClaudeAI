## Cómo usar este módulo

Para usar este módulo, necesitamos obtener una clave API de Claude AI y tener créditos disponibles. Sigue estos pasos:

### Obtener la API Key

1. Para comenzar, cree una cuenta o inicie sesión en [console.anthropic.com](https://console.anthropic.com/settings/keys).

2. Una vez en la página de claves API, haga clic en el botón "Create Key" para crear una nueva clave.

3. Se abrirá una ventana donde deberá:
   - Seleccionar el workspace donde se usará la clave (por defecto aparece "Default")
   - Ingresar un nombre descriptivo para la clave
   - Hacer clic en "Add" para crear la clave

4. La clave API se mostrará en pantalla. Utilice el botón de copiar para guardarla.

**Importante**: Asegúrese de guardar la clave en un lugar seguro, ya que no podrá verla nuevamente después de cerrar esta ventana.

### Comprar Créditos

Para poder usar la API de Claude, es necesario tener créditos disponibles:

1. Visite la página de facturación en [console.anthropic.com/settings/billing](https://console.anthropic.com/settings/billing)

2. Aquí podrá:
   - Ver su saldo actual de créditos
   - Comprar más créditos según necesite
   - Configurar el pago automático si lo desea

**Nota**: Sin créditos disponibles, no podrá usar la API aunque tenga una clave API válida.

### Uso del Módulo

Una vez que tenga su clave API y créditos disponibles, puede usar el módulo de la siguiente manera:

1. **Conectar con Claude AI**:
   - Use el comando "Connect to Claude AI"
   - Ingrese su clave API en el campo correspondiente
   - El módulo verificará la conexión y mostrará los modelos disponibles

2. **Generar Texto**:
   - Use el comando "Generate Text"
   - Ingrese su prompt o pregunta
   - Seleccione el modelo a usar (por ejemplo, claude-3-opus o claude-3-sonnet)
   - Configure los parámetros opcionales si lo desea:
     - Temperature (0-1): controla la creatividad de las respuestas
     - Max Tokens: límite de tokens para la respuesta
     - System Prompt: instrucciones o contexto general para el modelo
     - Stop Sequence: texto que detendrá la generación

3. **Procesar Documento**:
   - Use el comando "Process Document"
   - Ingrese el prompt indicando qué desea extraer/analizar
   - Seleccione el archivo a procesar
   - Seleccione el modelo a usar (por ejemplo, claude-3-5-sonnet-20240620)
   - Configure los parámetros opcionales si lo desea:
     - Temperature (0-1): controla la creatividad de las respuestas
     - Max Tokens: límite de tokens para la respuesta

4. **Consultar Modelos Disponibles**:
   - Use el comando "Get Available Models"
   - Verá una lista de los modelos que puede usar con su cuenta

### Recomendaciones

- Mantenga su clave API segura y no la comparta
- Monitoree su uso de créditos regularmente
- Use el modelo más apropiado para su caso de uso:
  - claude-3-opus: mayor capacidad y precisión
  - claude-3-sonnet: buen balance entre rendimiento y costo
- Configure el system prompt para obtener respuestas más consistentes
- Ajuste la temperatura según necesite respuestas más precisas (0) o creativas (1)
