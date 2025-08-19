import axios from "axios";

const fetchInventory = async () => {
    try {
        const token = localStorage.getItem('authToken');
        const response = await axios.get('http://localhost:8000/api/character/inventory', {
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