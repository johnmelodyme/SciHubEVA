# -*- coding: utf-8 -*-

import os
import sys
import locale
import platform
import subprocess
import darkdetect

try:
    import winreg
except Exception:
    pass

from pathlib import Path

from PySide2.QtCore import qVersion


DEFAULT_ENCODING = 'utf-8'
SYSTEM_LANGUAGE = locale.getdefaultlocale()[0]

PYTHON_VERSION = '.'.join(str(v) for v in sys.version_info[:3])
QT_VERSION = qVersion()


def is_windows():
    return platform.system() == 'Windows'


def is_macos():
    return platform.system() == 'Darwin'


def is_linux():
    return platform.system() == 'Linux'


def open_file(file_path, timeout=3):
    if is_windows():
        os.startfile(file_path)
    elif is_macos():
        subprocess.call(['open', file_path], timeout=timeout)
    elif is_linux():
        subprocess.call(['xdg-open', file_path], timeout=timeout)
    else:
        return


def open_directory(directory, timeout=3):
    if is_windows():
        subprocess.call(['explorer', str(Path(directory))], timeout=timeout)
    elif is_macos():
        subprocess.call(['open', directory], timeout=timeout)
    elif is_linux():
        subprocess.call(['xdg-open', directory], timeout=timeout)
    else:
        return


def is_system_dark_theme():
    if is_macos():
        return darkdetect.isDark()

    if is_windows():
        k = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize')
        try:
            return winreg.QueryValueEx(k, 'AppsUseLightTheme')[0] == 0
        except Exception:
            pass

    return False


def is_text_file(path: str) -> bool:
    try:
        with open(path, 'rt') as f:
            f.readlines()
    except:
        return False

    return True


__all__ = [
    'DEFAULT_ENCODING',
    'SYSTEM_LANGUAGE',
    'PYTHON_VERSION',
    'QT_VERSION',
    'is_windows',
    'is_macos',
    'is_linux',
    'open_file',
    'open_directory',
    'is_system_dark_theme',
    'is_text_file'
]
