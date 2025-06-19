import speech_recognition as sr
from pydub import AudioSegment
import os

def main():
    mp3_path = input("Enter the path to your MP3 file (e.g., my_audio.mp3): ").strip()

    if not os.path.isfile(mp3_path):
        print("Invalid file path.")
        return
    wav_path = "temp_audio.wav"
    sound = AudioSegment.from_file(mp3_path)
    sound.export(wav_path, format="wav")
    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language="tr-TR")  # Turkish language
        print("Transcription:", text)
    except sr.UnknownValueError:
        print("Speech could not be understood.")
    except sr.RequestError as e:
        print("Google API error:", e)

    if os.path.exists(wav_path):
        os.remove(wav_path)

if __name__ == "__main__":
    main()
