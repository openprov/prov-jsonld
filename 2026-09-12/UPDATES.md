# PROV-JSONLD 2026-09-12: updates from 2024-08-25

- `context.jsonld`: term `Bundle` → `prov:Bundle` added. A bundle's mandatory
  `"@type": "Bundle"` expanded to a document-relative IRI, not `prov:Bundle`.
  [openprov/prov-jsonld#5](https://github.com/openprov/prov-jsonld/issues/5).

- `schema.json`: the `@type` pattern of every statement, bundle and document
  anchored, `"Bundle"` → `"^Bundle$"` (19 patterns). Unanchored, any string
  containing the class name validated (`prov:Bundle`, `MyBundle`, `Bundles`).
  Consequence: `prov:`-prefixed types of the 2020 dialect (top-level
  `primer.jsonld` → `2020-03-23/`) no longer validate.
