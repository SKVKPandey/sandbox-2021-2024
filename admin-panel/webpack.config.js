const path = require('path');

module.exports = {
  mode: 'development',
  entry: './renderer.js',
  target: 'electron-renderer', // Set the target to Electron's renderer process
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        },
      },
    ],
  },
};
