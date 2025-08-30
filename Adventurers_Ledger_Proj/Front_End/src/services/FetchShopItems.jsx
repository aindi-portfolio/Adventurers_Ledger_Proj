import axios from "axios";

const fetchShopItem = async (fetch_count=1, recycle=false) => {
    try {
        const token = localStorage.getItem('authToken');
        console.log('Fetching items with count:', fetch_count, 'and recycle:', recycle);
        const response = await axios.post('http://localhost:8000/api/items/add-to-shop',
            {
                "fetch_count": fetch_count,
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