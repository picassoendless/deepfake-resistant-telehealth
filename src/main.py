"""main.py - demo entrypoint for the scaffold project

Run: python -m src.main
"""
import numpy as np
from datetime import datetime
from voice_encoder import VoiceEncoder
from face_encoder import FaceEncoder
from context_checker import ContextChecker
from fusion_model import FusionModel

def demo_run():
    # Create dummy inputs
    audio = np.sin(np.linspace(0, 3.14, 1600))  # fake waveform
    frames = [np.random.rand(8) for _ in range(10)]  # fake frame features
    ctx = {"ip_address": "198.51.100.23", "device_id": "demo-device-1", "timestamp": datetime.utcnow()}

    # Initialize pipeline components
    venc = VoiceEncoder()
    fenc = FaceEncoder()
    ctxchk = ContextChecker()
    fusion = FusionModel(threshold=0.5)

    v_emb = venc.encode(audio)
    f_emb = fenc.encode(frames)
    c_vec = ctxchk.score(ip_address=ctx['ip_address'], device_id=ctx['device_id'], timestamp=ctx['timestamp'])

    result = fusion.decide(v_emb, f_emb, c_vec)
    print("=== Demo run result ===")
    print(f"Score: {result['score']:.4f}")
    print(f"Accept: {result['accept']}")
    print("(Embeddings shapes)", v_emb.shape, f_emb.shape, c_vec.shape)

if __name__ == '__main__':
    demo_run()
