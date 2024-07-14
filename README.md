# ❓💻 watcmd

### A simple CLI tool to get UNIX commands from text explanations using AI


https://github.com/user-attachments/assets/b0ce442d-4492-4482-a24a-3d47b27c382b

## Installation

You can install `watcmd` directly from PyPI:

```
pip install watcmd
```

## Setup

After installation, you need to configure your OpenAI API key. You can do this by running:

```
watcmd setup YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual OpenAI API key. This will save your API key securely in a configuration file, so you don't need to set it as an environment variable each time.

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
