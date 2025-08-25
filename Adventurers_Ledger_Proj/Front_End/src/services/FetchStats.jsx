import axios from "axios";

// Fetch character stats from the backend

export default async function fetchCharacterStats() {
    try {
        const API_BASE = import.meta.env.VITE_API_URL; // Adjust the API base URL as needed

        const token = localStorage.getItem('authToken');
        const response = await axios.get(`${API_BASE}/character/stats`, {
            headers: {
                Authorization: `Token ${token}`,
                'Content-Type': 'application/json'
            }
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching character stats:', error);
        return
    }
}