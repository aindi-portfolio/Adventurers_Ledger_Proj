import axios from "axios";

const fetchShopItem = async (fetch_count=1, recycle=false) => {
    try {
        const API_BASE = import.meta.env.VITE_API_URL; // Adjust the API base URL as needed

        const token = localStorage.getItem('authToken');
        const response = await axios.post(`${API_BASE}/items/add-to-shop`,
            {
                "count": fetch_count,
                "recycle": recycle
            },
            {
            headers: {
                authorization: `Token ${token}`,
                'Content-Type': 'application/json'
            }
        });
        console.log('Fetched items:', response.data);
        
        return response.data;
    } catch (error) {
        console.error('Error fetching items:', error);
    }
}

export default fetchShopItem;