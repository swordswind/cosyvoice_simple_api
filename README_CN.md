# cosyvoice_simple_api

## 项目概述

`cosyvoice_simple_api` 是一个基于阿里的 CosyVoice 开发的简易的语音合成 API 服务器项目。它允许用户轻松地将文本转换为有情感的语音输出，适用于创建有声读物、自动语音回复系统以及其他语音合成应用。

### 项目地址

- CosyVoice 源地址：[FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice)
- CosyVoice Windows 适配版(特别鸣谢刘悦)：[v3ucn/CosyVoice_For_Windows](https://github.com/v3ucn/CosyVoice_For_Windows)
- 本项目地址：[swordswind/cosyvoice_simple_api](https://github.com/swordswind/cosyvoice_simple_api)

## 运行方式

1. 确保你的系统中已安装 Python 环境。
2. 通过 `git clone` 或下载 ZIP 文件的方式获取项目代码。
3. 在项目根目录下，运行以下命令安装依赖：

```bash
pip install -r requirements.txt
```

4. 在命令行中运行以下命令启动服务器：

```bash
python api.py
```

## 服务器地址

CosyVoice 语音合成 API 服务器地址为：`http://你的电脑IP:9881/`

## API 接口

### 接口地址

```
/cosyvoice/
```

### 请求方式

```
GET
```

### 请求参数

- `text`：必填，要合成的主体文本。

## 使用示例

1. 在浏览器地址栏输入以下地址：

```
http://127.0.0.1:9881/cosyvoice/?text=你好，很高兴遇见你
```

2. 按下回车键，服务器将返回输出格式为 wav 音频文件。

## 更换参考音频和参考音频文本

1. 将 `example.wav` 替换为自定义的参考音频，文件名保持不变。
2. 用记事本打开 `example参考音频文本.txt`，修改成新的自定义参考音频文本。
3. 修改完成后保存文件，并重新运行 `CosyVoice语音合成API服务器.bat` 文件。

## 技术栈

- FastAPI：用于构建 API 服务器。
- ModelScope：模型相关的库。
- Torch：PyTorch，用于深度学习模型。
- TorchAudio：用于音频处理。
- Uvicorn：ASGI 服务器，用于运行 FastAPI 应用。

## 贡献

欢迎对本项目进行贡献，包括但不限于修复 bug、增加新功能、改进文档等。在提交 Pull Request 之前，请确保你的代码通过了所有测试，并且遵循项目的代码风格。

## 许可证

本项目采用 [MIT 许可证](LICENSE)。