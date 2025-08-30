# SoundFont for Samplers

MP3 files converted from different SoundFonts that can be used in samplers and music applications.

## Update 2025-08-29 (v0.0.3)

- added instruments:
```
Bright Acoustic Piano - bright_acoustic_piano
Electric Grand Piano - electric_grand_piano
Marimba - marimba
Accordion - accordion
Harmonica - harmonica
Acoustic Bass - acoustic_bass
Synth Bass 1 - synth_bass_1
String Ensemble 2 - string_ensemble_2
Tuba - tuba
Soprano Sax - soprano_sax
Baritone Sax - baritone_sax
Oboe - oboe
English Horn - english_horn
Bassoon - bassoon
Piccolo - piccolo
Shakuhachi - shakuhachi
Pad 4 (choir) - pad_4_choir
Pad 5 (bowed glass) - pad_5_bowed
Pad 6 (metallic) - pad_6_metallic
Pad 7 (halo) - pad_7_halo
Pad 8 (sweep) - pad_8_sweep
FX 1 (rain) - fx_1_rain
FX 2 (soundtrack) - fx_2_soundtrack
FX 3 (crystal) - fx_3_crystal
FX 5 (brightness) - fx_5_brightness
FX 6 (goblins) - fx_6_goblins
FX 7 (echoes) - fx_7_echoes
FX 8 (sci-fi) - fx_8_scifi
```

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