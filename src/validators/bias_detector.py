from typing import Dict, List


class PreferenceBiasDetector:
    """Detects length and superficial verbosity bias in preference datasets."""

    @staticmethod
    def audit_pair(chosen: str, rejected: str) -> Dict[str, float]:
        len_chosen = len(chosen.split())
        len_rejected = len(rejected.split())
        ratio = len_chosen / max(len_rejected, 1)

        is_biased = ratio > 1.6 or ratio < 0.6
        return {
            "chosen_tokens": len_chosen,
            "rejected_tokens": len_rejected,
            "length_ratio": round(ratio, 2),
            "flagged_length_bias": is_biased
        }
