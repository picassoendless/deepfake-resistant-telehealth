"""context_checker.py

Simple contextual anomaly checker stub (IP/device/timing). Replace with more advanced heuristics or ML scoring.
"""
from datetime import datetime
import numpy as np

class ContextChecker:
    def __init__(self):
        pass

    def score(self, ip_address=None, device_id=None, timestamp=None):
        """Return a small context score vector summarizing anomalies.
        For demo: returns [ip_change_flag, new_device_flag, odd_hour_flag]
        """
        # Dummy rules:
        ip_change_flag = 0.0
        new_device_flag = 0.0
        if timestamp is None:
            timestamp = datetime.utcnow()
        hour = timestamp.hour
        odd_hour_flag = 1.0 if (hour < 6 or hour > 23) else 0.0
        return np.array([ip_change_flag, new_device_flag, odd_hour_flag], dtype=float)
