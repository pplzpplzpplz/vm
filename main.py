import whisper
import argparse
import os
import pwd

def get_username():
    return pwd.getpwuid(os.getuid())[0]

def parse_arguments():
    parser = argparse.ArgumentParser(description='Voice Memo Mate - (c) 2024 Caleb Moore') 
    parser.add_argument('--file', type=str, help='Name of the audio file to process (e.g. "vm audio.wav")')
    parser.add_argument('--folder', type=str, help='Name of the folder to process (e.g. "vm test/")')
    parser.add_argument('--model', type=str, default="base", help='Name of the model to use (default is "base")')
    return parser.parse_args()

def main():
    language = "en"
    # initial_prompt = "The following is a recording of me playing the acoustic guitar, and singing along. Please ignore the guitar and only focus on the words being sung."

    args = parse_arguments()
    model = whisper.load_model(args.model)

    username = get_username()
    print("username:", username)

    voiceMemoFolder = f"/Users/{username}/Library/Group Containers/group.com.apple.VoiceMemos.shared/Recordings"
    print("icloud voice memo location:", voiceMemoFolder)

    if args.file:
        audiofile = args.file
        print(f"Single file mode: {audiofile}")
        result = model.transcribe(audiofile, fp16=False)
        # write the new file but remove the audio extension before adding .txt
        with open (f"{audiofile.split('.')[0]}.txt", "w") as f:
            f.write(result["text"])
    elif args.folder:
        audiofolder = args.folder
        print(f"Folder mode: {audiofolder}")
        for file in os.listdir(audiofolder):
            if file != '.DS_Store':
              audiofile = os.path.join(audiofolder, file)
              print(f"Processing file: {audiofile}")
              result = model.transcribe(audiofile, fp16=False)
              with open (f"{audiofile.split('.')[0]}.txt", "w") as f:
                  f.write(result["text"])
    else:
      print("Error: Please provide either --file or --folder argument.")
      return
    
    print("Done!")
    os.system("""
          osascript -e 'display notification "done!" with title "Sonarch"'
          """)

if __name__ == "__main__":
    main()





