import whisper
import argparse
import os

def main():
    language = "en"
    initial_prompt = "The following is a recording of my playing the acoustic guitar, and singing along. Please ignore the guitar and only focus on the words being sung."
    parser = argparse.ArgumentParser(description='Voice Memo - (c) 2024 Caleb Moore') 
    parser.add_argument('--file', type=str, help='Name of the audio file to process')
    parser.add_argument('--folder', type=str, help='Name of the folder to process')
    parser.add_argument('--model', type=str, help='Name of the model to use')
    args = parser.parse_args()
    
    if args.model:
      model = whisper.load_model(args.model)
    else:
      model = whisper.load_model("base")


    if args.file:
        audiofile = args.file
        print(f"Single file mode: {audiofile}")
        result = model.transcribe(audiofile, fp16=False)
        audiofile = audiofile.split('.')[0] # remove the audio extension
        with open (f"{audiofile}.txt", "w") as f:
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
    print("Done!")
    os.system("""
          osascript -e 'display notification "done!" with title "VM"'
          """)

if __name__ == "__main__":
    main()





