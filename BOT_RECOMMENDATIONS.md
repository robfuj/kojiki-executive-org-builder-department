# Bot Recommendations (from org-structure.json)

After orientation + research, this agent emits `org-structure.json` (template in
`templates/`). Each instantiated department carries `recommended_bots` — the docx S5
sub-function slugs that org needs.

`recommend_bots.py` converts that into install commands:
```bash
python3 recommend_bots.py org-structure.json
```
Each printed command runs `install_bots.py` inside the relevant department repo. The
department owns its bot decisions; the Org Builder only recommends based on research.

Note: a department can also decide its own bots without this agent — see that repo's
`AGENT.md` ("Instantiate your working bots"). 21 is optional cross-org orchestration.
