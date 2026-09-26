# Personal Voice AI - Windows Setup

This guide is written for beginners and uses PowerShell commands.

## STEP 1: Open PowerShell

Open PowerShell in the folder where you want to keep the app.

## STEP 2: Create the project folder

```powershell
cd C:\Users\<USERNAME>\Desktop
mkdir PersonalVoiceAI
cd PersonalVoiceAI
```

## STEP 3: Create a virtual environment

```powershell
py -3.11 -m venv .venv
```

If Python 3.11 is not installed, install it from the Microsoft Store or python.org, then repeat the command.

## STEP 4: Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

## STEP 5: Upgrade pip

```powershell
python -m pip install --upgrade pip
```

## STEP 6: Install required packages

```powershell
pip install -r requirements.txt
```

## STEP 7: Install FFmpeg

FFmpeg is required for merging and exporting audio files.

### Option A: winget

```powershell
winget install Gyan.Dev.FFmpeg
```

### Option B: official zip

Download FFmpeg and add the `bin` folder to PATH.

After installation, verify:

```powershell
ffmpeg -version
```

Expected output should include the FFmpeg version string.

## STEP 8: Download the TTS model

The app uses a local XTTS-style model and does not require any API key.

Place the model folder manually under `models/` if you already have one, for example:

```text
models/
  xtts_v2/
```

or

```text
models/
  xtts/
```

If you do not have a model yet, download a compatible local XTTS model from a trusted source and put it in that folder before generating audio.

## STEP 9: Launch the app

```powershell
python app.py
```

## STEP 10: First-run checklist

1. Create a voice profile.
2. Import or record a voice sample.
3. Paste text or load a `.txt` file.
4. Choose chunk size and language.
5. Generate audio.

## Troubleshooting

If you see `ModuleNotFoundError`, run:

```powershell
python -m pip install -r requirements.txt
```

If `ffmpeg` is not found, reopen PowerShell after installation.

If the model fails to download, check the internet connection and try again.

If Windows microphone is unavailable, use the import voice sample feature instead.

## Privacy note

Voice samples and generated audio stay local on your computer. Nothing is uploaded to a server by default.
