# ❓💻 watcmd

A CLI tool to get UNIX commands from text explanations using AI

## Installation

You can install `watcmd` directly from PyPI:

```
pip install watcmd
```

## Setup

After installation, you need to configure your Anthropic API key. You can do this by running:

```
watcmd setup YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual Anthropic API key. This will save your API key securely in a configuration file, so you don't need to set it as an environment variable each time.

## Usage

Once you've set up your API key, you can use the tool like this:

```
watcmd your command description
```

For example:

```
watcmd to list all files in a directory
```

The tool will return an explanation of how to perform the task in a UNIX system.

You can also use the explicit query command:

```
watcmd query your command here
```

## Development

If you want to contribute or modify the tool:

1. Clone this repository:
   ```
   git clone https://github.com/alramalho/watcmd.git
   cd watcmd
   ```

2. Install the package in editable mode:
   ```
   pip install -e .
   ```

3. Make your changes and test them locally.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

## Author

Alex Ramalho ([@alramalho](https://github.com/alramalho))
