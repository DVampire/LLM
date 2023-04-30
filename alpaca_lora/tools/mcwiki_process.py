import os
import sys
import pathlib
import json
import re

ROOT = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.append(ROOT)

def replace(text, replacements):
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

def filter_keys(text, keys):
    flag = False
    for key in keys:
        if key in text:
            flag = True
            break
    return flag

def main():
    path = os.path.join(ROOT, "datasets", "mcwiki.json")

    replacements = {
        "\u200c[Bedrock Edition only]": "",
        "\u200c[Java Edition only]": "",
        "\u200c[Pocket Edition only]":"",
        "\u200c[JE only]":"",
        "\u200c[BE only]":"",
        "\u200c[PlayStation Vita Edition only]":"",
        "[Bedrock Edition only]":"",
        "(Java Edition only)":"",
    }
    keys = {
        "Edition",
        "edition",
        "Java",
        "java",
    }

    outputs = []
    with open(path) as op:
        data = json.load(op)

        for item in data:
            output = item["output"]

            output = replace(output, replacements)
            output = output.encode('unicode_escape').decode('utf-8')

            if filter_keys(output, keys):
                continue

            outputs.append(output)

    outputs = set(outputs)
    for item in outputs:
        print(item)

    print(len(outputs))

    with open(os.path.join(ROOT, "datasets", "mcwiki_cleaned.json"), "w") as op:
        json.dump(list(outputs), op)

if __name__ == '__main__':
    main()