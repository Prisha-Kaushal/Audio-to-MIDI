from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
import soundfile as sf

# Load your audio file (must be mono or stereo WAV)
audio_path = "test 3.wav"

# Run the prediction
model_output, midi_data, note_events = predict(audio_path)

# Save the MIDI
with open("output.mid", "wb") as f:
    midi_data.write(f)

# Optional: save note events as CSV or for visualization
import pandas as pd
df = pd.DataFrame(note_events)
df.to_csv("note_events.csv", index=False)