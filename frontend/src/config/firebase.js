// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: import.meta.env.VITE_FIREBASE_API_KEY || "AIzaSyB0PxRHDzPPq6EcSpiMMwirWWfwUhBmamQ",
    authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN || "gestongo-app.firebaseapp.com",
    projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID || "gestongo-app",
    storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET || "gestongo-app.firebasestorage.app",
    messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID || "49732729437",
    appId: import.meta.env.VITE_FIREBASE_APP_ID || "1:49732729437:web:4f20a0600cbe8a66472bb4",
    measurementId: import.meta.env.VITE_FIREBASE_MEASUREMENT_ID || "G-E2N9HME0FQ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firebase services
export const analytics = getAnalytics(app);
export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);

export default app;
