import difflib

class ClinicalEvaluator:
    def __init__(self, ground_truth):
        self.ground_truth = ground_truth

    def score_accuracy(self, output):
        """Calculates clinical accuracy against ground truth."""
        return round(difflib.SequenceMatcher(None, self.ground_truth, output).ratio() * 100, 2)

    def find_hallucinations(self, output, medical_terms):
        """Identifies fabricated medical terms not in the knowledge base."""
        return [t for t in medical_terms if t in output and t not in self.ground_truth]
