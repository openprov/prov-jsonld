# PROV-JSONLD 2026-09-12: updates from 2024-08-25

- `context.jsonld`: term `Bundle` → `prov:Bundle` added. A bundle's mandatory
  `"@type": "Bundle"` expanded to a document-relative IRI, not `prov:Bundle`.
  [openprov/prov-jsonld#5](https://github.com/openprov/prov-jsonld/issues/5).

- `schema.json`: the `@type` pattern of every statement, bundle and document
  anchored, `"Bundle"` → `"^Bundle$"` (19 patterns). Unanchored, any string
  containing the class name validated (`prov:Bundle`, `MyBundle`, `Bundles`).
  Consequence: `prov:`-prefixed types of the 2020 dialect (top-level
  `primer.jsonld` → `2020-03-23/`) no longer validate.

- `context.jsonld`: term `Document` → `provext:Document` added. A document's
  `"@type": "Document"` (required by 4.19, optional in the schema) expanded to
  a document-relative IRI. With the term it expands to `provext:Document`, on
  a blank node whose named graph holds the statements: a document has no
  identifier in PROV-N and no class in PROV-O, so the schema keeps `@id` out.
  [openprov/prov-jsonld#6](https://github.com/openprov/prov-jsonld/issues/6).

- `provext.ttl`: class `:Document` added, with a comment: the housekeeping
  construct holding statements and bundles, no PROV-DM/PROV-O counterpart.
  [openprov/prov-jsonld#6](https://github.com/openprov/prov-jsonld/issues/6).
