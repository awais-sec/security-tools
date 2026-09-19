# Document Finder

A simple Python utility that recursively scans a directory tree for PDF, DOC,
and DOCX files and writes every matching path to a text file.

## What It Does

The tool:

- Walks a root directory (the whole drive by default) looking for files with
  `.pdf`, `.doc`, and `.docx` extensions.
- Collects every matching path, no matter how deeply nested.
- Writes the full list of found paths to `found_files.txt`.

## Why It Is a Security Tool

Bulk-searching a filesystem for document types is a real reconnaissance step,
used both offensively and defensively. An attacker with local or remote
filesystem access can use exactly this kind of enumeration to locate
sensitive documents (financial records, contracts, credentials left in
files) before exfiltrating them. On the defensive side, the same technique
is used in data-loss-prevention (DLP) audits and insider-threat assessments
to answer the question "what sensitive files would be exposed if this
machine were compromised?"

> This implementation only enumerates and lists file paths locally. It does
> not read file contents or transmit anything off the machine.

## Requirements

- Python 3
- No external packages are required.

## Usage

```bash
python document_finder.py
```

The script searches `C:\` on Windows or `/home/` on Linux/macOS and prints
the total number of matches, then saves every path to `found_files.txt` in
the current directory.

## Limitations

- Extensions are matched by filename suffix only, not by file signature.
- No filtering by file size, date, or content.
- No exfiltration or upload step — output stays local.

## Skills Demonstrated

- Recursive filesystem search with `glob`
- Cross-platform path handling
- Security-relevant reconnaissance concepts (data discovery)
