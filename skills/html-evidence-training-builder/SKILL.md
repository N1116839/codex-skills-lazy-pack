---
name: html-evidence-training-builder
description: Build or revise traceable HTML training databases and internal learning pages from user-provided source folders. Use when the user provides SOP/WI/FR, deck, spreadsheet, or document sources and asks for an HTML training page, GDP database, searchable knowledge base, learner UI, source-backed answers, image2/imagegen visual planning, icon/background generation, or interactive visualizations. Enforce source traceability, no invented company facts, and Firestore/database synchronization when requested.
---

# HTML Evidence Training Builder

## Core Rules

1. Treat the user's source folder as the authority for company practices.
2. Do not invent company facts, periods, systems, thresholds, warehouses, forms, or retention rules.
3. Every answer or training statement must trace back to a source file, page section, SOP/WI/FR number, form number, or clearly marked external law source.
4. When the same fact appears in several pages, fix it everywhere in one pass.
5. If international law, Taiwan law, and company practice conflict, surface the conflict and ask whether to revise company material.
6. If source files have repeated years or versions, prefer the newest confirmed source and record the version assumption.
7. Separate text correction from visual enhancement: finish source-backed wording first, then do interaction and image work.

## Workflow

1. Inventory the source folder.
   - Count source files by type and location.
   - Exclude build outputs, previews, `.git`, generated screenshots, and temporary files unless the user says otherwise.
   - Confirm the searchable database has one or more records for every source file.

2. Extract source text.
   - Extract DOCX/XLSX/PPTX/HTML/MD where possible.
   - Preserve source path, file name, document code, chunk number, and extracted text.
   - If extraction fails, still create a file-index record with the path and failure note.

3. Build searchable records.
   - Required fields: `topic`, `keywords[]`, `international`, `taiwan`, `xinshing`, `sop_ref[]`, `sourceType`, `file`, `chunk`.
   - For company records, put extracted source text in `xinshing`; do not summarize into claims unless the source supports them.
   - Add short keywords as well as long phrases.
   - Keep correction records for known traps, such as removed cold-chain content or wrong system assumptions.

4. Fill legal context only when needed.
   - If international or Taiwan law is missing and needed for the UI, search official sources only.
   - Prefer PIC/S, Taiwan FDA / Ministry of Health and Welfare, and official law databases.
   - Cite the source URL in the record or page note.

5. Update the HTML.
   - Search Firestore/database first, then local fallback.
   - Search across topic, keywords, source text, source path, and SOP references.
   - Return multiple relevant results, not a single brittle answer.
   - Show source file and SOP/form reference near the answer.

6. Visual planning after text is stable.
   - Decide which pages need image2/imagegen background art.
   - Decide which controls need flat icons; generate transparent icons only after confirming the page purpose.
   - Propose interactive sections before generating them: word cloud, tabs, accordion, drag/slide, checklist, sortable cards, timeline, or modal.
   - Use visualizations only where they clarify the learning task.

7. Validate.
   - Run JavaScript syntax checks for HTML.
   - Spot-check key queries the user named.
   - Read back database records after upload.
   - Update project handoff notes with what changed and what still needs review.

## Required Caution

- Do not upload source-derived data to Firestore, GitHub, or public hosting unless the user explicitly confirms the destination and scope.
- Do not overwrite the only PPT file.
- Do not create new public URLs for mobile fixes; update the existing route or file.

