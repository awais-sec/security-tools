# CMD Prank

A tiny Python script that looks like an innocuous grade checker but launches
a command shell based on a hidden condition in the code.

## What It Does

The tool:

- Asks for a student's name and a mark out of 100.
- If the mark isn't a perfect 100, it silently opens a new `cmd` window
  (`os.system("start cmd")`).

## Why It Is a Security Tool

This is a deliberately simplified illustration of **trojan-style behavior**:
a program that presents itself as one thing (a grade checker) while its
real, hidden action (launching an arbitrary OS command) has nothing to do
with its stated purpose. Real trojans use exactly this pattern at a larger
scale — a program looks legitimate on the surface while a conditional
branch triggers unrelated, unexpected behavior. It's a useful, low-stakes
example for discussing why running untrusted scripts is risky, and why
`os.system`/shell-out calls in any program deserve scrutiny.

> This implementation only opens a local `cmd` window. It runs no commands
> inside it and has no payload beyond that.

## Requirements

- Python 3
- No external packages are required.

## Usage

```bash
python cmd_prank.py
```

## Limitations

- Windows-only (`start cmd`).
- No actual payload — it's a demonstration of the trigger pattern, not an
  attack.

## Skills Demonstrated

- Conditional program logic
- `os.system` and shell-out calls
- Security awareness: hidden/unexpected behavior in seemingly benign code
