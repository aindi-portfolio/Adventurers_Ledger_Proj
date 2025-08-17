import axios from "axios";

const SeedItems = async () => {

    try {
    const response_weapons = await axios.post("http://localhost:8000/api/items/seed-weapons", {}, {
        headers: {
        Authorization: `Token ${localStorage.getItem("authToken")}`,
        "Content-Type": "application/json",
        },
    });

    const response_armor = await axios.post("http://localhost:8000/api/items/seed-armor", {}, {
        headers: {
        Authorization: `Token ${localStorage.getItem("authToken")}`,
        "Content-Type": "application/json",
        },
    });
    } catch (err) {
        console.error("Error seeding items:", err);
    }
};


const SeedMonsters = async (challenge_rating) => {
    try {
        const response = await axios.post("http://localhost:8000/api/monsters/seed-monsters", {
            challenge_rating: challenge_rating,
        }, {
            headers: {
                Authorization: `Token ${localStorage.getItem("authToken")}`,
                "Content-Type": "application/json",
            },
        });
        console.log("Monsters seeded:", response.data);
    } catch (err) {
        console.error("Error seeding monsters:", err);
    }
}

export {SeedItems, SeedMonsters};