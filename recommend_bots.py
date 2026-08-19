#!/usr/bin/env python3
"""Turn an org-structure.json (emitted by 21-executive-org-builder) into bot-install
commands for each instantiated department. Stdlib only.

Usage:
 python3 recommend_bots.py org-structure.json
Reads each department with status 'instantiate' (and any recommended_bots), then prints
the `install_bots.py` command to run inside that department's repo. Departments own their
own bot decisions; this just translates the Org Builder's research into actions.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE) # the 21-executive-org-builder repo
LINES_DIR = os.path.dirname(REPO_ROOT) # sibling line repos live here

def slugify(s):
 import re
 return re.sub(r"[^a-z0-9]+", "-", s.lower().strip()).strip("-")

path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "org-structure.json")
with open(path) as f:
 struct = json.load(f)

print("# Bot install plan (from org-structure.json)")
print("# departments own their own bot decisions; run each command in that repo\n")
ran = 0
for dep in struct.get("departments", []):
 if dep.get("status") != "instantiate":
 continue
 key = dep["line_key"] # e.g. 15-legal
 bots = dep.get("recommended_bots") or struct.get("install_manifest", {}).get("recommended_bots", {}).get(key, [])
 if not bots:
 continue
 repo = os.path.join(LINES_DIR, key)
 print("# {key}: {sub}".format(key=key, sub=", ".join(bots)))
 print("cd {repo} && python3 bots/install_bots.py {bots}\n".format(
 repo=repo, bots=" ".join(bots)))
 ran += 1
if ran == 0:
 print("# (no recommended_bots found for instantiated departments)")
