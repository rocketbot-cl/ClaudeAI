



# ClaudeAI
  
Module to interact with ClaudeAI models from Rocketbot.  

*Read this in other languages: [English](Manual_ClaudeAI.md), [Português](Manual_ClaudeAI.pr.md), [Español](Manual_ClaudeAI.es.md)*
  
![banner](imgs/Banner_ClaudeAI.png o jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module

To use this module, we need to obtain a Claude AI API key and have available credits. Follow these steps:

### Getting the API Key

1. First, create an account or log in at [console.anthropic.com](https://console.anthropic.com/settings/keys).

2. Once on the API keys page, click the "Create Key" button to create a new key.

3. A window will open where you need to:
   - Select the workspace where the key will be used (default is "Default")
   - Enter a descriptive name for the key
   - Click "Add" to create the key

4. The API key will be displayed on screen. Use the copy button to save it.

**Important**: Make sure to save the key in a secure place, as you won't be able to see it again after closing this window.

### Purchasing Credits

To use the Claude API, you need to have available credits:

1. Visit the billing page at [console.anthropic.com/settings/billing](https://console.anthropic.com/settings/billing)

2. Here you can:
   - View your current credit 
balance
   - Purchase more credits as needed
   - Set up automatic payments if desired

**Note**: Without available credits, you won't be able to use the API even if you have a valid API key.

### Using the Module

Once you have your API key and available credits, you can use the module as follows:

1. **Connect to Claude AI**:
   - Use the "Connect to Claude AI" command
   - Enter your API key in the corresponding field
   - The module will verify the connection and display available models

2. **Generate Text**:
   - Use the "Generate Text" command
   - Enter your prompt or question
   - Select the model to use (e.g., claude-3-opus or claude-3-sonnet)
   - Configure optional parameters if desired:
     - Temperature (0-1): controls response creativity
     - Max Tokens: response token limit
     - System Prompt: general instructions or context for the model
     - Stop Sequence: text that will stop generation

3. **Query Available Models**:
   - Use the "Get Available Models" command

   - You'll see a list of models you can use with your account

### Recommendations

- Keep your API key secure and don't share it
- Monitor your credit usage regularly
- Use the most appropriate model for your use case:
  - claude-3-opus: higher capacity and accuracy
  - claude-3-sonnet: good balance between performance and cost
- Configure the system prompt to get more consistent responses
- Adjust temperature based on whether you need more precise (0) or creative (1) responses
## Description of the commands

### Connect to ClaudeAI
  
Establish connection to ClaudeAI
|Parameters|Description|example|
| --- | --- | --- |
|API Key|Your ClaudeAI API key|sk-ant...|
|Assign to variable|Variable name to store the connection|ClaudeAIResult|

### Get Models
  
Retrieve available models from ClaudeAI
|Parameters|Description|example|
| --- | --- | --- |
|Assign to variable|Variable name to store the list of models|modelsResult|

### Generate Text
  
Generate text using ClaudeAI
|Parameters|Description|example|
| --- | --- | --- |
|Prompt|Input text to generate text|What is Rocketbot?|
|Model|ID of the model to use|compound-beta-mini|
|Temperature (optional)|Controls the randomness of text generation (0.0 a 2)|0.8|
|Maximum tokens (optional)|Maximum number of tokens to generate|100|
|Stop sequence (optional)|Optional sequence to stop text generation|RPA tool|
|Assign to variable|Variable name to store the generated text|textResult|
