import axios from "axios";

const API_BASE = import.meta.env.VITE_API_URL; // Adjust the API base URL as needed


const SeedItems = async () => {

    try {
    const response = await axios.post(`${API_BASE}/items/seed`, {}, {
        headers: {
        Authorization: `Token ${localStorage.getItem("authToken")}`,
        "Content-Type": "application/json",
        },
    });
    console.log("Items seeded:", response.data);
    } catch (err) {
        console.error("Error seeding items:", err);
    }
};


const SeedMonsters = async (character_level) => {
    try {
        const response = await axios.post(`${API_BASE}/monsters/seed-monsters`, {
            character_level: character_level,
        }, {
            headers: {
                Authorization: `Token ${localStorage.getItem("authToken")}`,
                "Content-Type": "application/json",
            },
        });
        // console.log("Monsters seeded:", response.data);
    } catch (err) {
        console.error("Error seeding monsters:", err);
    }
}

export {SeedItems, SeedMonsters};