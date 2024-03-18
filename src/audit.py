from src.metrics.agreement import AnnotatorAgreementMetrics
from src.validators.bias_detector import PreferenceBiasDetector


def main():
    print("================ RLHF PREFERENCE DATASET QA AUDIT ================")
    # 1. Agreement test
    r1 = [1, 1, 0, 1, 0, 1, 1, 0, 1, 1]
    r2 = [1, 1, 0, 1, 1, 1, 1, 0, 1, 1]
    kappa = AnnotatorAgreementMetrics.cohens_kappa(r1, r2)
    print(f"[*] Inter-Annotator Reliability (Cohen's Kappa): {kappa}")

    # 2. Bias test
    sample_chosen = "نموذج لغوي عالي الجودة يقدم إجابة مركزة ومفيدة ومطابقة للسياق."
    sample_rejected = "نموذج لغوي عادي."
    bias = PreferenceBiasDetector.audit_pair(sample_chosen, sample_rejected)
    print(f"[*] Sample Length Ratio: {bias['length_ratio']} (Flagged: {bias['flagged_length_bias']})")
    print("==================================================================")


if __name__ == "__main__":
    main()
