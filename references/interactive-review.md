# Local sketch review

## Fast visual exploration before annotation

Use `assets/design-explorer.html` for phase 1. Copy it into the garment's local output folder and populate its `initial-state` JSON with a prepared `fashion-design-explorer-project`, `schemaVersion: 1`. Localize visible controls, status/error messages, view/category names, handoff text, and the HTML language tag to the designer's language; retain the validation, IDs, and export contract. Escape `<` as `\u003c` when embedding JSON in HTML. The blank template includes an explicitly labelled example neckline round; replace that example for the actual garment.

The project has `garment` (`id`, `name`, `baseRevision`), `brief` (label/value rows), `answers` (earlier question/option/answer records), `unresolved` (strings), `question` (`id`, `question`, `category`, exactly five `options` with stable `id`, `label`, `comment`, and `views`), `baseViews`, `selectedOptionId`, and `customAnswer`. View keys are front/side/back. All alternatives in a round have the same available view keys, with front required. Each view is a complete SVG snapshot; every alternative preserves the same recorded earlier choices. `category` is aesthetic, construction, or illustration. SVG snapshots have a finite viewBox and only the template's permitted basic geometry/text tags and attributes; no scripts, external URLs, styles, images, or foreignObject.

Show one unresolved decision per round. The five option cards display local SVG thumbnails, labels, and short designer comments; a choice immediately changes the current sketch. SVG viewBox units are visual coordinates, not garment millimetres. Earlier answers are read-only context. If the designer wants an earlier choice changed, record the request for the assistant to prepare a new coherent round rather than silently retaining incompatible alternatives.

Save/reopen an explorer project to retain the round, drawings, and selections. Export the selected SVG, PNG, and `fashion-design-choices` JSON (`schemaVersion: 1`) or copy the readable instructions into chat. Choices contain garment/revision, brief, earlier answers plus the current answer, unresolved items, and `needsRedraw`; they do not approve the design. For a custom answer, show the base sketch as pending redraw and disable drawing exports; choices still export the requested change. The assistant reads the answer and prepares the next round or clean revision. There is no automatic chat submission.

To continue into the existing annotation form, load the explorer's PNG for each corresponding view and set the same garment ID and revision. Explorer projects and choices are distinct formats; do not import them as version-1 annotation projects. The annotation format and its coordinate behavior remain unchanged.

Run `node scripts/check_explorer.mjs` for explorer identity, preserved choices, custom-request handling, malformed-input, and syntax checks. In a browser, also check keyboard selection, immediate preview, SVG sanitization, and SVG/PNG export agreement. Prepared projects must validate fully before replacing the current session.

Use `assets/annotation-review.html` as a reusable standalone form. It runs without an account, network service, or build step. The designer guides the design; the form records requests and never generates or approves construction on its own.

## Prepare a session

Copy the template into the garment output folder. Its `initial-state` JSON script accepts a version-1 project object. Embed raster images as data URLs for a self-contained review, or let the designer load them through the form. Include a stable garment ID/name, base revision, and available front/side/back views; use only the actual reference images for that garment.

Optional questions contain `id`, `question`, and exactly five options with stable `id`/`label`. The form adds a custom-answer field. Populate only unresolved taste decisions; leave unanswered choices unset. Default interface language is Norwegian; adapt visible labels if requested.

The template defines `fashion-review-project` for saved sessions and `fashion-review-feedback` for handoff, both `schemaVersion: 1`. Preserve the schema and validation in the template rather than inventing a different import format each time. Projects include original image data for reopening. Feedback contains garment/base revision, explicit decision, general instructions, answers, image dimensions/identity, and numbered annotations with normalized original-image coordinates and instructions. It omits image data; attach the PNGs too.

## Place the form in the phased workflow

In phase 1, use questions and detail annotations to establish a direction and record open decisions. In phase 2, load the selected revision for critique, track each requested change, and present clean revised views for explicit acceptance. Keep the current phase and handoff items in the garment brief; retain the existing form schema.

An acceptance applies to the displayed concept revision. Unresolved design changes require another review; acceptance does not verify measurements, pattern construction, fit, or print scale. After acceptance, phase 3 lays out production measurements, patterns, and tailor instructions. A subsequent construction change that alters the design returns to phase 2 and marks affected production sheets as needing revision.

## Review loop

1. Ask short Q&A in chat or load questions into the form.
2. Let the designer add numbered pins, arrows, freehand marks, or text. Every mark has a matching editable instruction. Zooming changes only the display, never saved coordinates.
3. Export the annotated PNG for each marked view and the feedback JSON. “Copy instructions” provides a readable chat handoff. “Save project” preserves the original images and review for later.
4. The designer attaches exports or pastes instructions into this chat. There is no automatic chat-submit integration. Do not claim one merely because the form is open beside the conversation.
5. Read both the markings and instructions. Verify the garment, base revision, and original-image identity against the active brief before editing. A stale review must be reconciled explicitly; do not transfer coordinates blindly to a different image.
6. Generate a clean revised sketch and report which requests it incorporates. Keep previous versions. An approval applies to the displayed base revision; pending change requests require another review before freezing the revised design.

Browser coordinates and raster pixels are visual locations, not garment millimetres. A request such as “strap 20 mm” is a designer dimension to carry into the brief and later drafting; do not calculate body dimensions from the sketch.

## Local opening and checks

Open the prepared HTML in a supported artifact/browser panel. If file preview is unsupported, serve only the garment review folder over localhost and open that URL in the in-app browser. Never require CorelDRAW or deploy the form externally to run a review.

If the in-app browser does not expose normal file downloads, the bundled `scripts/serve_review.py <review-folder> --port 8766` provides a local-only save route. Add `<meta name="local-export" content="enabled">` to the prepared session HTML (not the reusable standalone template), and open its localhost URL. Exports are written to that folder's `exports` subfolder without overwriting existing files. The route requires same-origin requests and the review header, accepts only bounded PNG, safe basic SVG, and supported review/explorer JSON exports, and has no external destination. Attach the saved files to chat manually. A successful server response, not an attempted browser click, establishes that a file was saved.

Check a mark at fit view and at zoom, edit its instruction, undo/restore a mark, and export/reopen a project. Confirm the JSON/PNG retain the original image size, view, garment, revision, and annotation IDs. Imported strings must be rendered as text, and imported projects must pass the template's validation before replacing the current review.

Run `node scripts/check_review.mjs` for the template's coordinate, round-trip, feedback identity, input-validation, and syntax checks. The saved project preserves `nextAnnotationId` so later marks do not reuse deleted numbers.
