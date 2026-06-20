# File Explorer — Cross-Drive File Search Utility

> **Find any file across all local and USB drives from the command line**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)](https://www.microsoft.com/windows)

## Overview

`File_Explorer` is a lightweight command-line utility that scans **every mounted drive** on a Windows machine — including USB sticks and external HDDs — to locate a file by name. When multiple copies are found, it identifies duplicates, sorts them by modification date, and returns the path of the **most recent version**.

## Features

- **Full-Drive Scan** — automatically discovers and searches all local and external drives
- **Duplicate Detection** — lists every copy found with its last-modified timestamp
- **Smart Sort** — returns the most recently modified file path first
- **Zero Dependencies** — uses only the Python standard library

## Usage

```bash
python File_Explorer.py
```

When prompted, enter the filename you are looking for (e.g. `report.xlsx`). The tool will print every match with its path and modification date, then highlight the newest copy.

### Example output

```
Searching all drives...
Found: D:\Projectseport.xlsx  (2024-11-15 09:43:21)
Found: E:\Backupeport.xlsx    (2024-08-02 14:12:05)

Most recent: D:\Projects\report.xlsx
```

## Requirements

No third-party packages required. Runs with a standard Python 3.9+ installation.

## Author

**Engin Can Cicek**
