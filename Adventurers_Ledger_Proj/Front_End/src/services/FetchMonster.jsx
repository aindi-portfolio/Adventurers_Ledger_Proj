import axios from "axios";

const API_BASE = import.meta.env.VITE_API_URL; // Adjust the API base URL as needed


// Fetch random monster based on character level
const fetchMonster = async (characterLevel) => {
    try {
        const response = await axios.get(`${API_BASE}/monsters/${characterLevel}`);
        console.log("Monster data fetched:", response.data);
        const list_length = response.data.length;
        const random_monster = Math.floor(Math.random() * list_length);
        response.data = response.data[random_monster];
        return response.data;
    } catch (error) {
        console.error("Error fetching monster:", error);
        throw error;
    }
};

export default fetchMonster;