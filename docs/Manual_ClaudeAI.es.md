



# ClaudeAI
  
Módulo para interactuar con los modelos de ClaudeAI desde Rocketbot.  

*Read this in other languages: [English](Manual_ClaudeAI.md), [Português](Manual_ClaudeAI.pr.md), [Español](Manual_ClaudeAI.es.md)*
  
![banner](imgs/Banner_ClaudeAI.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  

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

1. Visite la página de facturación en 
[console.anthropic.com/settings/billing](https://console.anthropic.com/settings/billing)

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

3. **Consultar Modelos Disponibles**:
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
## Descripción de los comandos

### Conectar con ClaudeAI
  
Establece conexión con ClaudeAI
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|API Key|Clave API de tu cuenta de ClaudeAI|sk-ant...|
|Asignar a variable|Nombre de la variable donde se guardará la conexión|resultadoClaudeAI|

### Obtener Modelos
  
Recupera los modelos disponibles de ClaudeAI
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar a variable|Nombre de la variable donde se guardará la lista de modelos|resultadoModelos|

### Generar Texto
  
Genera texto utilizando ClaudeAI
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Prompt|Texto de entrada para generar texto|Qué es Rocketbot?|
|Modelo|ID del modelo a utilizar|compound-beta-mini|
|Temperatura (opcional)|Controla la aleatoriedad de la generación de texto (0.0 a 2)|0.8|
|Máximo de tokens (opcional)|Número máximo de tokens a generar|100|
|Secuencia de parada (opcional)|Secuencia opcional para detener la generación de texto|herramienta RPA|
|Asignar a variable|Nombre de la variable donde se guardará el texto generado|resultadoTexto|
