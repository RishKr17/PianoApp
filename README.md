# 🎹 Rishky Piano

A state-of-the-art interactive piano playable with your **MacBook Air keyboard**. Built with Python, Streamlit, and the Web Audio API.

## Features

- **Real-time audio synthesis** — Multi-harmonic additive synthesis with piano-accurate ADSR envelopes
- **MacBook keyboard mapping** — Play two octaves naturally from the home row
- **5 instrument tones** — Piano, Electric Piano, Organ, Strings, Bells
- **Sustain pedal** — Hold Space to sustain notes like a real pedal
- **Room reverb** — Convolution reverb for depth and space
- **Chord detection** — Automatically identifies and names chords as you play
- **Stereo imaging** — Lower notes panned left, higher notes right
- **Live waveform visualizer**
- **Octave shifting** — Arrow keys or on-screen buttons

## Keyboard Layout

```
 Black:    W  E     T  Y  U     O  P  [
 White:   A  S  D  F  G  H  J  K  L  ;  '
          C  D  E  F  G  A  B  C  D  E  F
               (Octave 4)      (Octave 5 →)

 Lower:   Z  X  C  V  B  N  M
          C  D  E  F  G  A  B  (Octave 3)
```

| Key | Action |
|-----|--------|
| `A–J` + `W/E/T/Y/U` | Play one octave (default: Octave 4) |
| `K–;` + `O/P/[` | Play notes one octave higher |
| `Z–M` | Play notes one octave lower |
| `Space` | Sustain pedal (hold) |
| `↑ / ↓` | Shift octave up/down |

## Quick Start

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/rishky-piano.git
cd rishky-piano

# Install
pip install streamlit

# Run
streamlit run app.py
```

Or just open `piano.html` directly in any browser — zero dependencies.

## Deploy to Streamlit Cloud (Free, Permanent)

1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub, select this repo, set `app.py` as entrypoint
4. Click Deploy — you get a permanent public URL

## Files

| File | Description |
|------|-------------|
| `piano.html` | Standalone piano (HTML + CSS + JS, no dependencies) |
| `app.py` | Streamlit wrapper for web deployment |
| `requirements.txt` | Python dependencies |
| `piano_notebook.ipynb` | Jupyter notebook with inline piano + synthesis docs |

## Sound Engine

The audio engine uses the **Web Audio API** with additive synthesis:

- **Harmonics**: Fundamental + 2nd, 3rd, 4th, 6th, 8th overtones
- **ADSR**: 4ms attack, 800ms decay, 15% sustain, 1.2s release (piano profile)
- **Reverb**: Synthetic impulse response convolution
- **Compression**: Dynamics compressor prevents clipping during chords
- **Stereo spread**: Notes are panned based on pitch

## License

MIT
