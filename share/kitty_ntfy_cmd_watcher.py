from typing import Any, Dict

from kitty.boss import Boss
from kitty.window import Window
import os
import subprocess

LOCK_FILE = "/tmp/kitty_ntfy_cmd_lock.lock"

def on_resize(boss: Boss, window: Window, data: Dict[str, Any]) -> None:
    # Here data will contain old_geometry and new_geometry
    # Note that resize is also called the first time a window is created
    # which can be detected as old_geometry will have all zero values, in
    # particular, old_geometry.xnum and old_geometry.ynum will be zero.
    pass

def on_focus_change(boss: Boss, window: Window, data: Dict[str, Any])-> None:
    # Here data will contain focused
    pass

def on_close(boss: Boss, window: Window, data: Dict[str, Any])-> None:
    # called when window is closed, typically when the program running in
    # it exits
    pass

def on_set_user_var(boss: Boss, window: Window, data: Dict[str, Any]) -> None:
    # called when a "user variable" is set or deleted on a window. Here
    # data will contain key and value
    pass

def on_title_change(boss: Boss, window: Window, data: Dict[str, Any]) -> None:
    # called when the window title is changed on a window. Here
    # data will contain title and from_child. from_child will be True
    # when a title change was requested via escape code from the program
    # running in the terminal
    pass

def on_cmd_startstop(boss: Boss, window: Window, data: Dict[str, Any]) -> None:
    # called when the shell starts/stops executing a command. Here
    # data will contain is_start, cmdline and time.
    # boss.call_remote_control(window, ('send-text', f'--match=id:{window.id}', 'hello world'))
    if not data["is_start"]:
        print(data["cmdline"])
        if os.path.exists(LOCK_FILE) and not "kitty-ntfy-cmd" in data["cmdline"]:
            subprocess.run(["curl",
                              "-H",
                              "p:4",
                              "-d",
                              f"Command `{data['cmdline']}` ended.",
                              "http://192.168.1.23:46975/CLI"], capture_output=True, text=True)
