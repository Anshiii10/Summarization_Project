import click
import os
import requests

# Replace with your Ollama API key
OLLAMMA_API_KEY = 'ollama/id_ed25519.pub'

def summarize_text(text):
    """Summarize text using Ollama API and Qwen2 0.5B model."""
    url = "https://api.ollama.ai/v1/summarize"
    data = {"text": text, "model": "qwen2-0.5B"}
    headers = {"Authorization": f"Bearer {'olama/id_ed25519.pub'}"}
    data = {"text": text, "model": "qwen2-0.5B"}
    headers = {"Authorization": f"Bearer {OLLAMMA_API_KEY}"}
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()["summary"]

def summarize_file(file_path):
    """Summarize text file using Ollama API and Qwen2 0.5B model."""
    with open(file_path, "r") as f:
        text = f.read()
    return summarize_text(text)

@click.command()
@click.option("-t", "--text", help="Text to summarize.")
@click.option("-f", "--file", type=click.Path(exists=True), help="Text file to summarize.")
def summarize(text, file):
    """Summarize text or text file using Ollama API and Qwen2 0.5B model."""
    if text:
        summary = summarize_text(text)
    elif file:
        summary = summarize_file(file)
    else:
        raise click.ClickException("Either -t or -f option must be provided.")
    click.echo(f".Summary of {file or 'text pasted'}.\n\n{summary}")

if __name__ == "__main__":
    summarize()
