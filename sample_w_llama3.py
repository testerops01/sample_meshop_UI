import ollama
import mesop as me
import mesop.labs as melabs

@me.page(
    security_policy=me.SecurityPolicy(
        allowed_iframe_parents=["https://google.github.io"]
    ),
    path="/chat-ollama",
    title="Meshop Chat with Ollama"
)
def page():
    melabs.chat(transform, title="Mesop Chat with Ollama", bot_user="Mesop Bot")


def transform(input: str, history: list[melabs.ChatMessage]):
    messages = [{"role": "user", "content": message.content} for message in history]
    messages.append({"role": "user", "content": input})

    stream = ollama.chat(model='llama3', messages=messages, stream=True)

    for chunk in stream:
        content = chunk.get('message', {}).get('content', '')
        if content:
            yield content
