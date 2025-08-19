import axios from "axios";
// This component is responsible for handling the purchase logic for the item selected.
export default async function BuyItem( item ) {
    const token = localStorage.getItem('authToken');
        try {
            const response = await axios.post(
                'http://localhost:8000/api/character/inventory/',
                { "item_name": item },
                { headers:
                    { Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json" }
                }
            );
            if (response.status === 200) {
                alert(`You have successfully bought ${item.name}!`);
                // Optionally, you can refresh the page or update the state to reflect the new inventory.
            }
        } catch (error) {
            console.error("Error buying item:", error);
            alert("Failed to buy item. Please try again.");
        }
};