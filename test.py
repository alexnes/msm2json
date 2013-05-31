#!/usr/bin/env python
# -*- coding: utf-8 -*-

from globals_description import description

props = {}
for g in description:
	for p in description[g]["prop"]:
		if props.get(p) == None: props[p] = []
		props[p].append(g)
for p in sorted(props.keys()):
	print "%s =>\t" % (p),
	for g in sorted(props[p]):
		print g + " ",
	print