"""Held-out governance scenarios for F132."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"plagiarism_risk": True}, False),
    (base() | {"rights_clearance_gap": True}, False),
    (base() | {"continuity_failure": True}, False),
    (base() | {"credit_authorship_gap": True}, False),
    (base() | {"privacy_likeness_risk": True}, False),
    (base() | {"sensitivity_safety_risk": True}, False),
    (base() | {"production_readiness_gap": True}, False),
    (base() | {"evidence_provenance_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_support_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F132 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
