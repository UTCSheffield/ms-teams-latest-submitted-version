# submissionsync

Create shortcuts to the latest submitted assignment versions from a hierarchical student work directory structure.

## Overview

`submissionsync` automates the organization of student submissions by creating shortcuts to only the latest version of each assignment. Perfect for managing large volumes of student work organized in the nested directories produced by "MS Teams Assignments".

## Features

- 🔗 Automatic shortcut creation to latest submission versions
- 📁 Intelligent filtering of Student Work directories
- ⚡ Modification time caching for performance
- 🔄 Force rebuild option for rechecking all submissions
- 🐛 Debug mode for troubleshooting
- 📊 Optional directory tree visualization
- 🖥️ Cross-platform Python module (shortcuts on Windows)

## Installation

### Basic Installation

```bash
pip install submissionsync
```

### With Windows Shortcut Support

```bash
pip install submissionsync[win32]
```

## Quick Start

### Using Defaults

Run with default paths:
```bash
submissionsync
```

This uses:
- **Source**: `~/UTC Sheffield`
- **Output**: `P:\Documents\Student Work - Latest Submissions`

### Custom Directories

Specify custom source and output paths:
```bash
submissionsync /path/to/student/work /path/to/output
```

## Usage

### Command Line Interface

```bash
submissionsync [SOURCE] [OUTPUT] [OPTIONS]
```

**Arguments:**
- `SOURCE`: Source directory containing student work (optional, default: `~/UTC Sheffield`)
- `OUTPUT`: Output directory for shortcuts (optional, default: `P:\Documents\Student Work - Latest Submissions`)

**Options:**
```bash
  --debug          Show detailed processing information
  --show-tree      Display directory tree before processing
  --force          Force recreation of all shortcuts (ignore cache)
  --version        Show version and exit
  --help           Show help message and exit
```

### Examples

```bash
# Debug mode with verbose output
submissionsync --debug

# Force rebuild of all shortcuts
submissionsync --force

# Show directory tree and process
submissionsync --show-tree

# Custom paths with options
submissionsync /source/path /output/path --debug --force
```

## Module Usage

Use `submissionsync` as a Python library:

```python
from submissionsync import create_symlink_structure
from pathlib import Path

source = Path.home() / "UTC Sheffield"
output = Path.home() / "shortcuts"

# Basic usage
create_symlink_structure(source, output)

# With debug output
create_symlink_structure(source, output, debug=True)

# Force rebuild
create_symlink_structure(source, output, force=True, debug=True)

# Show directory tree
create_symlink_structure(source, output, show_tree=True)
```

### Available Functions

```python
from submissionsync import (
    mask,                    # Filter mask for relevant directories
    get_latest_mtime,        # Get latest modification time in path
    iter_latest_versions,    # Iterate over latest version folders
    create_symlink_structure # Main function to create shortcuts
)
```

## Directory Structure

The tool expects a structure like:
