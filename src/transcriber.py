import logging
import speech_recognition as sr
from pocketsphinx.pocketsphinx import *
import wave

l = logging.getLogger(__name__)


def transcribe(wav_file):
    l.info("Transcribing " + wav_file)
    r = sr.Recognizer()

    wave_read = wave.open(wav_file, 'rb')
    length = wave_read.getnframes()/wave_read.getframerate()  # Length of audio in seconds
    l.debug("Audio Length: " + str(length) + " seconds.")

    with sr.AudioFile(wav_file) as source:
        audio = r.record(source)   # Reads entire audio file into memory
        raw_transcript = r.recognize_sphinx(audio, show_all=True)

    transcript = []
    nframes = Decoder.n_frames(raw_transcript)
    offset = None
    for seg in Decoder.seg(raw_transcript):
        if offset is None:
            offset = seg.start_frame
        word = seg.word
        start_frame = seg.start_frame - offset
        end_frame = seg.end_frame - offset
        duration = end_frame - start_frame  # in milliseconds
        transcript.append((word, start_frame/nframes*length, end_frame/nframes*length, duration))
    l.debug(str(transcript))
    return transcript

