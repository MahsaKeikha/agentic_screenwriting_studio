from AGENTS import character_agent, continuity_agent, review_agent, story_agent, structure_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "story": story_agent.run(case),
        "structure": structure_agent.run(case),
        "character": character_agent.run(case),
        "continuity": continuity_agent.run(case),
        "review": review_agent.run(case),
    }
    governance = authorize("release_support_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
