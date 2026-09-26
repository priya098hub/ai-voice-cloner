from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent
    sys.path.insert(0, str(root))
    try:
        from PySide6.QtWidgets import QApplication
        from personal_voice_ai.ui.main_window import MainWindow
    except Exception as exc:  # pragma: no cover
        raise SystemExit(
            "PySide6 is required to run the GUI. Install dependencies with: python -m pip install -r requirements.txt"
        ) from exc

    app = QApplication(sys.argv)
    app.setApplicationName("Personal Voice AI")
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
