import sys
from pathlib import Path


def create_shortcut(shortcut_path: Path, target_folder: Path, force: bool = False, dbg=None):
    """Create a Windows shortcut. Returns True on success."""
    if dbg is None:
        dbg = lambda *args, **kwargs: None
    
    if sys.platform != "win32":
        dbg(f"  ⚠ Shortcuts only supported on Windows; skipping {shortcut_path}")
        return True
    
    try:
        import win32com.client
    except ImportError:
        dbg("  ✗ pywin32 not installed; cannot create shortcuts")
        return False
    
    shell = win32com.client.Dispatch("WScript.Shell")
    
    if shortcut_path.exists() and not force:
        try:
            existing_target = Path(shell.CreateShortCut(str(shortcut_path)).Targetpath)
            if existing_target.resolve() == Path(target_folder).resolve():
                dbg("  - Shortcut already up to date; skipping")
                return True
            else:
                dbg(f"  - Shortcut exists but points to {existing_target}; replacing")
                shortcut_path.unlink(missing_ok=True)
        except Exception as e:
            dbg(f"  - Could not read existing shortcut (will recreate): {e}")
    elif shortcut_path.exists() and force:
        dbg("  - Force enabled; recreating shortcut")
        shortcut_path.unlink(missing_ok=True)

    try:
        shortcut = shell.CreateShortCut(str(shortcut_path))
        shortcut.Targetpath = str(target_folder)
        shortcut.WorkingDirectory = str(target_folder.parent)
        shortcut.save()
        dbg(f"  ✓ Shortcut created/updated")
        if not shortcut_path.exists():
            raise Exception("Shortcut creation failed - file does not exist after save()")
        return True
    except Exception as e:
        dbg(f"  ✗ Error creating shortcut: {e}")
        raise
