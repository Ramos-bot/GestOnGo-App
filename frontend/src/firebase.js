/**
 * Configuração Firebase para GestOnGo
 * 
 * Este ficheiro contém a configuração para integração com Firebase,
 * permitindo autenticação, Firestore para dados em tempo real,
 * e Storage para ficheiros.
 * 
 * Para activar Firebase:
 * 1. npm install firebase
 * 2. Configurar projeto no console Firebase
 * 3. Substituir a configuração abaixo pelas suas credenciais
 * 4. Descomentar as importações e inicialização
 */

// import { initializeApp } from 'firebase/app';
// import { getAuth } from 'firebase/auth';
// import { getFirestore } from 'firebase/firestore';
// import { getStorage } from 'firebase/storage';

// Configuração Firebase (substituir pelos valores reais)
const firebaseConfig = {
    apiKey: "your-api-key",
    authDomain: "gestongo-app.firebaseapp.com",
    projectId: "gestongo-app",
    storageBucket: "gestongo-app.appspot.com",
    messagingSenderId: "123456789",
    appId: "1:123456789:web:abcdef123456"
};

// Inicialização Firebase (descomentar quando configurado)
// const app = initializeApp(firebaseConfig);

// Serviços Firebase
// export const auth = getAuth(app);
// export const db = getFirestore(app);
// export const storage = getStorage(app);

// Funções auxiliares para autenticação Firebase
/*
import { 
    signInWithEmailAndPassword,
    createUserWithEmailAndPassword,
    signOut,
    onAuthStateChanged 
} from 'firebase/auth';

export const loginWithFirebase = async (email, password) => {
    try {
        const userCredential = await signInWithEmailAndPassword(auth, email, password);
        return userCredential.user;
    } catch (error) {
        throw new Error('Erro no login Firebase: ' + error.message);
    }
};

export const registerWithFirebase = async (email, password) => {
    try {
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        return userCredential.user;
    } catch (error) {
        throw new Error('Erro no registo Firebase: ' + error.message);
    }
};

export const logoutFromFirebase = async () => {
    try {
        await signOut(auth);
    } catch (error) {
        throw new Error('Erro no logout Firebase: ' + error.message);
    }
};

export const onAuthStateChangedListener = (callback) => {
    return onAuthStateChanged(auth, callback);
};
*/

// Funções auxiliares para Firestore
/*
import { 
    collection, 
    addDoc, 
    getDocs, 
    doc, 
    updateDoc, 
    deleteDoc,
    query,
    where,
    orderBy 
} from 'firebase/firestore';

export const adicionarCliente = async (clienteData) => {
    try {
        const docRef = await addDoc(collection(db, 'clientes'), {
            ...clienteData,
            dataCriacao: new Date()
        });
        return docRef.id;
    } catch (error) {
        throw new Error('Erro ao adicionar cliente: ' + error.message);
    }
};

export const obterClientes = async () => {
    try {
        const querySnapshot = await getDocs(collection(db, 'clientes'));
        return querySnapshot.docs.map(doc => ({
            id: doc.id,
            ...doc.data()
        }));
    } catch (error) {
        throw new Error('Erro ao obter clientes: ' + error.message);
    }
};

export const adicionarServico = async (servicoData) => {
    try {
        const docRef = await addDoc(collection(db, 'servicos'), {
            ...servicoData,
            dataCriacao: new Date(),
            status: 'agendado'
        });
        return docRef.id;
    } catch (error) {
        throw new Error('Erro ao adicionar serviço: ' + error.message);
    }
};

export const obterServicos = async () => {
    try {
        const q = query(
            collection(db, 'servicos'),
            orderBy('dataServico', 'desc')
        );
        const querySnapshot = await getDocs(q);
        return querySnapshot.docs.map(doc => ({
            id: doc.id,
            ...doc.data()
        }));
    } catch (error) {
        throw new Error('Erro ao obter serviços: ' + error.message);
    }
};
*/

export default firebaseConfig;
