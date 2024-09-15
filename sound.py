import pyaudio
import wave

available_notes = ['C', 'D', 'E', 'F', 'G']

def play(note):
    
    if note not in available_notes:
        return
    
    # Load the sound file
    wavefile = wave.open("assets/sounds/" + note + ".wav", 'rb')

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open a stream for output
    stream = p.open(format=p.get_format_from_width(wavefile.getsampwidth()),
                    channels=wavefile.getnchannels(),
                    rate=wavefile.getframerate(),
                    output=True)

    # Read and play the sound data
    data = wavefile.readframes(1024)
    while data:
        stream.write(data)
        data = wavefile.readframes(1024)

    # Close the stream and PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    
if __name__ == "__main__":
    play('C')