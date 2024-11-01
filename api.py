import torchaudio
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from cosyvoice.cli.cosyvoice import CosyVoice
from cosyvoice.utils.file_utils import load_wav

app = FastAPI()
print("正在加载CosyVoice模型，请稍后...")
model = CosyVoice('data/model/CosyVoice-300M')
prompt_speech = load_wav('example.wav', 16000)
with open('example参考音频文本.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
prompt_text = lines[0].strip()
output_path = 'data/cache/cache.wav'


@app.get("/cosyvoice/")
def run_cosyvoice(text: str):
    results = model.inference_zero_shot(text, prompt_text, prompt_speech)
    tts_speech = results['tts_speech']
    torchaudio.save(output_path, tts_speech, 22050)
    return FileResponse(output_path)


print("本地CosyVoice语音合成大模型API服务器启动成功!")
uvicorn.run(app, host="0.0.0.0", port=9881)
