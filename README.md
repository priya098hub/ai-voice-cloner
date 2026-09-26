# Personal Voice AI

Personal Voice AI is a local, offline desktop application for creating a voice profile from your own recording and generating long-form speech from large text scripts. It is designed for personal use and runs on a local Windows PC without requiring a paid cloud API.

## Features

- Voice recording and sample import
- Local voice profile management
- Long-text normalization and chunking
- Resume-aware long generation jobs
- Audio chunk saving and final merging
- WAV and MP3 export
- CPU fallback and GPU detection
- Offline local model support

## Important notice

This app is intended for cloning and synthesizing voices for which you have clear permission to use. Do not clone someone else’s voice without consent.

## Model and license note

This project is designed around open-source local TTS options such as XTTS-style models. Licensing varies by model, so review the model license before downloading or using it.

## System requirements

- Windows 11 or later
- Python 3.11+
- 8 GB RAM minimum (16 GB recommended)
- FFmpeg installed and on PATH
- Local GPU optional; CPU fallback supported

## Installation

For step-by-step beginner instructions, see [SETUP_WINDOWS.md](SETUP_WINDOWS.md).

## Privacy

- Voice files stay local on your device.
- Text is processed locally.
- No analytics or telemetry are included.
- No external APIs are required for the core workflow.

## How to create a voice

1. Launch the app.
2. Open the voice section.
3. Record a clean voice sample or import a WAV/MP3/M4A file.
4. Save the profile in the `voices/` folder.
5. Validate the sample before using it.

## How to generate speech without any API

1. Open PowerShell in the project folder.
2. Activate the virtual environment:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
3. Start the app:
   ```powershell
   python app.py
   ```
4. Select a voice profile.
5. Paste text or load a `.txt`/`.md` file.
6. Choose language, chunk size, and output format.
7. Click Generate Audio.
8. The app chunks the text, generates audio locally, and merges the final result.

### Local model requirement

This project is designed to run fully offline. You do not need an API key.

Place a compatible local XTTS model in the `models/` folder, for example:

```text
models/
  xtts_v2/
  xtts/
```

The app will use the model from that folder automatically when present.

## Long text support

The app automatically normalizes text, splits it into natural sentence-aware chunks, and saves each chunk to disk as it is generated. This allows large jobs to resume later without starting over.

## GPU support

If CUDA is available, the app uses GPU acceleration when configured. If not, it falls back to CPU automatically.

## Troubleshooting

- `ModuleNotFoundError`: install dependencies with `python -m pip install -r requirements.txt`
- `ffmpeg not found`: install FFmpeg and restart PowerShell
- `CUDA unavailable`: the app will use CPU mode automatically
- `Voice sample invalid`: provide a clearer recording or a longer sample with speech

## Project structure

- `app.py` – app entry point
- `personal_voice_ai/` – main library package
- `tests/` – automated tests
- `SETUP_WINDOWS.md` – Windows setup guide
