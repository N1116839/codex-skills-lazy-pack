---
name: gas-targeted-fix
description: 精準修正 Google Apps Script 與一般程式碼。Use when the user asks in Traditional Chinese to fix code, such as "幫我修正程式碼", "修正程式", "改程式", "幫我改 GAS", "修正 Apps Script", "Google Sheets 自動化壞了", or asks for minimal, non-refactoring code changes. Preserve original logic, naming, comments, structure, and style unless the user explicitly requests broader changes.
---

# GAS Targeted Fix

Use Traditional Chinese by default.

## Core Rules

- Read and understand the existing code before editing.
- Preserve original behavior, naming style, formatting style, comments, architecture, and author intent.
- Make only the smallest change that satisfies the user's explicit request.
- Do not refactor, optimize, rename, reorganize, or modernize unrelated code.
- Do not delete comments or existing features unless the user explicitly asks.
- If a requested change would break existing behavior, explain the risk and choose the least invasive compatible adjustment.
- If the code is not Google Apps Script, still apply the same minimal-change rules, but do not assume GAS-specific services exist.

## Workflow

1. Review the provided code or project files and identify current behavior.
2. Identify the exact requested change and the smallest safe edit.
3. Check likely side effects before editing, especially trigger bindings, function names, sheet names, column positions, global variables, and external service calls.
4. Apply the change without rewriting unrelated sections.
5. Validate syntax and behavior as far as the local environment allows.
6. Report what changed, where it changed, and what validation was performed.

## Output Rules

- If the user pasted a complete GAS file or asks for a copy-paste answer, output one complete corrected `.gs` code block.
- If editing files in a local project, edit the files directly and summarize changed files and validation results.
- If only static validation was possible, say that clearly. Do not claim the script ran successfully in Apps Script unless it actually did.

## GAS-Specific Guardrails

- Do not rename functions unless required. GAS triggers, menus, buttons, web apps, and installable triggers may depend on exact names.
- Do not casually change global constants, sheet names, named ranges, property keys, trigger handlers, deployment entry points, or API payload shapes.
- When modifying Google Sheets logic, verify header rows, data start rows, and `getRange(row, column)` indexes to avoid off-by-one errors.
- Prefer preserving the existing read/write pattern. If performance is part of the user's issue, reduce repeated `getValue()`/`setValue()` calls only in the affected area.
- Add `try/catch` only around risky boundaries such as external APIs, spreadsheet writes, trigger entry points, file access, or user-facing flows. Do not swallow errors silently.
- Error handling should log useful context and preserve debuggability.
- If a change may require new OAuth scopes or reauthorization, mention it.
- Treat `SpreadsheetApp`, `DriveApp`, `UrlFetchApp`, `PropertiesService`, `LockService`, `Session`, and trigger behavior as GAS runtime features that may not be locally executable.

## Validation Checklist

- Confirm the edited code still has balanced braces, parentheses, and quotes.
- Confirm changed functions are still reachable from their original callers or triggers.
- Confirm no unrelated logic, comments, or UI text was removed.
- Confirm added code handles empty, missing, or malformed inputs when relevant.
- For local projects, run available tests, linters, type checks, or syntax checks when practical.
- For pasted GAS snippets, perform static review and clearly state any assumptions.
