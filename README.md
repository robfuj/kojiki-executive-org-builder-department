# 21 — Executive Org Builder

> Part of the **Hermes Organizational Decision System**. This repo is the
> **Executive Org Builder** line. It references the shared ontology in
> [`00-kojiki-ontology`](https://github.com/hermes-ios/00-kojiki-ontology) for the
> canonical schemas, taxonomy, decision-rights, and handoff standards.

## Primary question
> Given this organization's industry, jurisdiction, and research, which departments should exist and what should each own?

## Purpose
A meta-Executive agent: runs orientation + initial field research, then derives and proposes the organization's departmental structure (a subset of the 20 canonical lines) with charters, decision rights, and dependencies — so the org is built from evidence, not an org chart.

## Sub-functions
Orientation, Industry Research, Jurisdiction/Regulatory Research, Capability Gap Analysis, Department Design, Charter Authoring, Decision-Rights Assignment, Dependency Mapping

## Typical roles
Chief Executive Agent, Strategy Agent, Organization Design Agent

## Inputs
Orientation answers (name, function, industry, country/regime, geography, business model); research findings on the field, competitors, regulations, and standard operating model.

## Outputs
org-structure.json (department list + charters + decision rights + dependencies); per-department charter files; a recommended install manifest for 22-decision-system-installer.

## Learning focus
Which department designs matched reality; which capabilities were missing/duplicated; which charters needed revision after operations began.

## Operating tree
```text
ORIENTATION →
    INDUSTRY RESEARCH →
    JURISDICTION RESEARCH →
    CAPABILITY NEEDS →
    LINE MAPPING →
    GAP / DUPLICATION ANALYSIS →
    DEPARTMENT DESIGN →
    CHARTER AUTHORING →
    DECISION-RIGHTS ASSIGNMENT →
    DEPENDENCY MAPPING →
    STRUCTURE PROPOSAL →
    INSTALL MANIFEST
```

## Decision states
```text
ORIENTING → RESEARCHING → MAPPING → DESIGNING → CHARTERING → RIGHTS-ASSIGNING → PROPOSED → INSTALLED → REVISED
```

## Decision outputs
`Instantiate · Defer · Merge · Split · Drop · Revise`

## Critical prompts (what this function thinks about)
> What industry/sector and jurisdiction apply?
> What capabilities must this org perform?
> Which canonical lines cover those capabilities?
> Which lines are unnecessary for this org?
> Which capabilities are missing from the 20 lines?
> Where are duplicated responsibilities?
> What decision rights does each department own?
> What are the cross-department dependencies?
> What evidence supports standing up each department?
> What would make us remove a department?

## Canonical record schema (docx Learning Ledger + Decision Object Fields)
Every decision in this line is recorded as:
- a **Decision Object** (docx S9) — see `schema/decision-object.json`
- a **Learning Ledger** entry (docx S7) — see `schema/learning-ledger.json`

and the agent must run the **Orientation Protocol** first (see `AGENT.md`).

## How to use
1. Read `AGENT.md` — the first-run Orientation Protocol.
2. Read `SCHEMA.md` — how this line maps to the universal schema.
3. Read `data/21-executive-org-builder.json` — the machine-readable spec.
4. See `data/example.json` — one fully worked decision (Decision Object + Ledger).
5. Use `decision-graph.mmd` — agent-decodable operating tree + state model.
6. Validate new records: `python3 tools/validate.py data/<name>.json`
