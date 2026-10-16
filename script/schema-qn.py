#!/usr/bin/env python3
"""<version>/schema-qn.json: <version>/schema.json with the syntax of a qualified name enforced.

JSON Schema (draft-07) has no override: schema.json refers to its own #/definitions/QualifiedName, so a schema that
referenced it could not replace that one definition. The variant is therefore a copy, generated from schema.json and
differing from it in exactly three places:

  - QualifiedName's pattern: PROV-N's QUALIFIED_NAME (https://www.w3.org/TR/prov-n/#prod-QUALIFIED_NAME) restricted
    to ASCII, where schema.json accepts any string after an optional prefix;
  - QualifiedName's $comment, which says so;
  - the $id, https://openprovenance.org/prov-jsonld/schema-<version>-qn.json.

The edit is textual, so the rest of the file is schema.json byte for byte. --check regenerates in memory and fails
unless the existing schema-qn.json is exactly what this script writes.

Usage: schema-qn.py [--check] <version-directory> ...
"""
import json
import os
import sys

SPEC_ID = "https://openprovenance.org/prov-jsonld/schema.json"

# PROV-N's productions, after SPARQL's, with PN_CHARS_BASE restricted to the ASCII letters.
PN_PREFIX = r"[A-Za-z](?:[A-Za-z0-9_.-]*[A-Za-z0-9_-])?"     # PN_CHARS_BASE ((PN_CHARS | '.')* PN_CHARS)?
PN_CHARS_OTHERS = r"[/@~&+*?#$!]|%[0-9A-Fa-f]{2}|\\[='(),\-:;\[\].]"   # the others, PERCENT, PN_CHARS_ESC
PN_LOCAL = (rf"(?:[A-Za-z0-9_]|{PN_CHARS_OTHERS})"             # (PN_CHARS_U | [0-9] | PN_CHARS_OTHERS)
            rf"(?:(?:[A-Za-z0-9_.-]|{PN_CHARS_OTHERS})*"       # ((PN_CHARS | '.' | PN_CHARS_OTHERS)*
            rf"(?:[A-Za-z0-9_-]|{PN_CHARS_OTHERS}))?")         #  (PN_CHARS | PN_CHARS_OTHERS))?
QUALIFIED_NAME = rf"^(?:(?:{PN_PREFIX}:)?{PN_LOCAL}|{PN_PREFIX}:)$"   # (PN_PREFIX ':')? PN_LOCAL | PN_PREFIX ':'

COMMENT = ("A qualified name follows the PROV-N syntax of QUALIFIED_NAME (https://www.w3.org/TR/prov-n/#prod-QUALIFIED_NAME), "
           "restricted to ASCII: letters A-Z and a-z only, where PROV-N admits the Unicode ranges of SPARQL's PN_CHARS_BASE. "
           "This variant of the {version} schema enforces it; schema.json does not.")


def jstr(s):
    return json.dumps(s, ensure_ascii=False)


def replace_once(text, old, new, what):
    if text.count(old) != 1:
        raise SystemExit(f"schema-qn: {what} found {text.count(old)} times, expected once")
    return text.replace(old, new)


def generate(directory):
    version = os.path.basename(os.path.normpath(directory))
    source = open(os.path.join(directory, "schema.json"), encoding="utf-8").read()
    spec = json.loads(source)
    if spec.get("$id") != SPEC_ID:
        raise SystemExit(f"schema-qn: {directory}/schema.json has $id {spec.get('$id')}, expected {SPEC_ID}")
    qname = spec["definitions"]["QualifiedName"]
    text = replace_once(source, jstr(qname["pattern"]), jstr(QUALIFIED_NAME), "QualifiedName's pattern")
    comment = COMMENT.format(version=version)
    if "$comment" in qname:
        text = replace_once(text, jstr(qname["$comment"]), jstr(comment), "QualifiedName's $comment")
    else:
        text = replace_once(text, '"pattern": ' + jstr(QUALIFIED_NAME), '"$comment": ' + jstr(comment) + ', "pattern": ' + jstr(QUALIFIED_NAME), "QualifiedName's pattern")
    qn_id = f"https://openprovenance.org/prov-jsonld/schema-{version}-qn.json"
    text = replace_once(text, '"$id": ' + jstr(SPEC_ID), '"$id": ' + jstr(qn_id), "the $id")

    # the three places, and nothing else
    variant = json.loads(text)
    expected = json.loads(source)
    expected["$id"] = qn_id
    expected["definitions"]["QualifiedName"]["pattern"] = QUALIFIED_NAME
    expected["definitions"]["QualifiedName"]["$comment"] = comment
    assert variant == expected, directory
    return text


def main(args):
    check = "--check" in args
    directories = [a for a in args if a != "--check"]
    if not directories:
        raise SystemExit(__doc__)
    status = 0
    for directory in directories:
        text = generate(directory)
        target = os.path.join(directory, "schema-qn.json")
        if check:
            current = open(target, encoding="utf-8").read() if os.path.exists(target) else None
            if current == text:
                print(f"{target}: up to date")
            else:
                print(f"{target}: {'missing' if current is None else 'differs from what schema-qn.py generates'}")
                status = 1
        else:
            with open(target, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Written: {target}")
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
