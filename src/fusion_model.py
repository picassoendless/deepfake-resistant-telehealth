"""fusion_model.py

Lightweight fusion model that concatenates embeddings and runs a threshold-based decision.
Replace with trained classifier for production.
"""
import numpy as np

class FusionModel:
    def __init__(self, threshold=0.5):
        self.threshold = threshold

    def score(self, voice_emb, face_emb, context_vec):
        # simple similarity/consistency proxy: normalized dot of first elements
        v = np.concatenate([voice_emb[:16], face_emb[:16], context_vec])
        # normalize
        norm = np.linalg.norm(v) + 1e-9
        s = float(np.sum(v) / norm)
        # map to [0,1] via sigmoid-like
        score = 1.0 / (1.0 + np.exp(-s*0.1))
        return score

    def decide(self, voice_emb, face_emb, context_vec):
        score = self.score(voice_emb, face_emb, context_vec)
        return {"score": score, "accept": bool(score >= self.threshold)}
