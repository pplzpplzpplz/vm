import whisper
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Voice Memo - (c) 2024 Caleb Moore') 
    # parser.add_argument('audiofilename', type=str, help='Name of the audio file to process')
    parser.add_argument('audiofolder', type=str, help='Name of the folder to process')
    args = parser.parse_args()
    
    # audiofile = args.audiofilename
    audiofolder = args.audiofolder
    model = whisper.load_model("base")

    # loop through each file inside of the audiofolder file folder and transcribe it
    for file in os.listdir(audiofolder):
        audiofile = os.path.join(audiofolder, file)
        print(f"Processing file: {audiofile}")
        result = model.transcribe(audiofile, fp16=False)
        language = "en"
        print(file + result["text"])


    # print(f"Processing file: {audiofile}")

    # result = model.transcribe(audiofile, fp16=False)
    # language = "en"

    # print(result["text"])

if __name__ == "__main__":
    main()





