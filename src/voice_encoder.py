"""voice_encoder.py

Placeholder voice encoder: in the real project replace with spectrogram CNN encoder.
"""
import numpy as np

class VoiceEncoder:
    def __init__(self, embedding_dim=128):
        self.embedding_dim = embedding_dim

    def encode(self, audio_waveform):
        """Return a deterministic pseudo-embedding for an audio waveform.
        audio_waveform: 1D numpy array or list
        """
        arr = np.array(audio_waveform, dtype=float)
        # simple, tiny "embedding": normalized mean/std + length -> reproducible
        mean = float(np.mean(arr)) if arr.size else 0.0
        std = float(np.std(arr)) if arr.size else 0.0
        length = float(arr.size)
        vec = np.zeros(self.embedding_dim, dtype=float)
        vec[:3] = np.array([mean, std, length])
        return vec
