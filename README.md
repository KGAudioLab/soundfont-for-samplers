# SoundFont for Samplers

MP3 files converted from different SoundFonts that can be used in samplers and music applications.

## Installation

```bash
npm install soundfont-for-samplers
```

## Usage

```javascript
const soundfont = require('soundfont-for-samplers');

// Get all available instruments
const instruments = soundfont.getInstrumentNames();
console.log(instruments); // ['acoustic_grand_piano', 'accordion', ...]

// Get local file paths for an instrument
const pianoFiles = soundfont.getInstrumentFiles('acoustic_grand_piano');

// Get CDN URL for a specific note (provide your own CDN URL)
const cdnUrl = 'https://your-cdn.com/soundfonts/';
const pianoC4 = soundfont.getInstrumentNoteURL(cdnUrl, 'acoustic_grand_piano', 'C4');
```

## Available Soundfonts

### FluidR3 General MIDI
- **Source**: Generated from [FluidR3_GM.sf2](http://www.synthfont.com/SoundFonts/FluidR3_GM.sfArk)
- **License**: MIT License
- **Instruments**: 139 General MIDI instruments plus percussion kits
- **Format**: Individual MP3 files for each note (C1-C8)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Attribution

This project contains MP3 files converted from the FluidR3 SoundFont by Frank Wen, and is inspired by the conversion approach from the midi-js-soundfonts project by Benjamin Gleitzman. Both original works are used under their respective MIT licenses.