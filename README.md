# Fashion Design & Sewing Patterns

A Codex skill for adult fashion across womenswear, menswear, and unisex designs: couture, tailoring, everyday wear, streetwear, romantic, vintage, avant-garde, and activewear. The designer guides the choices; the assistant acts as sketcher and tailor.

## Workflow

1. **Fast visual exploration:** one taste question at a time, five visual alternatives plus a custom answer, and immediate local SVG previews that preserve earlier choices.
2. **Refined illustration and critique:** choose pencil, ink, watercolor, marker, or a detailed couture appearance; develop illustration sheets or concept boards; annotate and revise until explicit acceptance.
3. **Production preparation:** confirmed measurements, construction drawings, editable patterns, tailor instructions, and print verification.

Concept acceptance, construction checking, fitting, and digital/physical print verification have separate statuses. Sketches and schematic pattern overviews do not establish full-size sewing geometry.

## Use with Codex

Clone this repository into your Codex skills directory as `streetwear-fashion-design`. Invoke `$streetwear-fashion-design` in chat. See [SKILL.md](SKILL.md) for the complete workflow. CorelDRAW and other vector editors are optional.

## Local annotation form

Start with [assets/design-explorer.html](assets/design-explorer.html) for quick choices and designer comments. It includes clearly labelled gown-neckline and illustration-style examples. The assistant prepares a round for the actual garment; this is not a universal garment generator. Save/reopen the round, or export SVG, PNG, and structured choices to chat. Custom requests are recorded for redraw, with image exports disabled until a revised sketch exists.

The explorer separates fashion aesthetic, garment construction, and illustration medium. Its drawings use visual coordinates, not garment dimensions. See [the visual workflow](references/interactive-review.md) for preparing rounds and [illustration and boards](references/illustration-and-boards.md) for refined artwork and optional Claude Design handoffs.

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
node scripts/check_explorer.mjs
python scripts/check_server.py
```

A production package still requires checked construction, a physical calibration print, and toile fitting. This repository contains reusable templates and guidance; it contains no completed garment patterns or personal review sessions.

Claude Design can be used manually for early visual exploration or final document layout. Direct remote control and automatic chat submission are not assumed. Presentation exports do not establish sewing-pattern scale.
