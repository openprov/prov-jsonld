# PROV-JSONLD 2026-10-14: updates from 2026-09-12

- `schema.json`: definition `node_reference` added, an object with `@id` (a
  `QualifiedName`) and nothing else, admitted as an attribute value. A
  qualified name under an extension property (`foaf:pastProject`) had no form
  a JSON-LD processor reads as an IRI: the context coerces `type`, `location`
  and `role` to `@id`, and a plain string under any other key is a literal.
  Written `{"@id": "ex:shed"}`, it expands to `http://example.org/shed`.
  [openprov/prov-jsonld#7](https://github.com/openprov/prov-jsonld/issues/7).

- `schema.json`: definition `ArrayOfStringValues` added (plain string, typed
  value, language string, node reference) for the attributes the context
  does not coerce: the extension properties (`^[A-Za-z0-9_]+:(.*)$`, 17
  pattern properties) and `value` (1). A plain string there is a string;
  `"Meeting at 10:30"` validates. `ArrayOfValues`, now with
  `node_reference`, stays on `type`, `location` and `role` (31), where a
  plain string is a qualified name. Both definitions say so in their
  `description`.
  [openprov/prov-jsonld#7](https://github.com/openprov/prov-jsonld/issues/7).

- `schema.json`: `QualifiedName` unchanged; a `$comment` says a qualified
  name is expected to follow PROV-N's `QUALIFIED_NAME`
  (https://www.w3.org/TR/prov-n/#prod-QUALIFIED_NAME), which its pattern does
  not enforce. Consequence: `ArrayOfValues` and `ArrayOfStringValues` accept
  the same values and differ in how a plain string is read.

- `context.jsonld`, `provext.ttl`: unchanged from 2026-09-12.
