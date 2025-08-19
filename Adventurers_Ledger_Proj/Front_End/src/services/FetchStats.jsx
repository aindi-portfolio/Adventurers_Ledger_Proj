import axios from "axios";

// Fetch character stats from the backend

export default async function fetchCharacterStats() {
    try {
        const token = localStorage.getItem('authToken');
        const response = await axios.get('http://localhost:8000/api/character/stats', {
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