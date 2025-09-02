📸 Calorie Counter Bot
A smart Telegram bot built with n8n that analyzes food photos to provide instant calorie and fat content information. This project showcases the power of workflow automation and AI integration for practical, real-world tasks.

🚀 Key Features
Instant Analysis: Simply send a photo of your meal to the bot to get a detailed nutritional breakdown.

AI-Powered: Integrates with a Generative AI model (Google Gemini) for accurate calorie and fat content estimations.

Easy to Use: A seamless, conversational interface through Telegram.

No-Code/Low-Code: Built entirely using the visual workflow automation tool, n8n.

⚙️ How It Works
The workflow is triggered when a user sends a photo to the Telegram bot. It then:

Downloads the Photo: Retrieves the image from the Telegram chat.

Analyzes with AI: Sends the image to the Google Gemini API with a custom prompt to identify the food and estimate its calories and fat content.

Sends a Response: Formats the AI's response into a friendly, conversational message and sends it back to the user on Telegram.

🛠️ Requirements
To run this bot, you will need a self-hosted instance of n8n. You will also need:

n8n: A local installation of the n8n application.

Telegram Bot Token: A unique token from BotFather to connect to your bot.

Telegram Chat ID: Your unique chat ID to receive messages from the bot.

Google Gemini API Key: An API key from Google AI Studio to power the AI analysis.

ngrok: A tunneling service to create a secure, public URL for your local n8n instance.

🚀 Setup Guide
Import the Workflow:

Open your n8n editor at http://localhost:5678.

Create a new, blank workflow.

Right-click on the canvas and select "Import from JSON" to upload the workflow file.

Configure Credentials:

Telegram: Double-click the Telegram nodes and add a new credential. Enter your Bot Token and Chat ID to connect to your bot.

Google Gemini: Double-click the "Analysis The Photo Deeply" node. Create a new credential and paste your Gemini API key.

Start the Tunnel:

Run ngrok http 5678 in a terminal to get a new public URL.

In a separate terminal, start n8n with the new ngrok URL:

set N8N_HOST=https://<YOUR_NGROK_URL>
set WEBHOOK_URL=https://<YOUR_NGROK_URL>
n8n

Activate the Workflow:

Go to your n8n editor and click the "Inactive" button to make your workflow "Active".