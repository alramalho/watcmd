import argparse
import configparser
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

from openai import OpenAI

CONFIG_DIR = Path.home() / '.config' / 'watcmd'
CONFIG_FILE = CONFIG_DIR / 'config.ini'

MODEL_CACHE_FILE = CONFIG_DIR / 'model_cache.json'
MODEL_CACHE_TTL = 24 * 60 * 60

GATEWAY_BASE_URL = "https://ai-gateway.vercel.sh/v1"
FALLBACK_MODEL = "anthropic/claude-sonnet-5.5"
SONNET_PATTERN = re.compile(r"^anthropic/claude-sonnet-(\d+(?:\.\d+)*)$")


def _version_key(model_id):
    return tuple(int(p) for p in SONNET_PATTERN.match(model_id).group(1).split('.'))


def get_latest_sonnet():
    """Resolve the newest Sonnet on the Vercel AI Gateway, cached for a day."""
    try:
        cache = json.loads(MODEL_CACHE_FILE.read_text())
        if time.time() - cache['fetched_at'] < MODEL_CACHE_TTL:
            return cache['model']
    except (OSError, ValueError, KeyError):
        pass

    try:
        with urllib.request.urlopen(f"{GATEWAY_BASE_URL}/models", timeout=3) as resp:
            ids = [m['id'] for m in json.load(resp)['data']]
        sonnets = [i for i in ids if SONNET_PATTERN.match(i)]
        model = max(sonnets, key=_version_key) if sonnets else FALLBACK_MODEL
    except Exception:
        return FALLBACK_MODEL

    try:
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        MODEL_CACHE_FILE.write_text(json.dumps({'model': model, 'fetched_at': time.time()}))
    except OSError:
        pass
    return model


def get_api_key():
    if CONFIG_FILE.exists():
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        return config['DEFAULT']['api_key']
    return os.environ.get('AI_GATEWAY_API_KEY')

def setup_config(api_key):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'api_key': api_key}
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)
    print(f"API key saved to {CONFIG_FILE}")


def query_llm(prompt):
    api_key = get_api_key()
    if not api_key:
        print("Error: Vercel AI Gateway API key not found. Please set it using 'watcmd --setup YOUR_API_KEY'")
        sys.exit(1)

    client = OpenAI(api_key=api_key, base_url=GATEWAY_BASE_URL)

    try:
        response = client.chat.completions.create(
            model=get_latest_sonnet(),
            messages=[
                {"role": "system", "content": "You are a silent assistant that just outputs UNIX cli commands"},
                {"role": "user", "content": "what command for listing all files"},
                {"role": "assistant", "content": "ls -a"},
                {"role": "user", "content": f"what command {prompt}"}
            ],
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error: API request failed. {str(e)}")
        sys.exit(1)



def main():
    parser = argparse.ArgumentParser(description="Get UNIX commands from text explanations using AI")
    parser.add_argument('--setup', metavar='API_KEY', help='Setup Vercel AI Gateway API key')
    parser.add_argument('query', nargs='*', help='The task description to get a UNIX command for')
    args = parser.parse_args()

    if args.setup:
        setup_config(args.setup)
        print("API key set successfully.")
    elif args.query:
        query = ' '.join(args.query)
        suggested_command = query_llm(query)
        print(suggested_command)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()