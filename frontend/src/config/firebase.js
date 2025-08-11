// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB0PxRHDzPPq6EcSpiMMwirWWfwUhBmamQ",
  authDomain: "gestongo-app.firebaseapp.com",
  projectId: "gestongo-app",
  storageBucket: "gestongo-app.firebasestorage.app",
  messagingSenderId: "49732729437",
  appId: "1:49732729437:web:4f20a0600cbe8a66472bb4",
  measurementId: "G-E2N9HME0FQ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firebase services
export const analytics = getAnalytics(app);
export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);

export default app;
