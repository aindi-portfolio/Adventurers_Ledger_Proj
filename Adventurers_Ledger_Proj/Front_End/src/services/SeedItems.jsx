import axios from "axios";

const SeedItems = async () => {
    setLoading(true);
    setError("");
    try {
    const response_weapons = await axios.post("http://localhost:8000/api/items/seed-weapons", {
        headers: {
        Authorization: `Token ${localStorage.getItem("authToken")}`,
        "Content-Type": "application/json",
        },
    });
    const response_armor = await axios.post("http://localhost:8000/api/items/seed-armor", {
        headers: {
        Authorization: `Token ${localStorage.getItem("authToken")}`,
        "Content-Type": "application/json",
        },
    });
    } catch (err) {
    setError("Seeding failed. Check server logs.");
    }
};

export default SeedItems;