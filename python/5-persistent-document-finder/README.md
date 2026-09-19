# Persistent Document Finder

An extended version of [Document Finder](../2-document-finder/) that adds a
persistence mechanism: it installs itself to run automatically on every
login, then repeats the document scan each time.

> **DISCLAIMER: For educational purposes only.** Run only on systems you own
> or have explicit permission to test.

## What It Does

The tool:

- On Windows, creates a shortcut in the Startup folder
  (`%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`) pointing back
  at itself.
- On Linux, writes a `.desktop` autostart entry to `~/.config/autostart`.
- After registering itself, performs the same PDF/DOC/DOCX scan as
  Document Finder and writes matches to `found_files.txt`.

## Why It Is a Security Tool

Persistence is one of the core stages of the MITRE ATT&CK framework
(`TA0003`): malware and post-exploitation tooling need to survive a reboot
to remain useful to an attacker. Startup-folder shortcuts and autostart
`.desktop` entries are two of the most common, simplest persistence
techniques used in the wild, precisely because they require no elevated
privileges. Combining persistence with a data-discovery scan mirrors how
real info-stealer malware behaves: install once, then keep quietly
re-scanning for valuable files on every login.

Understanding this technique is directly useful for defenders — knowing
what to look for (unexpected Startup shortcuts, unfamiliar autostart
entries) is a standard step in incident response and endpoint hardening.

> This implementation only enumerates and lists file paths locally. It does
> not read file contents, exfiltrate data, or attempt to hide itself.

## Requirements

- Python 3
- `pywin32` on Windows (only needed for the Startup shortcut; the script
  still runs and scans without it, just without persistence)

## Usage

```bash
python persistent_document_finder.py
```

## Removing It

- **Windows:** delete the `FileSearcher.lnk` shortcut from the Startup
  folder.
- **Linux:** delete `~/.config/autostart/FileSearcher.desktop`.

## Limitations

- Persistence technique is basic and easily visible to anyone checking the
  Startup folder or autostart directory — it makes no attempt at stealth.
- No privilege escalation, no scheduled-task fallback, no exfiltration.

## Skills Demonstrated

- OS-specific persistence mechanisms (Windows Startup, Linux autostart)
- Cross-platform branching with `platform.system()`
- Security awareness around startup/autorun locations as a detection point
