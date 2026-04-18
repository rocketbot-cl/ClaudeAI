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
   - View your current credit balance
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

3. **Process Document**:
   - Use the "Process Document" command
   - Enter the prompt that explains what you want to extract/analyze
   - Select the file to process
   - Select the model to use (e.g., claude-3-5-sonnet-20240620)
   - Configure optional parameters if desired:
     - Temperature (0-1): controls response creativity
     - Max Tokens: response token limit

4. **Query Available Models**:
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
