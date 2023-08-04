# transcribe.py

import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch

def transcribe_audio(file):
    # Model ve işlemci yükleme
    processor = Wav2Vec2Processor.from_pretrained("mpoyraz/wav2vec2-xls-r-300m-cv8-turkish")
    model = Wav2Vec2ForCTC.from_pretrained("mpoyraz/wav2vec2-xls-r-300m-cv8-turkish")

    waveform, sample_rate = torchaudio.load(file)
    resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
    waveform = resampler(waveform)
    input_values = processor(waveform.squeeze().numpy(), return_tensors="pt", sampling_rate=16000).input_values

    with torch.no_grad():
        logits = model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)

    transcription = processor.batch_decode(predicted_ids)
    return transcription[0]

