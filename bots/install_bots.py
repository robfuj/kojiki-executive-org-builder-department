#!/usr/bin/env python3
"""On-demand bot installer ( sub-functions).

Usage:
 python3 install_bots.py # install ALL candidate bots
 python3 install_bots.py brand growth # install only the named slugs

Each installed bot is a child decision system under bots/<slug>/ with README.md,
AGENT.md, schema/ (mirror of 00-kojiki-ontology), data/example.json, tools/validate.py.
It registers under the parent department's group_id so it can hand off to siblings.
Stdlib only.
"""
import json, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE) # the line repo
ONT_SCHEMA = os.path.join(ROOT, "..", "00-kojiki-ontology", "schemas")

DATE = __import__("datetime").date.today().isoformat()

def slugify(s):
 import re
 return re.sub(r"[^a-z0-9]+", "-", s.lower().strip()).strip("-")

with open(os.path.join(HERE, "manifest.json")) as f:
 manifest = json.load(f)

ALL = {b["slug"]: b for b in manifest["bots"]}
choose = [a for a in sys.argv[1:] if a]
slugs = choose if choose else list(ALL.keys())

# templates ---------------------------------------------------------------
def readme_md(b, parent_title, parent_key, parent_url):
 return ("# Bot \u2014 {sub}\n\n"
 "A sub-function bot of the **{parent}** decision system.\n\n"
 "## Parent\n[`{key}`]({url}) \u2014 part of the Kojiki Decision System.\n\n"
 "## What it does\nPerforms the **{sub}** sub-function as a decision system: "
 "receives its slice of parent inputs, decides within scope, emits evidence/outcomes, "
 "learns via the canonical Learning Ledger, and hands off cross-scope work to siblings.\n\n"
 "## Orientation\nOn first run, execute the Kojiki Orientation Protocol, then scope to "
 "the parent department context.\n\n"
 "## Schemas (mirror of 00-kojiki-ontology)\n- `schema/learning-ledger.json`\n"
 "- `schema/decision-object.json`\n- `schema/orientation.json`\n").format(
 sub=b["sub_function"], parent=parent_title, key=parent_key, url=parent_url)

def agent_md(b, parent_title, titles):
 return ("# AGENT.md \u2014 {sub} bot\n\n"
 "Entry point for the **{sub}** bot (sub-function of **{parent}**).\n\n"
 "## Kojiki Orientation Protocol (first-run)\n"
 "1. Name + function\n2. Industry / sector (triggers research)\n"
 "3. Jurisdiction (country / region / regulatory)\n"
 "4. Geography + business model\n5. Sibling registration under parent group_id\n\n"
 "## Scope\nSub-function: **{sub}** within **{parent}**.\n"
 "Typical human titles: {titles}.\n\n"
 "## Function prompt\nYou are the **{sub}** bot inside the {parent} decision system. "
 "Act as a decision system: state \u2192 diagnose \u2192 thesis \u2192 decide \u2192 act "
 "\u2192 expected vs actual \u2192 learn. Hand off cross-scope decisions via the Handoff Standard.\n").format(
 sub=b["sub_function"], parent=parent_title, titles=", ".join(titles))

def stub(b, parent_title, parent_key):
 return {
 "decision_object": {
 "decision_id": "{k}-{s}-001".format(k=parent_key, s=b["slug"]),
 "decision_name": b["sub_function"] + " decision (stub)",
 "owning_function": parent_title, "decision_owner_role": b["sub_function"],
 "trigger_condition": "Parent department routes a " + b["sub_function"] + " decision to this bot",
 "current_state": "", "required_inputs": [], "evidence_threshold": "",
 "available_options": [], "decision_criteria": "", "constraints": "",
 "risk_level": "medium", "delegation_level": "Execute",
 "escalation_conditions": "", "expected_outcome": "", "verification_method": "",
 "actual_outcome": "", "learning_extracted": "", "rule_version": "", "last_reviewed": DATE,
 "ledger": {"case": "", "decision": "", "assumption": "", "action": "",
 "expected_result": "", "actual_result": "", "variance": "",
 "cause": "", "learning": "", "rule_update": ""},
 },
 "installed_by": "bots/install_bots.py",
 }

# locate validate.py + schemas to mirror
validate_src = os.path.join(ROOT, "tools", "validate.py")
# parent repo title/key
parent_key = manifest.get("department", os.path.basename(ROOT))
parent_title = parent_key.replace("-", " ").title()

for slug in slugs:
 if slug not in ALL:
 print("skip (unknown slug): " + slug); continue
 b = ALL[slug]
 bd = os.path.join(HERE, slug)
 os.makedirs(os.path.join(bd, "schema"), exist_ok=True)
 os.makedirs(os.path.join(bd, "data"), exist_ok=True)
 os.makedirs(os.path.join(bd, "tools"), exist_ok=True)
 with open(os.path.join(bd, "README.md"), "w") as f: f.write(readme_md(b, parent_title, parent_key, "https://github.com/robfuj/" + slugify(parent_key)))
 with open(os.path.join(bd, "AGENT.md"), "w") as f: f.write(agent_md(b, parent_title, b["titles"]))
 for sf in ["learning-ledger.json", "decision-object.json", "orientation.json"]:
 src = os.path.join(ONT_SCHEMA, sf)
 if os.path.isfile(src): shutil.copy(src, os.path.join(bd, "schema", sf))
 with open(os.path.join(bd, "data", "example.json"), "w") as f:
 json.dump(stub(b, parent_title, parent_key), f, indent=2)
 if os.path.isfile(validate_src): shutil.copy(validate_src, os.path.join(bd, "tools", "validate.py"))
 # register in department handoffs registry
 reg = os.path.join(ROOT, "handoffs", "registry.json")
 os.makedirs(os.path.dirname(reg), exist_ok=True)
 data = []
 if os.path.isfile(reg):
 try: data = json.load(open(reg))
 except Exception: data = []
 data.append({"slug": slug, "sub_function": b["sub_function"],
 "group_id": parent_key, "registered_at": DATE})
 with open(reg, "w") as f: json.dump(data, f, indent=2)
 print("installed bot: " + slug)

print("done. installed " + str(len([s for s in slugs if s in ALL])) + " bot(s).")
