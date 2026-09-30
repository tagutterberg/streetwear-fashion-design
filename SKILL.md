---
name: streetwear-fashion-design
description: Co-design gowns, high-end streetwear, and other garments through designer Q&A and annotated watercolor sketches, then prepare editable tailor sheets and checked full-size sewing-pattern exports.
---

# Fashion design and sewing patterns

The user is the designer; act as their sketcher and tailor. Use this harness as the default workspace. Keep each garment's brief, images, and construction files together under a stable garment ID and revision; do not mix separate garments or use an unrelated repository as their output folder.

## Phase 1 — Brief and detail sketches

1. Establish the garment, wearer, occasion, season, finish, references, and constraints. Ask only for missing decisions in the user's language. Offer **five meaningful alternatives for every taste question**, plus a custom answer. Use a question surface that can display all five; do not invent filler alternatives for measurements or factual questions. Record the question ID, option ID, and actual answer so a later reply such as “2” cannot lose its meaning.
2. Explore materially different directions as watercolor or ink-and-wash sketches, normally three when the designer has not already selected a direction. Use image generation for raster artwork and edits. Keep identity, pose, material, and accepted details consistent. Show front, side, and back when needed, rather than inventing hidden construction silently.
3. Sketch the selected direction's details: silhouette, fabric, color, closures, pockets, trims, movement, signature, and exclusions. Include enlarged detail studies where a full-length sketch leaves decisions unclear. Record preliminary measurements with their source; finish production specifications in phase 3.

**Handoff:** a named, versioned concept with detail studies, a recorded brief, and clearly identified open decisions. Move to critique when the designer has a direction to review. Sewing patterns and production sheets belong to phase 3.

## Phase 2 — Critique and revisions

1. Review proportion, material behavior, movement, practicality, and agreement across front/side/back views. Give concrete critique and possible improvements; distinguish your suggestions from the designer's instructions. Resolve construction implications affecting appearance before concept acceptance.
2. Refine through short Q&A and image annotations. Use the [local review form](assets/annotation-review.html) when useful; read [the form workflow](references/interactive-review.md) when preparing it. Treat marks and handwriting as change requests, not finished artwork. Interpret arrows and outlined shapes in context; ask when a mark could imply materially different changes.
3. Show a clean revision with the marks removed and compare it against every requested change. Report incorporated, unresolved, and deferred requests by annotation ID. Update all affected views and retain previous versions under the same garment ID.
4. Repeat until the designer explicitly accepts a specific revision. An export, a selected option, or silence is not acceptance. Freeze the dated accepted images and brief; record any agreed exclusions or deferred details.

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

CorelDRAW or another vector editor is optional when the designer asks for native editing, provides a native file, or the editor materially helps construction. Preserve originals and work on a copy. Inspect the supported control surface before promising live edits; a failed import is not a completed edit. Return to SVG exchange when direct control is unavailable instead of repeatedly attempting the same failing picker.

Render and inspect every delivered SVG/PDF page for clipping, readability, missing geometry, and agreement across views. Proofread requested Norwegian labels and preserve the designer's chosen branding/signature. Deliver artwork and sources, separate illustrated instructions, and checked A4/A0 pattern PDFs when full-size drafting is actually complete. State any missing measurements and distinguish digital checks from physical checks.
