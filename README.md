# File Orginizer Agent

A lightweight Python agent that automatically organizes files in a target directory (for example, your Downloads folder) using a task-based workflow and strategy pattern.

It can:
- Run one-time organization on startup
- Keep watching the directory for new files
- Classify files by extension into category folders
- Move files into their categorized destination folders

## How It Works

The project builds a `FileOrganizerAgent` with a `Workflow` made of three tasks:

1. `ScanFilesTask`
- Scans the target directory
- Collects only files (not folders)
- Ignores temporary/incomplete downloads like `.crdownload`, `.tmp`, `.part`

2. `ClassifyFilesTask`
- Uses strategy classes to match file extensions
- Groups files into categories:
  - `Images`
  - `Documents`
  - `Audio`
  - `Code`
  - `Videos`

3. `MoveFilesTask`
- Creates category folders if they do not exist
- Moves files into the mapped folder
- Skips if destination file already exists

After initial organization, a watchdog observer listens for new files and triggers the agent again.

## Installation

### Prerequisites
- Python `3.12+`
- `pip` (or `uv`, optional)

### Option 1: Using `uv` (recommended)
```powershell
uv sync
```

### Option 2: Using `pip`
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

## Run the Project

Run from project root:

```powershell
python main.py
```

By default, the watcher is configured in `main.py` as:

```python
WATCH_DIR = "C:/Users/User/Downloads"
```

Update this value to your own folder path if needed.

## Folder Structure

```text
file-orginizer/
|-- agent/
|   `-- organizer.py          # FileOrganizerAgent wrapper around workflow execution
|-- core/
|   |-- context.py            # Shared state passed between tasks
|   `-- workflow.py           # Task pipeline executor
|-- strategies/
|   `-- types.py              # Extension-based classification strategies
|-- tasks/
|   |-- base.py               # Abstract Task contract
|   |-- scan.py               # Scans files from target directory
|   |-- classify.py           # Maps files to category folders
|   |-- move.py               # Moves files to categorized folders
|   `-- donothing.py          # Placeholder no-op task
|-- watcher.py                # Filesystem event handler using watchdog
|-- main.py                   # Entry point: builds agent + starts observer
|-- pyproject.toml            # Project metadata and dependencies
|-- uv.lock                   # Locked dependency file for uv
`-- README.md
```

## Agent Workflow at Runtime

1. App starts and builds workflow in `main.py`
2. Agent runs once on `WATCH_DIR` to organize existing files
3. Watchdog observer starts monitoring the same directory
4. When a new file appears, handler waits briefly and runs agent again
5. Files are re-scanned, re-classified, and moved

## Current Supported File Categories

- Images: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
- Documents: `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`
- Audio: `.mp3`, `.wav`, `.aac`, `.flac`
- Code: `.py`, `.js`, `.java`, `.cpp`, `.c`, `.rb`, `.go`, `.rs`, `.ts`
- Videos: `.mp4`, `.avi`, `.mkv`, `.mov`

## Notes

- If a file extension is not matched by any strategy, it is left in place.
- If a destination file already exists, the move is skipped to prevent overwrite.
- Stop the watcher with `Ctrl + C`.
