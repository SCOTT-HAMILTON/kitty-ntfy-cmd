import fcntl
import sys
import os
from plyer import notification

LOCK_FILE = "/tmp/kitty_ntfy_cmd_lock.lock"

def lock_file(lock_file):
    """Create a lock file to indicate the lock is held."""
    if os.path.exists(lock_file):
        print("Lock already held by another process.")
        return
    with open(lock_file, 'w') as f:
        f.write("locked")

    print("File locked.")

def unlock_file(lock_file):
    """Remove the lock file to release the lock."""
    if os.path.exists(lock_file):
        os.remove(lock_file)
        print("File unlocked.")
    else:
        print("No lock to release.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 kitty_ntfy_cmd <allow|forbid>")
        sys.exit(1)

    action = sys.argv[1].lower()
    if action == "allow":
        lock_file(LOCK_FILE)
        notification.notify(
            title='Activated',
            message='Kitty commands ending notifications activated.',
            app_name='kitty-ntfy-cmd',
            timeout=10
        )
    elif action == "forbid":
        unlock_file(LOCK_FILE)
        notification.notify(
            title='Deactivated',
            message='Kitty commands ending notifications deactivated.',
            app_name='kitty-ntfy-cmd',
            timeout=10
        )
    else:
        print("Unknown action. Use 'allow' or 'forbid'.")
