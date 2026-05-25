# HTML Training Deck Review Checklist

Use this checklist before final delivery.

## Content

- The learner-facing page does not show database setup instructions or private implementation notes.
- Inspection points are labeled as 稽查重點, not exam-question placeholders, unless the user explicitly wants exams.
- Each page has enough inspection points for practical training and does not stop at three generic bullets.
- SOP/document codes are clickable or otherwise traceable.
- SOP content shown in the page is summarized for training unless full publication is explicitly approved.
- The sidebar heading identifies the platform by name — no version labels, no description of app features.
- No "建議先確認可見性" or similar implementation-warning text appears in any modal or tooltip.

## GDP-Specific (新勝醫藥)

- All 8 departments are present: GDP權責人、管理藥師、品保、人事、倉管、採購、業務、文管.
- 人事 section covers DP22-01, DP24-01, DP25-01; FR24-01, FR24-02; ≥70 分合格; 保存5年.
- 跨部門責任矩陣 renders all columns and rows with 主辦/核准/協助/受查/提報/記錄/— values.
- Department flow diagrams cover the full operational sequence (not 3 generic bullets).
- 3-column swipe uses CSS scroll-snap; no floating overlay for standards content.

## Visual

- First viewport has a strong topic image and readable headline.
- Text is large enough in screenshots.
- Document-code buttons are centered and stable in size.
- Dense content is split into multiple sections/slides.
- At least one image2/imagegen asset is used when the user asks for rich visual learning.
- Swipe tab dots are visible and sync with the scroll position.

## Interaction

- Left navigation works.
- Mobile selector works if present.
- SOP modal opens and closes.
- Q&A form works locally (localStorage) or with Firestore; both modes fail gracefully.
- 3-column swipe panels re-initialize after section navigation (`initSwipePanels()` called in `showSection()`).

## Deployment

- Public GitHub Pages risk has been reviewed and user confirmed.
- Commit includes only web assets: HTML, assets/, .nojekyll — no PPT, DOCX, private notes, screenshots.
- `README_Codex接續.md` and second-brain project note updated with outputs and pending todos.
- A browser screenshot has been captured after final edits.
