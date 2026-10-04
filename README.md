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

## Filed on StudioNet

Contract [`0x37350A86821678F8eA3623D2b56fd5E107DF2c5f`](https://explorer-studio.genlayer.com/address/0x37350A86821678F8eA3623D2b56fd5E107DF2c5f) was deployed in transaction [`0x7580799e00b428cd140dc05bab149d36aa49d02a6abfe667a5b340a11aa0e14a`](https://explorer-studio.genlayer.com/transactions/0x7580799e00b428cd140dc05bab149d36aa49d02a6abfe667a5b340a11aa0e14a).

The live reconstruction transaction [`0x260e86b08044379ee6248221ebcfdae763cd184e59e8a167b90a9da28f05b298`](https://explorer-studio.genlayer.com/transactions/0x260e86b08044379ee6248221ebcfdae763cd184e59e8a167b90a9da28f05b298) stored three exact event days with citations to both sources and closed docket `DISPATCH-1791076325` as `CONSISTENT`.

Deployed source SHA-256 `2db8562c7fad39f1348fb37ddba84470ded2b5228be27aa233d1a431a89753bc` matches the reviewed repository contract.
