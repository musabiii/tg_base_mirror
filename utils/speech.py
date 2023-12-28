# importing libraries
import speech_recognition as sr # numpy also require
import os
import soundfile as sf


# create a speech recognition object
r = sr.Recognizer()

def transcribe_audio(path):
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        text = ""
        try:
            text = r.recognize_google(audio_listened, language='ru-RU')
        except:
            print(" не удалось распознать")
            text = " ...не удалось распознать..."
    return text

def ogg_to_wav(ogg_file_path):
    try:
        # Open the file
        data, samplerate = sf.read(ogg_file_path)
        wav_file_path = ogg_file_path + ".wav"
        sf.write(wav_file_path, data, samplerate)
        return wav_file_path
    except:
        raise Exception



def ogg_to_text(ogg_file_path):
    try:
        wav_file_path = ogg_to_wav(ogg_file_path)
        txt = transcribe_audio(wav_file_path)
    except:
        txt = "ошибка"
        return txt

    if os.path.exists(wav_file_path):
        os.remove(wav_file_path)

    return txt


# file_name = "files/new_file_ru.ogg"

# txt = ogg_to_text(file_name)


# print(txt);
