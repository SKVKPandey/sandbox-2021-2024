import firebase from 'firebase/app';
import 'firebase/firestore';
import 'firebase/storage';

// Initialize Firebase with your configuration
const firebaseConfig = {
    apiKey: "REDACTED",
    authDomain: "esoapp-417e0.firebaseapp.com",
    databaseURL: "https://esoapp-417e0-default-rtdb.firebaseio.com",
    projectId: "esoapp-417e0",
    storageBucket: "esoapp-417e0.appspot.com",
    messagingSenderId: "943027878273",
    appId: "1:943027878273:web:1b558dca34619ab17c5080",
    measurementId: "G-7NQ3NSW9PT"
};

firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();
const storage = firebase.storage();

const form = document.getElementById('courseForm');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const data = {};

  // Handle file uploads
  const flyerFile = formData.get('flyer');
  const backgroundImageFile = formData.get('background-image');

  try {
    // Upload images to Firebase Storage and get their download URLs
    const flyerRef = storage.ref().child('flyers/' + flyerFile.name);
    const backgroundImageRef = storage.ref().child('background_images/' + backgroundImageFile.name);

    const flyerSnapshot = await flyerRef.put(flyerFile);
    const backgroundImageSnapshot = await backgroundImageRef.put(backgroundImageFile);

    const flyerUrl = await flyerSnapshot.ref.getDownloadURL();
    const backgroundImageUrl = await backgroundImageSnapshot.ref.getDownloadURL();

    // Store the download URLs in the data object
    data['flyerUrl'] = flyerUrl;
    data['backgroundImageUrl'] = backgroundImageUrl;
  } catch (error) {
    console.error('Error uploading images to Firebase Storage: ', error);
    return;
  }

  // Store the rest of the form data
  formData.forEach((value, key) => {
    if (key !== 'flyer' && key !== 'background-image') {
      data[key] = value;
    }
  });

  // Save the data to the Firebase collection 'courses'
  db.collection('courses')
    .add(data)
    .then(() => {
      console.log('Data successfully sent to Firebase.');
    })
    .catch((error) => {
      console.error('Error sending data to Firebase: ', error);
    });
});