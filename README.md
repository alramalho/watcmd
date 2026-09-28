# ❓💻 watcmd

### A simple CLI tool to get UNIX commands from text explanations using AI
![image](https://github.com/user-attachments/assets/b9397477-0027-4d9e-8515-9ecb6e59bd8a)

## Installation

You can install `watcmd` directly from PyPI:

```
pip install watcmd
```

## Setup

After installation, you need to configure your Vercel AI Gateway API key. You can do this by running:

```
watcmd --setup YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual Vercel AI Gateway API key (create one in the Vercel dashboard under AI Gateway → API Keys). This will save your API key securely in a configuration file, so you don't need to set it as an environment variable each time.

Alternatively, you can set the `AI_GATEWAY_API_KEY` environment variable.

watcmd always uses the latest Claude Sonnet model available on the gateway (checked once a day), falling back to `anthropic/claude-sonnet-5.5`.

## Usage

Once you've set up your API key, you can use the tool like this:

```
watcmd your command description
```

For example:

```
watcmd to list all files in a directory
> ls -al
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

## Author

Alex Ramalho ([@alramalho](https://github.com/alramalho))
