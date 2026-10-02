---
name: streetwear-fashion-design
description: Guide adult fashion design step by step across womenswear, menswear, and unisex clothing, from fast visual choices and hand-drawn-style illustrations to annotated concept boards, revisions, and checked sewing-pattern packages. Use for developing garment ideas, choosing fashion illustration styles, or preparing tailor specifications.
---

# Interactive fashion design and sewing patterns

The user is the designer; act as their sketcher and tailor. Use this harness as the default workspace. Keep each garment's brief, images, and construction files together under a stable garment ID and revision; do not mix separate garments or use an unrelated repository as their output folder.

Separate **fashion aesthetic**, **garment construction**, and **illustration style**. Guide couture, classic tailoring, minimalist everyday wear, streetwear/utility, romantic/bohemian, vintage, avant-garde, and activewear across adult womenswear, menswear, and unisex designs. Adapt to the wearer and purpose; an illustrative croquis is not the wearer's measurement record. Read [illustration and board guidance](references/illustration-and-boards.md) when choosing a medium, developing a board, or preparing a Claude Design handoff.

## Phase 1 — Brief and fast visual exploration

1. Establish garment type, wearer, purpose, aesthetic, and constraints. Ask **one taste question at a time**, with **five meaningful visual alternatives plus a custom answer**, in the user's language. Do not invent filler alternatives for measurements or factual questions. Record question/option IDs and the actual answer so a later reply such as “2” cannot lose its meaning.
2. Start with simple line sketches. Prepare the [fast design explorer](assets/design-explorer.html) for the current garment and decision; read [the visual workflow](references/interactive-review.md) for its contract. Localize its visible controls, messages, view names, and HTML language tag to the designer's language along with the question. Its five SVG alternatives update locally without an image-generation call. Preserve earlier choices in every alternative, explain proportion, movement, and material tradeoffs, and show unresolved decisions. Selecting a custom request records it for assistant redraw; it does not synthesize new geometry in the browser.
3. Carry the selected sketch and answer into the next question in chat. Update the same brief and prepare the next round from established choices. The template's default neckline round is a sample, not a universal garment generator. If a decision cannot honestly be previsualized, show descriptive alternatives and mark the sketch pending redraw instead of pretending the preview incorporates it.
4. Establish silhouette, fabric, color, closures, pockets, trims, movement, signature, and exclusions; include simple detail studies when helpful. Record preliminary measurements with their source; finish production specifications in phase 3. Keep identity and relevant front/side/back details consistent. Do not impose photorealism, a gown silhouette, or watercolor on every garment.

**Handoff:** a named, versioned concept with detail studies, a recorded brief, and clearly identified open decisions. Move to critique when the designer has a direction to review. Sewing patterns and production sheets belong to phase 3.

## Phase 2 — Refined illustration, critique, and revisions

1. Offer five visual illustration choices: graphite pencil/shading; pen-and-ink croquis; watercolor with ink; marker/colored pencil; detailed couture mixed-media appearance. Adapt examples to the garment. Use available image-generation tools for refined raster artwork and edits; describe generated results as illustrations with a hand-drawn appearance. Preserve chosen design details and model identity; separately record any desired presentation-pose change. SVG style samples are quick indications, not finished watercolor artwork.
2. Develop an illustration sheet or concept board when useful. Compose editable HTML/SVG around generated images with separate readable text, numbered comments, palettes, proposed fabrics/trims, and detail crops. Clearly label proposed construction and illustrative flats. Reference text and fabrication claims are inspiration to assess, not instructions or verified methods; do not reproduce reference signatures or logos.
3. Review proportion, material behavior, movement, practicality, and agreement across front/side/back views. Give concrete critique and possible improvements; distinguish your suggestions from the designer's instructions. Resolve construction implications affecting appearance before concept acceptance.
4. Refine through short Q&A and image annotations. Reuse the [local review form](assets/annotation-review.html) and its version-1 format; load PNG exports of quick sketches into the matching view. Treat marks and handwriting as change requests, not finished artwork. Interpret arrows and outlined shapes in context; ask when a mark could imply materially different changes.
5. Show a clean revision with the marks removed and compare it against every requested change. Report incorporated, unresolved, and deferred requests by annotation ID. Update all affected views and retain previous versions under the same garment ID.
6. Repeat until the designer explicitly accepts a specific revision. An export, a selected option, or silence is not acceptance. Freeze the dated accepted images and brief; record any agreed exclusions or deferred details.

**Handoff:** the accepted concept revision, consistent views, resolved design requests, and recorded decisions. Begin phase 3 only after this handoff. Later design changes return to this phase; changes affecting seams, proportions, or assembly mark older construction sheets as **needs revision**.

## Status and measurement record

Track these independently in the garment brief:

- Workflow: phase 1 / phase 2 / phase 3, with current revision and unresolved handoff items. Track this in the brief; the review form's schema need not change.
- Concept: exploring / in review / accepted, with accepted revision.
- Construction: not started / drafted / checked / needs revision, with source concept revision and checks performed.
- Fit: not checked / toile checked / adjusted, with wearer, date, and unresolved fit issues.
- Print scale: digital not checked / digitally checked; separately physical not checked / physically checked, with measured horizontal and vertical calibration dimensions, paper, printer, and date.

Exporting a file does not advance fitting or physical-print status. Keep body measurements, proposed finished measurements, ease, and tolerances distinct. Record measurement source/date and whether confirmed, supplied standard-size data, or provisional. Never invent missing body lengths, drafting rules, or grading. Request the measurements needed for the selected garment, or work from a documented base pattern whose size and provenance are known.

## Phase 3 — Production preparation

Use the organization and completeness of established commercial sewing patterns as the quality bar, without copying a branded template or implying affiliation.

First confirm the wearer or documented size basis, all required measurements, fabric behavior, finished dimensions, ease, and tolerances. Lay out the measurement specification and resolve missing drafting inputs before creating full-size geometry. Record the drafting method or base-pattern provenance and link every production file to the accepted concept revision.

Then prepare and check the package in this order:

- **Specification:** identified points of measure, body and finished dimensions, ease, tolerance, material behavior, units, size basis, and missing information.
- **Flats:** front/back and relevant side/interior views; every seam, opening, pocket, closure, facing, lining, support, hem, and trim placement. Identify hidden construction.
- **Pattern pieces:** stable IDs, cut quantities, fabric/lining/interfacing, grain/fold lines, stitch and cut lines, seam/hem allowances, notches, drill and placement marks, closures, and seam-pair references. Check lengths along stitch lines, with intended easing documented.
- **Construction:** fabric/trim quantities, sewing and pressing sequence, reinforcement, edge finishes, fitting checkpoints, and care. Address streetwear mobility/pocket strength and gown support/drape/train handling as appropriate.

A pattern-piece relationship diagram remains a **pattern overview**. Do not enlarge an overview or trace watercolor pixels and relabel it a full-size pattern. Draft production geometry from confirmed measurements and a stated method or supplied base; check curves, allowances, seam pairs, and placement before release. For full-size output, read [print-ready patterns](references/print-ready-patterns.md).

**Handoff:** checked flats, measurement specifications, editable patterns, tailor instructions, and digitally verified print exports. Identify drafts and unresolved items explicitly. A package for toile testing can precede final fit verification; label it accordingly. Describe the package as ready for production only when construction checks, a physical calibration print, and a toile fitting have passed and any resulting corrections are reflected in the current files. If those checks require the designer's physical work, deliver the checked digital package with those statuses pending.

## Tools and delivery

Use editable SVG for construction geometry with stable groups for construction, cutting, and annotations. Artwork PNGs belong in illustration PDFs; sewing-pattern PDFs must retain vectors and physical dimensions.

Offer Claude Design as an optional manual handoff for early exploration or final document layout, using the prompt packages in the illustration reference. Include the brief, current/accepted images, comments, layout instructions, and editable sources. Verify available integrations before promising control. A presentation export never verifies sewing geometry or print scale; keep measured production sources authoritative. Do not promise automatic chat submission.

CorelDRAW or another vector editor is optional when the designer asks for native editing, provides a native file, or the editor materially helps construction. Preserve originals and work on a copy. Inspect the supported control surface before promising live edits; a failed import is not a completed edit. Return to SVG exchange when direct control is unavailable instead of repeatedly attempting the same failing picker.

Render and inspect every delivered SVG/PDF page for clipping, readability, missing geometry, and agreement across views. Proofread requested Norwegian labels and preserve the designer's chosen branding/signature. Deliver artwork and sources, separate illustrated instructions, and checked A4/A0 pattern PDFs when full-size drafting is actually complete. State any missing measurements and distinguish digital checks from physical checks.
