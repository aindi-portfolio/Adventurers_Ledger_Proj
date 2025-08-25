import axios from "axios";

const API_BASE = import.meta.env.VITE_API_URL; // Adjust the API base URL as needed

const Sign_Up = async (userData) => { // userData has email and password
    try {
        
        const response = await axios.post(`${API_BASE}/user/signup`, userData);
        return response.data;
    } catch (error) {
        console.error('Error during sign up:', error);
        throw error;
    }
  };
  
  const Log_In = async (userData) => { // userData has email and password
    try {
        userData['username'] = userData.email; // applies username as email
        const response = await axios.post(`${API_BASE}/user/login`, userData);
        const token = response.data.token;
        localStorage.setItem('authToken', token); // Store token in local storage
        return token;
    } catch (error) {
        console.error('Error during login:', error);
        throw error;
    }
  };
  
const Log_Out = () => {
    localStorage.removeItem("authToken"); // Remove token from local storage
  }

  export { Sign_Up, Log_In, Log_Out };