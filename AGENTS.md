✦︎✦︎✦︎ Meta Apollo Logos //

# AGENTS // SYNTAGMA

> **STATE //** active \~\~ **VIEW //** agent entry contract

This file is the canonical shared entry point for an AI or other worker entering Meta Apollo Logos // Post-Apollo. It is intentionally compact: the protocols live in Syntagma's OPERATE room; personal cognition and evidence remain with How I Think / Poioumenon, and technical truth remains in each owning project.

## AUTHORITY // FIRST RULE

**The user is final authority.**

An agent may inspect, analyze, compare, propose, document, test, and—when implementation has actually been authorized—make bounded changes.

Do not silently convert discussion into implementation.

Do not silently convert a proposal into a canonical decision.

Do not treat architectural exploration, brainstorming, diagnosis, or "what would you do?" as permission to mutate a live system.

## SCOPE // WORK ONLY WHERE THE TASK ACTUALLY IS

Before significant action, reconstruct enough state to know:

- what project or system is being discussed
- current architecture and ownership
- current branch / state / target
- immediate goal
- relevant upstream and downstream relationships
- concurrent work that may collide

Prefer the smallest coherent change that satisfies the approved goal.

Stop when the requested scope is complete. Do not recursively implement every future possibility discovered along the way.

## LOCAL MACHINE // ASK BEFORE WRITE

A connected local computer is a live operating environment, not merely another repository.

Reading, inspecting, and diagnosing may proceed when the task calls for them.

**Writing or mutating the local machine requires explicit user approval for that change.**

Planning is not approval.

A previous local-write approval does not automatically carry forward to a different change.

Explicit approval is especially required before:

- editing local files
- installing or removing packages
- changing system configuration
- moving or deleting files
- restarting or killing services
- reloading or restarting Quickshell
- changing Git worktree state with pull, reset, checkout, rebase, or similar operations

When local work is approved, preserve the user's current live state and avoid unrelated cleanup.

## GITHUB / REPOSITORIES

Repository history, branches, diffs, and rollback make GitHub work more recoverable than live-machine work.

When the user explicitly asks to fix, implement, land, or continue repository work, bounded repository changes may proceed under the established project workflow.

When the user is only discussing, designing, comparing, or planning, remain in that mode unless implementation is explicitly requested.

Re-check current branch/head/shared seams before writes when concurrent agents may be active.

## WORKING STYLE // COMMUNICATION

Do not infer global ignorance from one missing term, command, or conventional workflow.

Prefer the minimum sufficient explanation that preserves the important relationships.

Treat the user's metaphors as structural codecs unless the task requires literal interpretation. Do not flatten metaphor into literal mechanism.

Preserve semantic distinctions when the user is being precise, even if the surrounding language is casual.

For planning, think in families, dependencies, collision points, parallel work, bottlenecks, and rollback rather than forcing one giant total-order roadmap.

For debugging, prefer:

```text
what changed?
what was expected?
what actually happened?
what depends on it?
what old assumption could generate this?
what is the cheapest discriminating test?
what is the rollback?
```

Do not immediately patch symptoms when the underlying relationship is still unclear.

## POST-APOLLO // USE THE SYSTEM THAT EXISTS

Before inventing a new component, service, control, visual primitive, or workflow, inspect the relevant project for an existing one.

Preserve runtime-sensitive paths and established ownership boundaries.

When the user's Post-Apollo control surfaces already expose an operation, explain the **UI/menu path first**. Use CLI commands as fallback, diagnostics, automation, or when the UI does not expose the capability.

Distinguish clearly between:

- GitHub/repository state
- local working-tree state
- live Quickshell/runtime state
- Hospital coordination state

Do not claim these are synchronized unless verified.

## VERIFY // CLAIMS NEED EVIDENCE

Before declaring a significant change fixed, landed, verified, certified, or complete, check the evidence appropriate to that claim.

Report uncertainty plainly.

Preserve provenance and important decision history.

## DOCUMENTATION AUTHORITY // CHECK BEFORE WRITING RULES

This repository is **Syntagma (Σύνταγμα)**, the designated shared rules and AI/operator-interface authority. **How I Think / Poioumenon** retains the author's personal reasoning, narratives, evidence and archaeology; the umbrella Meta Apollo Logos repository retains family principles and repository design language. The old Syntagma workstream in Meta-Apollo-Logos-How-I-Think is preserved during link migration, not a second live rules authority. Never delete, silently sync, or bulk-migrate personal evidence or another worker's files.

Before adding a rule to any Meta Apollo project: read the [authority and provenance map](./ATLAS/SOURCE-MAP.md) and the [documentation placement / classification workflow](./OPERATE/POST-APOLLO-WORKING-GUIDE.md#documentation-ownership--placement). Follow the canonical source; link instead of copying. Preserve the operator's informal input and organize it on their behalf. Check active ownership/PRs before moving any file.

## DEEPER CONTEXT

Start with:

- [HOW-I-THINK-PUBLIC.md](https://github.com/kudokudo1/Meta-Apollo-Logos-How-I-Think/blob/main/HOW-I-THINK-PUBLIC.md) — current cognitive / communication map
- [OPERATE/WORKING-WITH-ME.md](./OPERATE/WORKING-WITH-ME.md) — compact collaboration behavior
- [OPERATE/AUTHORITY-AND-PERMISSIONS.md](./OPERATE/AUTHORITY-AND-PERMISSIONS.md) — actuation boundaries
- [OPERATE/DEBUGGING-AND-PLANNING.md](./OPERATE/DEBUGGING-AND-PLANNING.md) — problem-solving protocol
- [OPERATE/COMMAND-ENVIRONMENT.md](./OPERATE/COMMAND-ENVIRONMENT.md) — host / shell conventions
- [OPERATE/POST-APOLLO-WORKING-GUIDE.md](./OPERATE/POST-APOLLO-WORKING-GUIDE.md) — approved Post-Apollo development policy
- [OPERATE/POST-APOLLO-ICON-GRAMMAR.md](./OPERATE/POST-APOLLO-ICON-GRAMMAR.md) — operator-established glyph, relational color, range and independent glow grammar
- [OPERATE/CONTROL-SURFACES.md](./OPERATE/CONTROL-SURFACES.md) — UI-first operator routes and control-plane map
- [OPERATE/DESKTOP-LIFECYCLE.md](./OPERATE/DESKTOP-LIFECYCLE.md) — startup ownership, layered health, live-vs-source state, and restart boundaries
- [OPERATE/HOSPITAL-AGENT-PROTOCOL.md](./OPERATE/HOSPITAL-AGENT-PROTOCOL.md) — Hospital-compatible doctor / room / patient / assignment behavior
- [OPERATE/HOSPITAL-ORGANIZATION-PROTOCOL.md](./OPERATE/HOSPITAL-ORGANIZATION-PROTOCOL.md) — ten staff roles, Patient-level leadership, Teams, Proxy Doctor, delegation, context and succession
- [OPERATE/HOSPITAL-REPORT-PROTOCOL.md](./OPERATE/HOSPITAL-REPORT-PROTOCOL.md) — report timing, schema, evidence, completion, and handoff behavior
- [ATLAS/SOURCE-MAP.md](./ATLAS/SOURCE-MAP.md) — where these rules came from and which external sources remain canonical
- [How I Think archaeology](https://github.com/kudokudo1/Meta-Apollo-Logos-How-I-Think/tree/main/dump) — preserved original source when the compressed layer is insufficient

> **Use the skim layer first. Descend only when the task needs more context.**
