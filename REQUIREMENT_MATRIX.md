# Docket controls

| Control | Enforcement | Test | Status |
| --- | --- | --- | --- |
| Graph remains acyclic | forward-edge validation in `open_docket` | surface assertion | PASS |
| Auditor differs from owner | role check in `open_docket` | surface assertion | PASS |
| Evidence origins are distinct | normalized host check in `reconstruct` | surface assertion | PASS |
| Every event has interval and citation | `_reconstruct` | consensus and attribution test | PASS |
| Exact endpoints, citations, and digests reach consensus | comparative principle | exact field assertion | PASS |
| Consistent, overlapping, and reversed order differ | `chronology_state` | outcome and multi-edge tests | PASS |
| Reviewed source deployed and exercised on StudioNet | deployment evidence | added after network verification | UNVERIFIED |
