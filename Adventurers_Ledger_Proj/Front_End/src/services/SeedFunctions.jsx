import axios from "axios";

const SeedItems = async () => {

    try {
    const response = await axios.post("http://localhost:8000/api/items/seed", {}, {
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