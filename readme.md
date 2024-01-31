# Voice Memo Mate 

Bulk voice Memo Categorization, Naming, Description and Transcription using OpenAI's Whisper model.

## Initial environment setup
- created python environment in vscode using VENV
  - shift+cmd+p> Python: Create Environment > Venv > Python 3.11.7
- check that pip is up to date
  - python3 -m pip install --upgrade pip
- install whisper to environment
  - python3 -m pip install -U openai-whisper
- created alias for easier command line usage, in .zshrc in ~/

`alias vm="/Users/caleb/git/vm/.venv/bin/python /Users/caleb/git/vm/main.py"`

## Script usage
```
    usage: vm [-h] [--file FILE] [--folder FOLDER] [--model MODEL]

    Voice Memo Mate - (c) 2024 Caleb Moore

    options:
      -h, --help       show this help message and exit
      --file FILE      Name of the audio file to process (e.g. "vm audio.wav")
      --folder FOLDER  Name of the folder to process (e.g. "vm test/")
      --model MODEL    Name of the model to use (default is "base")
```
### Details
- The hard coded `initial_prompt` var sets the *context* for the recording, useful for after deciding what kind of recording it is. For example:

  ```initial_prompt = "The following is a recording of me playing the acoustic guitar, and singing along. Please ignore the guitar and only focus on the words being sung."```

- Forces `fp32` by setting `fp16=False` on `model.transcribe` (to avoid command line error)

## TODO 
+ look into voice memo default folder like this project:
https://github.com/michaelgriscom/voice-memo-transcription/blob/main/transcribe.py
+ chatgpt to come up with filenames based on transcription
+ whisper-at for audio-event labels- genre, describes sounds, etc!
https://github.com/YuanGongND/whisper-at/blob/main/audioset_label.csv
+ name ideas: memomate, sonarch (used), 
