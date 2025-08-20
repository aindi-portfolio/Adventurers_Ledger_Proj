import axios from "axios";

const fetchShopItem = async (fetch_count=1) => {
    try {
        const token = localStorage.getItem('authToken');
        const response = await axios.post('http://localhost:8000/api/items/add-to-shop',
            {
                "count": fetch_count,
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