"""APK entry point for MINOS - SIGINT // UFO Scanner.

buildozer/python-for-android launches the app from a file named ``main.py``.
This thin wrapper keeps the original ``UFOscanner.py`` untouched while
providing the standard entry point the Android packaging expects.
"""

from UFOscanner import MinosSigintUFOApp


if __name__ == "__main__":
    MinosSigintUFOApp().run()
