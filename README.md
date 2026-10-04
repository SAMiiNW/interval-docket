# Interval Docket

## Clerk's reconstruction

A timeline can look plausible while violating the one ordering fact that matters. Interval Docket does not ask validators for a narrative verdict. It asks for bounded date intervals and citations, then lets contract code test the chronology.

An owner opens a docket with named events and forward precedence constraints. A separate auditor supplies two to five sources from distinct origins. Validators fetch the sources and agree on the earliest and latest defensible ISO date for every event, the citation indexes, and every source digest. Each interval endpoint is stored as an ordinal day.

The docket closes in one of three ways:

```text
CONSISTENT  every required predecessor ends before its successor begins
UNRESOLVED  at least one pair overlaps, but none is reversed
IMPOSSIBLE  a required predecessor begins on or after its successor ends
```

Only forward edges are accepted, so the constraint graph is acyclic by construction. Missing citations, repeated source origins, incomplete event coverage, duplicate IDs, self-auditing, and replayed reconstruction are rejected.

## Reproduce the checks

Run `python -m pytest -q`, then run `genvm-lint check contracts/contract.py` with UTF-8 output enabled on Windows.

The dispatch log and board minutes are operator-created fixtures mirrored through two delivery hosts. Host separation tests retrieval behavior; it does not imply independent institutional authorship.
