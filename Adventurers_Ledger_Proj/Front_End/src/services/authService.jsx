import axios from 'axios';

const API_BASE = 'http://localhost:8000/api/user';
const TOKEN_KEY = 'authToken';

export const Sign_Up = async (userData) => { // userData has email and password
    try {
        userData['username'] = userData.email; // applies username as email
        const response = await axios.post(`${API_BASE}/signup`, userData);
        return response.data;
    } catch (error) {
        console.error('Error during sign up:', error);
        throw error;
    }
};

export const Log_In = async (userData) => { // userData has email and password
    try {
        userData['username'] = userData.email; // applies username as email
        const response = await axios.post(`${API_BASE}/login`, userData);
        const token = response.data.token;
        localStorage.setItem(TOKEN_KEY, token); // Store token in local storage
        return token;
    } catch (error) {
        console.error('Error during login:', error);
        throw error;
    }
};

export const Log_Out = () => {
    token = localStorage.getItem(TOKEN_KEY);
    token.delete(); // Delete token from the database
    localStorage.removeItem(TOKEN_KEY); // Remove token from local storage
    Log_Out(request)
}

export const Create_Character = async (characterData) => {
    try {
        const token = localStorage.getItem(TOKEN_KEY);
        const config = {
            headers: { Authorization: `Bearer ${token}` } // Include the token in the request headers for authentication
        };
        const response = await axios.post(`${API_BASE}/create-player`, characterData, config);
        return response.data;
    } catch (error) {
        console.error('Error during character creation:', error);
        throw error;
    }
}