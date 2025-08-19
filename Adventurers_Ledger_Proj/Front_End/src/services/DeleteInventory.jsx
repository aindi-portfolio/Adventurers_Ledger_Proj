import axios from 'axios';

const handleCharacterDeath = async () => {
  try {
    const response = await axios.delete('http://localhost:8000/api/inventory/death/', {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${yourAuthToken}` // if you're using JWT or token-based auth
      }
    });

    console.log('Inventory cleared:', response.data.message);
    // Optionally trigger UI updates, redirect, or show a toast
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.data.error);
    } else {
      console.error('Request failed:', error.message);
    }
  }
};
