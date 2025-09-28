"""face_encoder.py

Placeholder face encoder: in the real project replace with a ResNeXt/Transformer encoder that extracts micro-motion features.
"""
import numpy as np

class FaceEncoder:
    def __init__(self, embedding_dim=128):
        self.embedding_dim = embedding_dim

    def encode(self, frames):
        """frames: list/array of per-frame feature vectors or flattened frames
        Returns a pseudo-embedding.
        """
        arr = np.array(frames, dtype=float)
        mean = float(np.mean(arr)) if arr.size else 0.0
        std = float(np.std(arr)) if arr.size else 0.0
        vec = np.zeros(self.embedding_dim, dtype=float)
        vec[:2] = np.array([mean, std])
        return vec
