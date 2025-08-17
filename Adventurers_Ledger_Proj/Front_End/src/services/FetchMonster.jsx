import axios from "axios";
import calculate_valid_cr_to_level from "../utils/calculate_valid_cr_to_level";

BASE_API = 'http://localhost:8000/api'

// Fetch random monster based on character level
export const fetchMonster = async (characterLevel) => {
    try {
        // Calculate valid challenge ratings based on character level
        cr_list = calculate_valid_cr_to_level(characterLevel);
        console.log("Valid CRs for character level ", characterLevel, ": ", cr_list);
        random_cr = cr_list[Math.floor(Math.random() * cr_list.length)];
        console.log("Random CR selected: ", random_cr);

        const response = await axios.get(`${BASE_API}/monsters/${random_cr}`);
        if (response.data.results && response.data.results.length > 0) {
            const randomIndex = Math.floor(Math.random() * response.data.results.length);
            const monster = response.data.results[randomIndex];
            return monster;
        } else {
            throw new Error("No monsters found for the given character level.");
        }
    } catch (error) {
        console.error("Error fetching monster:", error);
        throw error;
    }
};