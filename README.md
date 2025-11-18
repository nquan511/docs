# Summary Docs

This repository contains LaTeX source files and notes for interview summaries, math, trading and other topics.

What I added:
- `.gitignore` to exclude LaTeX build artifacts and common temporary files.

How to build PDFs (example using `latexmk`):

1. Install a TeX distribution (TeX Live, MiKTeX) and `latexmk`.
2. From the project folder run:

```
latexmk -pdf summary.tex
```

or build a specific file, e.g.,

```
latexmk -pdf Coding/DP/Dp.tex
```

Notes:
- Aux files (e.g., `.aux`, `.toc`, `.fls`) are ignored by `.gitignore` since these are generated on build.
- Jupyter notebooks are kept, but checkpoints are ignored.

Next steps:
- If you want me to add a remote and push, provide the Git remote URL (e.g., `https://github.com/username/repo.git`).
