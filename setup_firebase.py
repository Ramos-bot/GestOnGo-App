#!/usr/bin/env python3
"""
Firebase integration setup for GestOnGo
Run this script to initialize Firebase configuration
"""

import json
import os
import sys
from pathlib import Path

def create_firebase_config():
    """Create Firebase configuration files"""
    
    # Check if Firebase CLI is available
    if os.system("firebase --version") != 0:
        print("❌ Firebase CLI not found. Install with: npm install -g firebase-tools")
        return False
    
    print("🔥 Setting up Firebase for GestOnGo...")
    
    # Initialize Firebase project
    print("\n1. Initializing Firebase project...")
    os.system("firebase init")
    
    # Create Firebase configuration template
    firebase_config = {
        "hosting": {
            "public": "frontend/dist",
            "ignore": [
                "firebase.json",
                "**/.*",
                "**/node_modules/**"
            ],
            "rewrites": [
                {
                    "source": "**",
                    "destination": "/index.html"
                }
            ]
        },
        "functions": {
            "source": "functions",
            "runtime": "python311"
        },
        "firestore": {
            "rules": "firestore.rules",
            "indexes": "firestore.indexes.json"
        }
    }
    
    # Write firebase.json if it doesn't exist
    if not os.path.exists("firebase.json"):
        with open("firebase.json", "w") as f:
            json.dump(firebase_config, f, indent=2)
        print("✅ Created firebase.json configuration")
    
    # Create Firestore rules
    firestore_rules = """rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users can only access their own data
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    
    // Clients data (requires authentication)
    match /clientes/{clienteId} {
      allow read, write: if request.auth != null;
    }
    
    // Services data (requires authentication)
    match /servicos/{servicoId} {
      allow read, write: if request.auth != null;
    }
  }
}"""
    
    if not os.path.exists("firestore.rules"):
        with open("firestore.rules", "w") as f:
            f.write(firestore_rules)
        print("✅ Created firestore.rules")
    
    # Create Firestore indexes
    firestore_indexes = {
        "indexes": [],
        "fieldOverrides": []
    }
    
    if not os.path.exists("firestore.indexes.json"):
        with open("firestore.indexes.json", "w") as f:
            json.dump(firestore_indexes, f, indent=2)
        print("✅ Created firestore.indexes.json")
    
    # Create frontend Firebase config
    frontend_firebase = """// Firebase configuration for GestOnGo
import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
import { getStorage } from 'firebase/storage';

const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID,
  appId: import.meta.env.VITE_FIREBASE_APP_ID,
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firebase services
export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);

export default app;
"""
    
    os.makedirs("frontend/src", exist_ok=True)
    with open("frontend/src/firebase.js", "w") as f:
        f.write(frontend_firebase)
    print("✅ Created frontend/src/firebase.js")
    
    print("\n🎉 Firebase setup complete!")
    print("\nNext steps:")
    print("1. Update your .env files with Firebase credentials")
    print("2. Run 'firebase deploy' to deploy your app")
    print("3. Configure authentication providers in Firebase Console")
    
    return True

def setup_firebase_auth():
    """Setup Firebase Authentication helper functions"""
    
    auth_service = """// Firebase Authentication service
import { 
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signOut,
  onAuthStateChanged 
} from 'firebase/auth';
import { auth } from './firebase';

export const authService = {
  // Sign in with email and password
  async signIn(email, password) {
    try {
      const userCredential = await signInWithEmailAndPassword(auth, email, password);
      return { user: userCredential.user, error: null };
    } catch (error) {
      return { user: null, error: error.message };
    }
  },

  // Sign up with email and password
  async signUp(email, password) {
    try {
      const userCredential = await createUserWithEmailAndPassword(auth, email, password);
      return { user: userCredential.user, error: null };
    } catch (error) {
      return { user: null, error: error.message };
    }
  },

  // Sign out
  async signOut() {
    try {
      await signOut(auth);
      return { error: null };
    } catch (error) {
      return { error: error.message };
    }
  },

  // Listen to auth state changes
  onAuthStateChanged(callback) {
    return onAuthStateChanged(auth, callback);
  },

  // Get current user
  getCurrentUser() {
    return auth.currentUser;
  },

  // Get auth token
  async getIdToken() {
    const user = auth.currentUser;
    if (user) {
      return await user.getIdToken();
    }
    return null;
  }
};
"""
    
    with open("frontend/src/authService.js", "w") as f:
        f.write(auth_service)
    print("✅ Created frontend/src/authService.js")

if __name__ == "__main__":
    print("🚀 GestOnGo Firebase Setup")
    print("=" * 50)
    
    if create_firebase_config():
        setup_firebase_auth()
        print("\n✨ Firebase integration ready!")
    else:
        print("\n❌ Firebase setup failed. Please install Firebase CLI first.")
        sys.exit(1)
