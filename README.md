# F132 | Agentic Screenwriting Studio | L3 Gold Standard | v1.0

A governed five-agent reference architecture for screenwriting development across story, structure, character, continuity, research provenance, originality, rights, sensitivity, production readiness, and qualified human creative approval.

F132 is decision-support and creative-development infrastructure. It can develop original story options, organize beats and scenes, maintain character and continuity records, identify revision risks, and prepare review packages. It cannot autonomously submit or release a screenplay, approve rights clearance, determine final credits, send material to production, or distribute creative work externally.

## Screenwriting lifecycle

```text
Premise and Creative Intent
        -> Story Development
        -> Structure and Scene Design
        -> Character Architecture
        -> Continuity and Research Review
        -> Originality, Rights, Sensitivity, and Production Review
        -> Qualified Human Creative Approval
        -> Human-Controlled Submission or Production
```

The workflow fails closed when required reviews are missing or when material plagiarism, rights, continuity, authorship, privacy, likeness, sensitivity, safety, production-readiness, or provenance risks remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Story Agent | Develops premise, dramatic question, conflict, theme, stakes, world, and story options | What story is being told and why does it matter? |
| Structure Agent | Organizes acts, sequences, beats, scenes, turning points, setup, payoff, and pacing | Does the dramatic architecture support the intended experience? |
| Character Agent | Maintains character goals, motivations, relationships, arcs, voice, contradictions, and agency | Are characters coherent, distinct, and dramatically functional? |
| Continuity Agent | Tracks chronology, world rules, props, locations, knowledge state, causality, and cross-scene consistency | Does the screenplay remain internally consistent? |
| Review Agent | Integrates originality, rights, research, sensitivity, production, provenance, and approval state | Is the creative package appropriate for qualified human review? |

Agents support writers and creative teams. They do not replace screenwriters, showrunners, directors, producers, script editors, legal counsel, rights professionals, intimacy coordinators, safety teams, cultural consultants, unions, guilds, or production leadership.

## Repository structure

```text
AGENTS/
├── story_agent.py
├── structure_agent.py
├── character_agent.py
├── continuity_agent.py
└── review_agent.py

SKILLS/
├── story_reasoning.py
├── structure_reasoning.py
├── character_reasoning.py
├── continuity_reasoning.py
└── review_reasoning.py

TOOLS/
├── beat_sheet.py
├── scene_index.py
├── character_bible.py
├── continuity_log.py
└── review_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Creative intent

Screenwriting begins with authorial intent. The system should preserve genre, audience, tone, format, thematic questions, dramatic goals, production context, and explicit creative constraints rather than optimizing toward a generic formula.

## Premise

A premise can define protagonist, situation, conflict, stakes, and distinguishing dramatic mechanism. F132 can generate alternatives, but creative ownership and selection remain human decisions.

## Logline

Loglines are compression tools rather than substitutes for the screenplay. They should accurately represent the central dramatic engine without inventing elements absent from the intended story.

## Theme

Theme can emerge through character choice, conflict, imagery, consequence, and dramatic contrast. F132 should avoid turning thematic intent into repetitive exposition.

## Story world

World design can preserve setting, social rules, technology, institutions, geography, culture, history, constraints, and exceptions. World rules should be versioned when they affect later scenes.

## Story agent

The policy requires `story_reviewed`.

The Story Agent can explore conflict, stakes, escalation, reversals, revelations, setup, payoff, thematic tension, and alternate story paths. It should distinguish proposed creative options from established canon.

## Structure

The policy requires `structure_reviewed`.

Structure can be analyzed through acts, sequences, beats, scenes, turning points, reversals, midpoint changes, climax, resolution, or other frameworks appropriate to the work.

No single structural model is mandatory. Three-act, five-act, episodic, nonlinear, ensemble, anthology, experimental, and other forms can all be legitimate.

## Beat sheets

`TOOLS/beat_sheet.py` provides a deterministic surface for tracking beat order and purpose. A production implementation can preserve:

```text
beat_id
sequence
story_function
character_goal
conflict
turn
setup
payoff
continuity_dependencies
status
```

## Scene design

A scene can be tracked by location, time, participants, point of view, objective, obstacle, turn, information change, emotional change, setup, payoff, and production notes.

## Scene index

`TOOLS/scene_index.py` can support deterministic scene tracking across revisions. Scene identifiers should remain stable where possible so notes and continuity records can survive pagination changes.

## Pacing

Pacing is not simply scene length. It can depend on information density, tension, emotional processing, action, silence, expectation, rhythm, visual change, and narrative urgency.

## Setup and payoff

Setups should be traceable to later consequences where relevant. F132 can identify unresolved setups, repeated exposition, premature reveals, or payoffs unsupported by prior story information.

## Character architecture

The policy requires `character_reviewed`.

Character analysis can include wants, needs, fears, beliefs, contradictions, skills, relationships, secrets, status, values, decision patterns, and arc state.

## Character bible

`TOOLS/character_bible.py` can preserve:

```text
character_id
name
role
goal
motivation
stakes
relationships
knowledge_state
arc_state
voice_notes
continuity_facts
version
```

## Character agency

Major characters should make meaningful choices appropriate to the intended story. F132 can flag when plot events repeatedly happen to a character without meaningful decision-making, while leaving creative judgment to the writer.

## Character voice

Dialogue and behavior should reflect character history, relationship, status, objective, emotional state, and context. Distinctiveness should not rely on stereotypes or caricature.

## Character arcs

Arcs can involve transformation, corruption, revelation, steadfastness, reconciliation, tragedy, maturation, or other forms. Not every character requires the same arc structure.

## Relationships

Relationship state should be tracked across scenes. Trust, attraction, resentment, power, knowledge, loyalty, obligation, and conflict can change over time and affect dialogue and behavior.

## Dialogue

Dialogue should serve character and dramatic purpose while allowing subtext, interruption, silence, misdirection, rhythm, and contradiction. F132 should not force every line to explicitly state intent.

## Subtext

Subtext can be modeled as the difference between spoken content, immediate objective, emotional truth, and withheld information. It should remain consistent with character knowledge and context.

## Exposition

Exposition should be evaluated for necessity, timing, point of view, repetition, and dramatic integration. The system can identify information already established elsewhere.

## Continuity

The policy requires `continuity_reviewed`.

Continuity includes chronology, geography, character knowledge, physical state, costume, props, injuries, relationships, world rules, weather, time of day, travel, causality, and scene dependencies.

`continuity_failure` blocks release when a material contradiction remains unresolved.

## Continuity log

`TOOLS/continuity_log.py` can track facts across scenes and revisions. Useful fields include scene, entity, fact, introduced version, dependencies, conflict state, resolution, and reviewer.

## Character knowledge state

A character should not act on information they have not learned unless the story intentionally establishes another source. Knowledge-state errors are a common form of continuity failure.

## Chronology

Nonlinear storytelling still requires an internally coherent chronology. F132 can maintain both presentation order and story-world chronological order.

## Causality

Events should have sufficient causal support for the intended genre and tone. Coincidence can be a deliberate device, but the system should distinguish deliberate coincidence from accidental logic gaps.

## Research

Historical, scientific, legal, medical, cultural, technical, geographic, or institutional details can require research. Creative fiction permits invention, but real-world claims and production assumptions should preserve source provenance.

The policy requires `evidence_provenance_reviewed`.

## Research provenance

Material research can preserve source, date, topic, reliability, limitations, interpretation, script usage, and reviewer. `evidence_provenance_gap` blocks release when important source provenance is incomplete.

## Historical fiction

Historical screenwriting should distinguish documented fact, disputed interpretation, compression, composite characters, invented dialogue, and deliberate fictionalization.

## Biographical stories

Projects based on real people can involve life rights, privacy, defamation, publicity rights, archival materials, estates, contracts, and jurisdiction-specific legal issues. F132 does not determine legal clearance.

## Real-person portrayals

`privacy_likeness_risk` blocks release when unresolved privacy, likeness, publicity, defamation, or real-person portrayal concerns remain material.

The system should not treat publicly known information as automatic permission for every portrayal or use.

## Adaptations

Adaptation work can involve novels, articles, podcasts, games, plays, biographies, news events, songs, existing films, characters, trademarks, or other source material.

Rights status should be explicit before a production package is treated as cleared.

## Rights clearance

`rights_clearance_gap` blocks release when adaptation, quotation, music, image, character, trademark, archival, or other relevant rights remain unresolved.

`approve_rights_clearance` is a protected action reserved for authorized rights and legal professionals.

## Originality

The policy requires `originality_rights_reviewed`.

F132 should help create original expression rather than reproducing protected scripts, scenes, dialogue, or distinctive expression from existing works.

## Plagiarism and excessive similarity

`plagiarism_risk` blocks release when material plagiarism or excessive similarity remains unresolved.

Genre conventions, tropes, archetypes, and broad ideas can recur across works, but distinctive protected expression should not be copied.

## Reference works

Writers can identify tonal, structural, visual, or genre references. References should guide high-level creative direction rather than become instructions to reproduce a living creator's distinctive expression or a protected work.

## Authorship

Human writers retain authorship decisions. F132 should preserve which material was human-written, AI-assisted, imported, adapted, commissioned, or revised where workflow policy requires it.

## Credit governance

`credit_authorship_gap` blocks release when material authorship or attribution status remains unresolved.

`approve_final_credit` remains outside autonomous authority. Credits can be governed by contracts, guild rules, arbitration, employment terms, and production agreements.

## Revision history

Drafts should preserve version identifiers, date, author or editor, revision purpose, changed scenes, unresolved notes, and approval state.

## Notes

Notes can come from writers, producers, directors, actors, executives, financiers, studios, networks, consultants, legal teams, or test audiences. F132 should preserve note source and status rather than silently merging conflicting direction.

## Note reconciliation

Conflicting notes should be surfaced as tradeoffs. The system should not manufacture consensus when stakeholders have different creative or commercial priorities.

## Rewrite planning

A rewrite plan can prioritize structural changes before line-level polishing where appropriate. Dependencies should be identified so revisions do not create new continuity problems.

## Draft locking

Production workflows may lock scenes, pages, dialogue, or shooting drafts. F132 should not overwrite locked material without explicit authorized workflow state.

## Production readiness

`production_readiness_gap` blocks release when the script package is materially incomplete for the intended production-review stage.

Readiness can include script version, scene numbering, locked elements, rights flags, research flags, safety notes, production assumptions, revision status, and approval state.

## Production feasibility

Screenwriting decisions can affect locations, cast, stunts, visual effects, animals, children, vehicles, weather, night work, crowds, period elements, music, intimacy, weapons, special effects, and budget.

F132 can identify production implications but does not approve budgets or production methods.

## Production safety

The policy requires `sensitivity_safety_reviewed`.

Scripts involving stunts, weapons, pyrotechnics, vehicles, water, heights, animals, hazardous environments, intimacy, minors, or other safety-sensitive elements should be reviewed by qualified production professionals.

The screenplay system should never substitute fictional description for real-world safety planning.

## Intimacy

Scenes involving intimacy, nudity, sexual content, or vulnerable performance conditions require professional consent-based production processes. F132 can flag such scenes for appropriate review but does not determine performer consent or choreography.

## Minors

Projects involving child performers require heightened legal, safeguarding, scheduling, educational, consent, and production review. F132 should flag relevant scenes and avoid treating fictional consent as real-world authorization.

## Violence

Violence can serve legitimate dramatic purposes. Production planning for fights, weapons, stunts, blood effects, or dangerous actions belongs to qualified production teams.

## Sensitive subject matter

Stories can explore trauma, suicide, abuse, addiction, discrimination, war, illness, disability, religion, politics, crime, or other sensitive subjects. Review should focus on context, accuracy where relevant, avoidable harm, representation, and production implications without erasing legitimate artistic expression.

## Cultural context

Cultural consultants or subject-matter experts can be valuable when a project depicts communities, languages, traditions, histories, or identities outside the creative team's expertise.

## Representation

Character diversity should not be reduced to demographic checklists. F132 can identify stereotypes, tokenism, flattening, or inconsistent characterization while preserving the writer's creative authority.

## Disability representation

Disability should not automatically be framed as tragedy, inspiration, villainy, or cure narrative. Relevant lived-experience and accessibility review can improve authenticity.

## Language and dialect

Dialect and multilingual dialogue should preserve meaning and character without relying on demeaning phonetic caricature. Qualified language review may be appropriate.

## Location and geography

Travel time, geography, architecture, climate, jurisdiction, and local context can affect story logic. Real locations can also introduce permissions and production constraints outside the screenplay system's authority.

## Format

F132 can support feature films, shorts, television episodes, pilots, limited series, web series, animation, interactive narrative, audio-visual hybrids, and other scripted formats.

Each format can require different structural and production conventions.

## Feature films

Feature development can track global arc, act progression, sequence structure, pacing, protagonist objective, climax, and resolution while preserving genre-specific flexibility.

## Television

Television development can additionally track episode engine, season arcs, act breaks where applicable, serialized versus episodic information, character availability, production blocks, and future-story dependencies.

## Series bible

A series bible can preserve premise, world, character canon, season direction, episode engine, tone, recurring locations, terminology, and continuity rules. It should be versioned alongside scripts.

## Pilot scripts

A pilot must function as a story while establishing a repeatable dramatic engine. F132 can identify elements introduced solely as exposition versus elements that generate future conflict.

## Episodic continuity

For series, continuity extends across episodes and seasons. Character knowledge, relationships, injuries, objects, world rules, and unresolved setups should be traceable across the canon.

## Animation

Animation can allow different physical possibilities while still requiring internal rules, asset considerations, voice performance, timing, and production feasibility.

## Interactive narrative

Branching stories require state tracking across choices. Continuity should preserve reachable states, prerequisites, consequences, convergence, and impossible branches.

## Genre

Genre expectations can inform audience promises without becoming rigid formulas. Horror, comedy, thriller, romance, science fiction, fantasy, drama, mystery, action, and hybrids each create different expectations around pacing, information, tone, and payoff.

## Comedy

Comedy depends heavily on timing, character, surprise, incongruity, escalation, and context. F132 should not optimize comedy by simply increasing joke density.

## Mystery

Mystery structures require fair clue placement, information control, red herrings, reveal timing, and solution coherence. The continuity system can track who knows what and when.

## Science fiction and fantasy

Speculative stories should maintain internal rules for technology, magic, institutions, species, geography, and constraints. Rule exceptions should be deliberate and traceable.

## Horror

Horror can depend on uncertainty, vulnerability, escalation, atmosphere, and controlled information. Production safety remains separate from fictional danger.

## Romance

Relationship development should preserve consent, agency, emotional progression, conflict, compatibility, and changing knowledge rather than treating attraction as sufficient character logic.

## Action

Action sequences should have dramatic purpose, spatial clarity, objectives, obstacles, reversals, and consequences. Real stunt design and safety remain outside F132.

## Tone

Tone can be tracked through language, violence, humor, pacing, visual assumptions, emotional distance, and character behavior. Abrupt tonal changes can be flagged without assuming they are errors.

## Rating and audience considerations

Content intensity, language, violence, sexuality, drug use, and thematic material can affect intended audience and distribution. F132 can flag content considerations but does not assign official ratings.

## Production notes

Script notes can identify effects, special requirements, research dependencies, continuity risks, rights flags, and safety review needs. They should not masquerade as final departmental instructions.

## Budget sensitivity

The system can identify potentially high-cost elements such as large crowds, period settings, extensive VFX, multiple distant locations, night exteriors, animals, or complex action. It cannot approve or commit production budgets.

## Scheduling implications

Story order and shooting order differ. F132 can surface continuity dependencies relevant to scheduling while leaving scheduling authority to production professionals.

## Casting boundaries

Character descriptions can communicate story-relevant traits. F132 should not make binding casting decisions, evaluate protected characteristics for employment, or rank real performers.

## Audition material

Sides can be derived from authorized script material for human-controlled production use. Rights and confidentiality should be preserved.

## Confidentiality

Unreleased scripts, story twists, casting plans, production details, contact information, contracts, and notes can be confidential. F132 should minimize unnecessary disclosure.

## Security and leaks

Production implementations should use access control, watermarking where appropriate, version tracking, least privilege, and audit logs. The reference architecture does not distribute confidential scripts autonomously.

## External submission

`submit_script` is protected. F132 cannot autonomously submit material to agents, managers, producers, studios, competitions, festivals, guilds, financiers, or platforms.

## Script release

`release_screenplay` is protected. Passing internal review does not itself create publication or distribution authority.

## Production handoff

`send_to_production` is protected. A screenplay support package can be prepared for human review, but actual production handoff remains a human-controlled action.

## External distribution

`external_distribution` is protected. F132 cannot autonomously email, upload, post, publish, or otherwise distribute screenplay material outside the governed environment.

## Versioning

Every material draft should have a stable version identifier. Revision state can include draft, revised draft, production draft, locked, superseded, archived, or other organization-defined statuses.

## Change impact

A change to one scene can affect character motivation, setup and payoff, continuity, chronology, props, locations, production requirements, or later dialogue. F132 should identify downstream dependencies before a revision is treated as complete.

## Memory and state

The `memory/` layer can preserve structured creative state across agents. It should distinguish canon, proposals, rejected ideas, research, rights status, continuity facts, notes, approvals, and production assumptions.

## Observability

The `observability/` layer supports traceability across story, structure, character, continuity, originality, rights, research, sensitivity, production, and governance states.

Useful telemetry includes draft version, scene count, unresolved continuity issues, rights flags, research gaps, sensitive-content flags, production-readiness state, approvals, and protected-action attempts.

## Required reviews

The executable policy requires all eight conditions:

```text
story_reviewed
structure_reviewed
character_reviewed
continuity_reviewed
originality_rights_reviewed
sensitivity_safety_reviewed
evidence_provenance_reviewed
qualified_creative_approval
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- plagiarism or excessive similarity risk remains unresolved
- rights, adaptation, quotation, or source clearance is incomplete
- a material continuity contradiction remains unresolved
- authorship, attribution, or credit state is unresolved
- privacy, likeness, publicity, or real-person portrayal risk remains unresolved
- material sensitivity, safeguarding, or production-safety risk remains unresolved
- the script package is not ready for its intended production-review stage
- research or source provenance is incomplete
- any required review is missing
- qualified creative approval is missing

The system exposes blockers rather than manufacturing creative or legal clearance.

## Protected actions

The safety policy permanently protects:

```text
submit_script
release_screenplay
approve_rights_clearance
approve_final_credit
send_to_production
external_distribution
```

These remain outside autonomous authority even after all required reviews are satisfied.

## Human authority boundaries

F132 must not autonomously submit or release scripts, approve rights, determine final credits, make binding casting decisions, authorize production safety, disclose confidential material, send scripts to production, or distribute creative work externally.

Qualified humans retain control over authorship, final creative decisions, legal clearance, credits, casting, production, safety, submission, and distribution.

## Explicit failure states

```text
STORY REVIEW REQUIRED
STRUCTURE REVIEW REQUIRED
CHARACTER REVIEW REQUIRED
CONTINUITY REVIEW REQUIRED
PLAGIARISM RISK
RIGHTS CLEARANCE GAP
CONTINUITY FAILURE
AUTHORSHIP OR CREDIT GAP
PRIVACY OR LIKENESS RISK
SENSITIVITY OR SAFETY REVIEW REQUIRED
PRODUCTION READINESS GAP
EVIDENCE PROVENANCE GAP
QUALIFIED CREATIVE APPROVAL REQUIRED
SCRIPT SUBMISSION PROHIBITED
SCREENPLAY RELEASE PROHIBITED
AUTONOMOUS RIGHTS APPROVAL PROHIBITED
AUTONOMOUS CREDIT APPROVAL PROHIBITED
PRODUCTION HANDOFF PROHIBITED
EXTERNAL DISTRIBUTION PROHIBITED
```

## End-to-end reference workflow

1. Define creative intent, format, genre, audience, premise, and constraints.
2. Develop story options, dramatic question, conflict, stakes, world, and theme.
3. Build structural beats, sequences, scenes, setups, payoffs, and turning points.
4. Build character bibles with goals, motivations, relationships, knowledge, and arc state.
5. Track chronology, world rules, scene dependencies, and continuity facts.
6. Register research and distinguish documented fact from deliberate fiction.
7. Review originality, adaptation status, rights, quotations, real-person portrayals, and attribution.
8. Review sensitivity, safeguarding, accessibility, and production-safety implications.
9. Reconcile notes, revisions, continuity impacts, and production-readiness state.
10. Preserve provenance, version history, unresolved risks, and approvals.
11. Apply fail-closed governance and require qualified human creative approval.
12. Keep submission, release, rights approval, final credit, production handoff, and external distribution outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test story coherence, structural reasoning, character consistency, continuity detection, research provenance, originality awareness, sensitivity escalation, and governance behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved support release, plagiarism risk, rights gaps, continuity failures, authorship or credit gaps, privacy or likeness risk, sensitivity or safety risk, production-readiness gaps, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed behavior, held-out governance scenarios, and execution of the governed reference workflow.

## Reproducibility

Reproducible screenwriting analysis requires preserving draft versions, story canon, beat sheets, scene IDs, character bibles, continuity facts, research sources, rights state, note history, production assumptions, unresolved issues, and approval state.

## Extension points

Organization-specific implementations can add governed integrations for script editors, production-management systems, research repositories, rights databases, version-control systems, breakdown tools, scheduling software, asset systems, and review workflows.

Any integration capable of submitting, distributing, publishing, or changing production state should remain behind explicit authorization, least privilege, audit logging, and human-controlled execution.

## Example applications

Potential governed uses include feature development, pilot development, episodic continuity, character bibles, scene analysis, rewrite planning, adaptation research, historical research, writers-room support, continuity audits, production-readiness review, and screenplay training.

F132 is not an autonomous screenwriter of record, rights authority, casting director, producer, safety coordinator, studio executive, guild authority, or distribution platform.

## Design principles

1. Preserve authorial intent and human creative authority.
2. Support multiple legitimate story structures rather than enforcing one formula.
3. Keep characters, chronology, world rules, and knowledge state traceable.
4. Never fabricate rights clearance, research provenance, authorship, or approval.
5. Create original expression and flag plagiarism or excessive similarity risk.
6. Treat real-person portrayals, sensitive material, and production safety with appropriate escalation.
7. Preserve version history, notes, continuity, and change impact.
8. Fail closed when material rights, safety, provenance, or review is incomplete.
9. Keep submission, production, credits, and external distribution under qualified human control.

## Scope statement

F132 demonstrates a governed multi-agent architecture for screenwriting decision support and creative development. It combines specialized story, structure, character, continuity, and review agents with deterministic beat, scene, character, continuity, and review tools, observability, held-out evaluation, and fail-closed governance while preserving strict human authority over authorship, rights, production, submission, and distribution.

Author: Mahsa Keikha
