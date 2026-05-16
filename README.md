# MonteurMeister

Python-based montage planning and field team coordination software by Derrer Solutions.

---

## Overview

MonteurMeister is a desktop application for planning, coordinating, and managing field montage teams and installation workflows. Built for Swiss SMEs and technical field operations.

## Core Features

- Montage job planning and scheduling
- Field team coordination and assignment
- Windows desktop application
- Automated GitHub Actions build pipeline (Windows EXE)
- Configuration management
- Asset management

## Tech Stack

- **Language:** Python
- **Platform:** Windows Desktop
- **Build:** GitHub Actions (Windows EXE via PyInstaller)
- **Distribution:** Standalone executable

## Setup

```bash
# Clone repository
git clone https://github.com/JayDeeG/MonteurMeister.git
cd MonteurMeister

# Install dependencies
pip install -r requirements.txt

# Run application
python monteurmeister/main.py
```

## Build (Windows EXE)

Automated builds are handled via GitHub Actions. See `.github/workflows/` for the build configuration.

## Project Status

Internal tool — active use by Derrer Solutions field operations.

---

*Derrer Solutions · Swiss Quality Software*
