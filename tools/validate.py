#!/usr/bin/env python3
"""Stdlib validator for records in this repo ( + S9). No third-party deps."""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

LEARNING_LEDGER = ["case","decision","assumption","action","expected_result","actual_result",
 "variance","cause","learning","rule_update"]
DECISION_OBJECT = ["decision_id","decision_name","owning_function","decision_owner_role",
 "trigger_condition","current_state","required_inputs","evidence_threshold",
 "available_options","decision_criteria","constraints","risk_level",
 "delegation_level","escalation_conditions","expected_outcome",
 "verification_method","actual_outcome","learning_extracted","rule_version","last_reviewed"]
RISK = ["low","medium","high","critical"]
RIGHTS = ["Own","Recommend","Consult","Execute","Approve","Escalate","Automate"]

def err(m): print("FAIL: "+m); return False

def validate_record(path):
    ok = True
    with open(path) as f: rec = json.load(f)
    do = rec.get("decision_object")
    ll = rec.get("learning_ledger")
    if not isinstance(do, dict): ok = err("missing decision_object"); do = {}
    if not isinstance(ll, dict): ok = err("missing learning_ledger"); ll = {}
    for fld in DECISION_OBJECT:
        if fld not in do: ok = err("decision_object missing: "+fld)
        if do.get("risk_level") not in RISK: ok = err("risk_level invalid: "+str(do.get("risk_level")))
        if do.get("delegation_level") not in RIGHTS: ok = err("delegation_level invalid: "+str(do.get("delegation_level")))
        if not isinstance(do.get("required_inputs"), list): ok = err("required_inputs must be a list")
        if not isinstance(do.get("available_options"), list) or not do["available_options"]: ok = err("available_options must be non-empty list")
        for fld in LEARNING_LEDGER:
            if fld not in ll: ok = err("learning_ledger missing: "+fld)
    return ok

def validate_spec(path):
    ok = True
    with open(path) as f: spec = json.load(f)
    for req in ["line","key","primary_question","purpose","operating_tree","decision_states","critical_prompts","decision_outputs"]:
        if req not in spec: ok = err("spec missing: "+req)
    if len(spec.get("operating_tree",[])) < 2: ok = err("operating_tree too short")
    return ok

def main():
    targets = sys.argv[1:] or [os.path.join(ROOT,"data",f) for f in os.listdir(os.path.join(ROOT,"data")) if f.endswith(".json")]
    all_ok = True
    for t in targets:
        print("== "+t)
        with open(t) as f: data = json.load(f)
        if "operating_tree" in data: all_ok &= validate_spec(t)
        else: all_ok &= validate_record(t)
    print("ALL VALID" if all_ok else "VALIDATION FAILED")
    sys.exit(0 if all_ok else 1)

if __name__ == "__main__":
    main()