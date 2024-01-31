# Whisper local w python notes

- created python environment in vscode using VENV
  - Python: Create Environment > Venv > Python 3.11.7
- check that pip is up to date
  - python3 -m pip install --upgrade pip
- install whisper to environment
  - python3 -m pip install -U openai-whisper

worked by pressing play with hard coded test.m4a 

----

- created alias for easier command line usage, in .zshrc in ~/
  - alias vm="/Users/caleb/git/vm/.venv/bin/python /Users/caleb/git/vm/main.py"
- added argument for audiofile so i can run in terminal like
  - vm test.m4a
- parseargs also has built in --help and -h that prints:

    usage: main.py [-h] audiofile

    Voice Memo - (c) 2024 Caleb Moore

    positional arguments:
      audiofile   Name of the audio file to process

    options:
      -h, --help  show this help message and exit

- added audiofolder argument that will process each file in a folder path with command:
    vm test/ 
- added fp16=False to model.transcribe to avoid that error in terminal about needing to use fp32

TODO:
+ look into voice memo default folder like this project:
https://github.com/michaelgriscom/voice-memo-transcription/blob/main/transcribe.py
+ chatgpt to come up with filenames based on transcription
+ whisper-at for audio-event labels
https://github.com/YuanGongND/whisper-at/blob/main/audioset_label.csv
