# sample_meshop_UI
Sample Repo for a UI using Mesop

# Mesop
Mesop is a UI library from Google. Mesop is a Python-based UI framework that allows you to rapidly build web apps like demos and internal apps

# Pre-Requisites
- Gemini : For using with Gemini, you need the GEMINI API KEY
- Ollama : For using with Ollama models, you need to have Ollama installed in your local.

For generating Gemini API Keys : https://www.youtube.com/watch?v=qcZ8-nFskos

For installing Ollama and other models on local using docker : https://testerops.com/2024/05/02/run-ollama-models-on-local/

# Packages 
- `mesop`
- `google-generativeai`
- `ollama`
- `groq`
- `llama-index`
- `llama-index-llms-anthropic`
- `langchain_community`
- `langchain`

I will create a video on this for showing and explaining how this works and also explain the code.

# Run
To run the files

- `mesop run app.py` : This will run the file which contains Gemini Integration. Go to http://localhost:32123/chat ( since that is the path we provided)
- `mesop run sample_w_llama3.py` : This will run the file which contains Ollama Integration. Go to http://localhost:32123/chat-ollama ( since that is the path we provided)

# Ollama
![Screenshot 2024-06-24 at 1.24.05 PM.png](images%2FScreenshot%202024-06-24%20at%201.24.05%E2%80%AFPM.png)

# Gemini
![Screenshot 2024-06-24 at 1.26.29 PM.png](images%2FScreenshot%202024-06-24%20at%201.26.29%E2%80%AFPM.png)