import axios from "axios";

const fetchInventory = async () => {
    try {
        const API_BASE = import.meta.env.VITE_API_URL; // Adjust the API base URL as needed

        const token = localStorage.getItem('authToken');
        const response = await axios.get(`${API_BASE}/character/inventory`, {
            headers: {
                authorization: `Token ${token}`,
                'Content-Type': 'application/json'
            }
        });
        // console.log('Fetched items:', response.data);
        return response.data;
    } catch (error) {
        console.error('Error fetching items:', error);
    }

}

export default fetchInventory;