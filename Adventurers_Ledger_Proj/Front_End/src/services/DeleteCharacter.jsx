import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_URL; // Adjust the API base URL as needed

const handleCharacterDeath = async () => {
  try {
    const token = localStorage.getItem('authToken');
    const response = await axios.delete(`${API_BASE}/character/manage-character`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}` // if you're using JWT or token-based auth
      }
    });
    console.log('Character deleted successfully:', response.data);
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.data.error);
    } else {
      console.error('Request failed:', error.message);
    }
  }
};

export default handleCharacterDeath;
