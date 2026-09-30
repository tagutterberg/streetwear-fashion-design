# Fashion Design & Sewing Patterns

A Codex skill for co-designing gowns, high-end streetwear, and other garments. The designer guides the choices; the assistant acts as sketcher and tailor.

## Workflow

1. **Brief and detail sketches:** taste questions with five meaningful alternatives and a custom answer, watercolor concepts, and detail studies.
2. **Critique and revisions:** image annotations, consistent front/side/back views, and explicit acceptance of a named revision.
3. **Production preparation:** confirmed measurements, construction drawings, editable patterns, tailor instructions, and print verification.

Concept acceptance, construction checking, fitting, and digital/physical print verification have separate statuses. Sketches and schematic pattern overviews do not establish full-size sewing geometry.

## Use with Codex

Clone this repository into your Codex skills directory as `streetwear-fashion-design`. Invoke `$streetwear-fashion-design` in chat. See [SKILL.md](SKILL.md) for the complete workflow. CorelDRAW and other vector editors are optional.

## Local annotation form

Open [assets/annotation-review.html](assets/annotation-review.html) in a browser. Load local front, side, or back images; add numbered pins, arrows, freehand marks, text, and instructions. Export annotated PNGs and feedback JSON, then attach them in chat. Save a project JSON to reopen the original images and annotations.

The form needs no account or external service. It does not automatically submit feedback to chat. Its default interface is Norwegian. See [the review workflow](references/interactive-review.md) for prepared sessions and the optional localhost export helper.

## Printing

[The printing reference](references/print-ready-patterns.md) covers millimetre geometry, editable SVG, vector A4 tiles/A0 pages, typography, and physical calibration. Default text sizes are 9 pt labels, 8 pt notes, and 12 pt titles. Print patterns at Actual Size / 100% and measure the 100 × 100 mm calibration square in both directions before cutting.

The calibration generator creates a printer test, not a garment pattern. It requires Python, ReportLab, and pypdf:

```sh
python -m pip install reportlab pypdf
python scripts/print_calibration.py output
```

Run the annotation and skill checks with Node.js 18 or later:

```sh
node scripts/check_review.mjs
```

A production package still requires checked construction, a physical calibration print, and toile fitting. This repository contains reusable templates and guidance; it contains no completed garment patterns or personal review sessions.
