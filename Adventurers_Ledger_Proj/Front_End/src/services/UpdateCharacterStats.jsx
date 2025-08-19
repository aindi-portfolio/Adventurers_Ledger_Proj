import axios from "axios";

export default async function updateCharacterStats(health, experience=0, gold=0) {
    try {
        const token = localStorage.getItem("authToken");
        const response = await axios.put('http://localhost:8000/api/character/manage-character',
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