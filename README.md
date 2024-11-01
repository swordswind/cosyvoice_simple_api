# cosyvoice_simple_api

## Project Overview

`cosyvoice_simple_api` is a simple text-to-speech API server project developed based on Alibaba's CosyVoice. It allows users to easily convert text into emotionally rich voice output, suitable for creating audiobooks, automated voice response systems, and other text-to-speech applications.

### Project Addresses

- CosyVoice Source Address: [FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice) 
- CosyVoice Windows Adaptation (Special thanks to Liu Yue): [v3ucn/CosyVoice_For_Windows](https://github.com/v3ucn/CosyVoice_For_Windows) 
- This Project Address: [swordswind/cosyvoice_simple_api](https://github.com/swordswind/cosyvoice_simple_api) 

## Running Method

1. Ensure that a Python environment is installed in your system.
2. Obtain the project code via `git clone` or by downloading the ZIP file.
3. In the project root directory, run the following command to install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the following command in the command line to start the server:

```bash
python api.py
```

## Server Address

The CosyVoice text-to-speech API server address is: `http://your-computer-IP:9881/`

## API Interface

### Interface Address

```
/cosyvoice/
```

### Request Method

```
GET
```

### Request Parameters

- `text`: Required, the main text to be synthesized.

## Usage Example

1. Enter the following address in the browser's address bar:

```
http://127.0.0.1:9881/cosyvoice/?text=Hello, nice to meet you
```

2. Press Enter, and the server will return a response in the format of a wav audio file.

## Changing Reference Audio and Reference Audio Text

1. Replace `example.wav` with your custom reference audio, keeping the file name unchanged.
2. Open `example_reference_audio_text.txt` with Notepad and modify it to your new custom reference audio text.
3. After modification, save the file and rerun the `CosyVoice Text-to-Speech API Server.bat` file.

## Technology Stack

- FastAPI: Used for building the API server.
- ModelScope: A library related to models.
- Torch: PyTorch, used for deep learning models.
- TorchAudio: Used for audio processing.
- Uvicorn: ASGI server, used to run FastAPI applications.

## Contribution

Contributions to this project are welcome, including but not limited to fixing bugs, adding new features, and improving documentation. Before submitting a Pull Request, please ensure that your code passes all tests and adheres to the project's coding style.

## License

This project is licensed under the [MIT License](LICENSE).