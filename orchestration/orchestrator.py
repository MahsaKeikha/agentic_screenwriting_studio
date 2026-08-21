from AGENTS import story_agent,structure_agent,character_agent,continuity_agent,review_agent
def run(c): return {'story':story_agent.run(c),'structure':structure_agent.run(c),'character':character_agent.run(c),'continuity':continuity_agent.run(c),'review':review_agent.run(c)}
