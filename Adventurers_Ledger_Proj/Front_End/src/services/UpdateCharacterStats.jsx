import axios from "axios";
import handleCharacterDeath from "./DeleteCharacter";

const API_BASE = import.meta.env.VITE_API_URL; // Adjust the API base URL as needed

export default async function updateCharacterStats(health, experience=0, gold=0) {
    try {

        if (health <= 0) {
            await handleCharacterDeath();
            return;
        }
        const token = localStorage.getItem("authToken");
        const response = await axios.put(`${API_BASE}/character/manage-character`,
        {
            "health": health,
            "experience": experience,
            "gold": gold,
        },
        {
            headers: {
                Authorization: `Token ${token}`,
                'Content-Type': 'application/json'
            }
        });
        return response.data;
    } catch (error) {
        console.log(`-----Error updating character stats:`, error)
        return
    }
}