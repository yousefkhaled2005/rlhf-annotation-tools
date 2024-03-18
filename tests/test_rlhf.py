from src.metrics.agreement import AnnotatorAgreementMetrics
from src.validators.bias_detector import PreferenceBiasDetector


def test_kappa_agreement():
    r1 = [1, 1, 0, 0]
    r2 = [1, 1, 0, 0]
    assert AnnotatorAgreementMetrics.cohens_kappa(r1, r2) == 1.0


def test_bias_detector():
    res = PreferenceBiasDetector.audit_pair("كلمة واحدة", "عشرة كلمات طويلة جدا جدا لا داعي لها على الإطلاق")
    assert res["flagged_length_bias"] is True
