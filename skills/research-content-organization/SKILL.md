---
name: research-content-organization
description: Read and consolidate project research materials by actual content before classification. Use whenever a user says 資料整理、整理資料、資料分類、研究整理、清理暫存檔, or asks to organize historical project files, evidence, notes, captures, datasets, scripts, or source archives. Build topic-based, traceable organization; distinguish completed, unfinished, verified evidence, pending analysis, obsolete paths, and external references; never classify only by filename or delete raw evidence without confirmation.
---

# 內容導向資料整理

## Outcome

建立可追溯的主題導覽，使後續工作先找到既有證據與結論，不會因檔名、日期或「暫存」字樣重複解析或誤刪資料。

## 1. Establish scope and authority

- Identify the authoritative project root, any workspace copies, and the current source of truth. Do not merge same-named files across roots without checking content.
- Read the project instructions, current work note, existing source index, inventory, and known-status document before reorganizing.
- Preserve user data. Treat agent-prefixed or `_暫存` names as candidates for review only, never as automatic deletion authority.
- If scope is ambiguous, classify and index first; do not move, rename, or delete.

## 2. Inventory before changing files

Create or update the project’s existing inventory/index rather than creating parallel conclusion documents. Record each artifact’s path, type, size, source location, existing links, and preliminary topic.

Use filename/path only to form a review queue. Mark its link confidence as preliminary; do not treat it as content review.

## 3. Read actual content in batches

Read each reviewable item’s content before final classification:

- Notes/reports: purpose, date, stated status, findings, blockers, and supersession statements.
- CSV/JSON: schema, record count, representative rows, source fields, and whether it is raw or derived.
- Code/scripts: inputs, outputs, side effects, target systems, and whether the route is current, experimental, or retired.
- Captures/ETL/pcap/memory snapshots/archives: metadata, packet or record presence, source chain, and reproducibility. Do not delete merely because they are large or temporary.

For large data, read metadata plus representative records and use targeted searches. Record `structure_read` only when the file cannot reasonably be read directly; never call it `content_read`.

## 4. Classify by subject and relationship

Use a stable topic structure adapted to the project. Typical topics:

1. Entry/login/gateway
2. Transport/session/protocol
3. Identity, creation, selection, persistence
4. Services, ports, infrastructure
5. Scene, map, NPC, task, combat, skills, inventory/rewards
6. Source data, rules, schemas, assets
7. Captures, observed operations, test evidence
8. Static analysis, memory, reverse engineering
9. Implementations, migration paths, retired experiments
10. Governance, status, inventories, decisions
11. External references and unrelated comparison environments

Place connected facts together. For example, an interaction chain such as player → NPC → dialogue → task → reward belongs to one gameplay relationship, while its packet capture remains linked as evidence under captures and its source table remains linked under data rules.

## 5. Label evidence state and disposition

For every reviewed item, record all four fields in the existing queue or ledger:

| Field | Required values / intent |
| --- | --- |
| ContentReadStatus | `content_read`, `structure_read`, or `not_read` |
| Topic | one primary subject; add links for secondary subjects |
| EvidenceState | `verified`, `obtained_pending_analysis`, `inference_pending_validation`, `not_obtained`, `historical` |
| Disposition | `retain_current_reference`, `retain_evidence`, `retain_evidence_tool`, `retain_derived_index`, `historical_reference`, `archived_rejected_path`, `retain_external_reference`, or `delete_candidate` |

Maintain a concise content basis: what the item actually contains and why its status/disposition was chosen. Date-based claims never override a newer explicitly authoritative status document.

## 6. Handle duplicates and cleanup safely

A file is a deletion candidate only if content review proves one of these:

- zero-byte or failed output with no evidence value;
- reproducible derivative fully replaced by a verified equivalent;
- exact duplicate with a retained canonical path;
- obsolete log/script that conflicts with the active route and has no unique evidence.

Before deletion, list absolute paths, sizes, reason, and retained replacement/source. Obtain the authority required by project rules or the user. Never delete raw captures with packets, ETL, source datasets, unique snapshots, original source files, or a tool needed to reproduce a conclusion solely because its name contains `_暫存`.

## 7. Write back without parallel conclusions

- Update the existing inventory/review queue with content status, topic, evidence state, disposition, and basis.
- Update the existing project work note with material decisions, verified completion, unresolved work, and next slice.
- Update the existing source index for external/original source locations.
- Update the established research database/topic documents, if present, using their required fixed structure. Do not create `_new`, `_final`, date-parallel dashboards, or duplicate summary files.

## 8. Validate and report

Before declaring the organization pass complete, verify:

- no reviewed row lacks a content status, topic, basis, or disposition;
- all current-status claims point to the authoritative current record;
- retired routes and external references are clearly separated from active work;
- no raw evidence was deleted without a recorded replacement and authorization.

Report the number actually content-read, any structure-only reviews, topic totals, deletion actions, and the boundary of work not yet manually interpreted. Never claim an entire archive was manually read when only an indexed subset was reviewed.