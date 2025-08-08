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
    token = Token.objects.get(user=request.user);
    token.delete(); // Delete token from the database
    localStorage.removeItem(TOKEN_KEY); // Remove token from local storage
    Log_Out(request)
}