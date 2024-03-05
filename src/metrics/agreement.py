from typing import List, Tuple


class AnnotatorAgreementMetrics:
    """Calculates Cohen's Kappa for inter-annotator reliability."""

    @staticmethod
    def cohens_kappa(rater1: List[int], rater2: List[int]) -> float:
        if len(rater1) != len(rater2) or not rater1:
            return 0.0

        n = len(rater1)
        # Agreement count
        po = sum(1 for a, b in zip(rater1, rater2) if a == b) / n

        # Marginal probabilities
        c1 = sum(rater1) / n
        c2 = sum(rater2) / n
        pe = (c1 * c2) + ((1 - c1) * (1 - c2))

        if pe == 1.0:
            return 1.0
        return round((po - pe) / (1.0 - pe), 3)
