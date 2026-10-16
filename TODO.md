# TODO

## Specification document: changes and their dates

The specification (`index.html` → `2024-08-25`) still describes the W3C member submission. The schema and context
have moved on (`2026-09-12`, `2026-10-14`), and the document does not say so.

1. Restructure the document so that each change is explicit, with the version (date) that introduced it, rather
   than silently rewriting the 2024-08-25 text.
2. Then document the changes, each against its version:
   - `2026-09-12`: the `Bundle` and `Document` terms in the context, the `provext:Document` class, the anchored
     `@type` patterns in the schema (#5, #6).
   - `2026-10-14` (#7): Section 4.1 — a qualified-name value of an attribute is written as a node reference,
     `{"@id": "ex:shed"}`; a bare string is a qualified name under `type`, `location` and `role` (coerced to `@id`
     by the context) and an `xsd:string` under any other attribute (`ArrayOfValues` / `ArrayOfStringValues`);
     a qualified name is expected to follow PROV-N's `QUALIFIED_NAME`, which the schema does not enforce.
   - Example 1 and `short-primer.jsonld`: an attribute with a qualified-name value (#7, item 3).
3. Settle the name of the node-reference definition with #3 (`NodeReference` there, `node_reference` in
   `2026-10-14`).
