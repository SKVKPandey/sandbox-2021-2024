// app.js

const electron = require('electron');
const magenta = require('@magenta/music');
const tone = require('tone');

// Create a new Electron app
const app = electron.app;

// Wait for the app to be ready
app.on('ready', async () => {
  // Create a new window
  const win = new electron.BrowserWindow({
    width: 800,
    height: 600,
  });

  // Initialize Magenta
  await magenta.initialize();

  // Create a new MusicVAE model
  const model = new magenta.MusicVAE('https://storage.googleapis.com/magentadata/js/checkpoints/music_vae/mel_4bar_small');

  // Create a new Tone.js player
  const player = new tone.Player();

  // Create a function to generate music
  function generateMusic() {
    // Generate a new melody
    model.sample(1).then((samples) => {
      const melody = samples[0].notes.map((note) => ({
        pitch: note.pitch,
        quantizedStartStep: note.quantizedStartStep,
        quantizedEndStep: note.quantizedEndStep,
        velocity: note.velocity,
      }));

      // Play the melody
      player.dispose();
      player.toDestination();
      player.sync().start(0, 0, undefined, 0, melody);
    });
  }

  // Wait for the window to finish loading
  win.webContents.on('did-finish-load', () => {
    // Add a button to the window that will generate music
    win.webContents.addListener('click', (event) => {
      if (event.button === 0) {
        generateMusic();
      }
    });

    // Show the window
    win.show();
  });

  // Load the index.html file
  win.loadFile('index.html');
});

// Export the app
module.exports = app;
