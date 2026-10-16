# PROV-JSONLD releases: one directory per version (2026-10-14/...), linked from the top level
# (schema-2026-10-14.json -> 2026-10-14/schema.json, schema.json -> the current one).
#
#   make qn VERSION=2026-10-14   <version>/schema-qn.json, the schema with the syntax of a qualified name
#                                enforced, generated from <version>/schema.json (script/schema-qn.py),
#                                and its top-level link schema-<version>-qn.json
#   make qn.check                every <version>/schema-qn.json is exactly what script/schema-qn.py generates
#                                from its schema.json

VERSION=2026-10-14
QN_VERSIONS=$(patsubst %/schema-qn.json,%,$(wildcard */schema-qn.json))

.PHONY: qn qn.check

qn:
	python3 script/schema-qn.py $(VERSION)
	ln -sfn $(VERSION)/schema-qn.json schema-$(VERSION)-qn.json

qn.check:
	python3 script/schema-qn.py --check $(QN_VERSIONS)
