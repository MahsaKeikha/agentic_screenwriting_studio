"""Fail-closed governance for F132 Agentic Screenwriting Studio."""

PROTECTED_ACTIONS = {
    "submit_script",
    "release_screenplay",
    "approve_rights_clearance",
    "approve_final_credit",
    "send_to_production",
    "external_distribution",
}

REQUIRED_REVIEWS = (
    "story_reviewed",
    "structure_reviewed",
    "character_reviewed",
    "continuity_reviewed",
    "originality_rights_reviewed",
    "sensitivity_safety_reviewed",
    "evidence_provenance_reviewed",
    "qualified_creative_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding creative or production action is outside reference-system scope"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required screenwriting review", "missing": missing}
    checks = {
        "plagiarism_risk": "plagiarism or excessive similarity risk unresolved",
        "rights_clearance_gap": "rights, adaptation, quotation, or source clearance unresolved",
        "continuity_failure": "material continuity contradiction unresolved",
        "credit_authorship_gap": "authorship, attribution, or credit state unresolved",
        "privacy_likeness_risk": "privacy, likeness, or real-person portrayal risk unresolved",
        "sensitivity_safety_risk": "material sensitivity, safeguarding, or production-safety risk unresolved",
        "production_readiness_gap": "script package is not ready for production review",
        "evidence_provenance_gap": "research or source provenance incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "screenwriting governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "screenwriting support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
