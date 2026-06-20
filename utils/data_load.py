from datasets import load_dataset
import json, random
from collections import defaultdict


CATEGORIES = {
    "Exclusivity": "exclusivity",
    "Non-Compete": "non_compete",
    "Anti-Assignment": "anti_assignment",
    "Cap On Liability": "liability_cap",
    "Insurance": "insurance_required",
    "Audit Rights": "audit_rights",
    "Governing Law": "governing_law",
    "Minimum Commitment": "minimum_commitment",
}

def main():
    ds = load_dataset("theatticusproject/cuad-qa", split="train", trust_remote_code=True)

    by_label = defaultdict(list)

    for row in ds:
        q = row["question"]
        cat = q.split('"')[1] if '"' in q else None
        if cat not in CATEGORIES:
            continue
        for span in row["answers"]["text"]:
            span = " ".join(span.split())
            if 150 <= len(span) <= 1500: #capturing only meaningful content(should be long enough)?
                by_label[CATEGORIES[cat]].append(span)

    random.seed(7)
    train, test = [], []
    PER_CLASS = 120 # 100 Training + 20 Test pro Klasse

    for label, spans in by_label.items():
        random.shuffle(spans)
        picked = spans[:PER_CLASS]
        for i, text in enumerate(picked):
            item = {"text": text, "label": label}
            (test if i < 20 else train).append(item)

    random.shuffle(train); random.shuffle(test)
    for name, data in [("train", train), ("test", test)]:
        with open(f"clauses_{name}.jsonl", "w", encoding="utf-8") as f:
            for item in data:
                f.write(json.dumps(item) + "\n")
    print(f"Train: {len(train)}, Test: {len(test)}")
    return train, test 
