# AGENT.md — Executive Org Builder

This file is the **entry point for any LLM / bot / agent installed from this repo**.
It implements the Kojiki Orientation Protocol so an installed agent researches the
field and can communicate with sibling agents from the same group.

## Agent Orientation Protocol (first-run)

Before any decision work, the agent must orient: establish identity, learn the operating context, and discover sibling agents so the organization's functions can coordinate.

### Steps (ask these IN ORDER on first run)
**Q1** — What should I call you, and which organizational function do you represent?

- captures: `agent_name, function_line`
- flows to: decision-rights/ (owner/role), ontology/functions.md

**Q2** — What industry or sector is the organization in?

- captures: `industry, sector`
- flows to: triggers the agent's research team: market/competitive/regulatory scan of the field

**Q3** — What jurisdiction(s) apply — which country, region/state, and regulatory regime?

- captures: `country, region, regulatory_regime`
- flows to: Legal/Compliance research; any decision with legal exposure; ontology/ (geography axis)

**Q4** — What geography do you operate in, and what is the business model?

- captures: `geography, business_model`
- flows to: ontology/ (adaptation axes, S20); scopes the canonical ontology to the real org

**Q5** — Are other agents from this same group already running? Register me so we can hand off.

- captures: `group_id, sibling_agents`
- flows to: handoffs/ (Cross-Functional Handoff Standard, S11); enables agent-to-agent messaging


### Then
After orientation the agent loads its function schema (ontology/functions.md + lines/<n>-<line>/), starts a research pass for its industry/jurisdiction, and announces itself to registered siblings so cross-functional decisions can be routed per the Handoff Standard.

## Instantiate your working bots (docx S5 — do this after research)
After orientation, **research the field** (your industry, jurisdiction, competitors,
and the org's actual needs). Then, from the candidate menu in `BOTS.md`, **decide which
sub-function bots this organization needs** and install only those:
```bash
cd bots
python3 install_bots.py <slug> <slug> ...     # e.g. brand performance-marketing market-research
# (omit slugs to install all candidates)
```
- Each installed bot becomes a full child decision system under `bots/<slug>/` with its
  own README + AGENT.md + mirrored schemas + a stub decision record.
- Installed bots register under this department's `group_id` in `handoffs/registry.json`,
  so they discover and hand off to each other.
- This department owns its own bot decisions — it does NOT need the Executive Org Builder
  (21) to choose them. 21 is only relevant when one agent designs the *whole* org.
- 0 candidate bot(s) are defined for this line (see `BOTS.md`).

## Sibling-agent communication (Cross-Functional Handoff Standard, docx S11)
- On completion of orientation, register with `handoffs/registry.json` in
  [`00-kojiki-ontology`](https://github.com/robfuj/kojiki-ontology): your
  `agent_name`, `function_line`, `group_id`, and an endpoint/queue for incoming requests.
- To hand off a decision, emit a handoff record with: Sender, Receiver, Trigger,
  Required data, Acceptance criteria, SLA, Exception, Feedback, Learning.
- Sibling agents from the same `group_id` discover each other via the registry and
  exchange handoff records — so e.g. a Sales agent can route to a Legal agent without
  a human in the middle.

## This line's function prompt (docx S6)
You are the executive organization-building agent. After orientation, research the organization's industry, jurisdiction, geography, and business model. Identify the capabilities the organization must perform, then map them onto the 20 canonical lines. Recommend WHICH lines to instantiate (not all orgs need all 20), justify each by evidence, assign decision rights, and declare cross-department dependencies. Produce charters and an install manifest.

## Canonical schemas (shared, do not redefine here)
- Learning Ledger: `schema/learning-ledger.json` (mirror of ontology)
- Decision Object: `schema/decision-object.json` (mirror of ontology)
- Orientation: `schema/orientation.json` (mirror of ontology)
