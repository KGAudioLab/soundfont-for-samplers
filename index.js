const path = require('path');
const fs = require('fs');

// Load instrument names
const instrumentNames = require('./FluidR3_GM/names.json');

/**
 * Get the list of all available instruments
 * @returns {string[]} Array of instrument names
 */
function getInstrumentNames() {
  return instrumentNames;
}

/**
 * Get the path to a specific instrument's MP3 directory
 * @param {string} instrumentName - Name of the instrument
 * @returns {string} Path to the instrument's MP3 directory
 */
function getInstrumentPath(instrumentName) {
  if (!instrumentNames.includes(instrumentName)) {
    throw new Error(`Instrument "${instrumentName}" not found. Available instruments: ${instrumentNames.join(', ')}`);
  }
  return path.join(__dirname, 'FluidR3_GM', `${instrumentName}-mp3`);
}

/**
 * Get all MP3 files for a specific instrument
 * @param {string} instrumentName - Name of the instrument
 * @returns {string[]} Array of MP3 file paths for the instrument
 */
function getInstrumentFiles(instrumentName) {
  const instrumentPath = getInstrumentPath(instrumentName);
  
  if (!fs.existsSync(instrumentPath)) {
    throw new Error(`Instrument directory not found: ${instrumentPath}`);
  }
  
  const files = fs.readdirSync(instrumentPath)
    .filter(file => file.endsWith('.mp3'))
    .map(file => path.join(instrumentPath, file));
  
  return files;
}

/**
 * Get CDN URL for a specific instrument note
 * @param {string} cdnPrefix - Base URL for your CDN (e.g., 'https://your-cdn.com/soundfonts/')
 * @param {string} instrumentName - Name of the instrument
 * @param {string} note - Note name (e.g., 'C4', 'A#3')
 * @returns {string} CDN URL for the MP3 file
 */
function getInstrumentNoteURL(cdnPrefix, instrumentName, note) {
  if (!instrumentNames.includes(instrumentName)) {
    throw new Error(`Instrument "${instrumentName}" not found`);
  }
  
  // Ensure CDN prefix ends with a slash
  const normalizedPrefix = cdnPrefix.endsWith('/') ? cdnPrefix : `${cdnPrefix}/`;
  
  // Convert note format (A#3 -> Ab3, etc.)
  const normalizedNote = note.replace('#', 'b');
  return `${normalizedPrefix}FluidR3_GM/${instrumentName}-mp3/${normalizedNote}.mp3`;
}

module.exports = {
  instrumentNames,
  getInstrumentNames,
  getInstrumentPath,
  getInstrumentFiles,
  getInstrumentNoteURL
};