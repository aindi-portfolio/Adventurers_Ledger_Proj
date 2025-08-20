import axios from "axios";
// This component is responsible for handling the purchase logic for the item selected.
export default async function Buy_or_Sell_Item(action, item ) {
    const token = localStorage.getItem('authToken');
        try {
            if (action === "buy") {
                const response = await axios.put(
                    'http://localhost:8000/api/character/inventory/',
                    {
                        "item_name": item,
                        "quantity": 1
                    },
                    {
                        headers:
                            { Authorization: `Bearer ${token}`,
                            "Content-Type": "application/json" }
                    }
                );
                if (response.status === 200) {
                    alert(`You have successfully bought ${item.name}!`);
                    // Optionally, you can refresh the page or update the state to reflect the new inventory.
                }
            }
            else if (action === "sell") {
                const response = await axios.put(
                    'http://localhost:8000/api/character/inventory/',
                    {
                        "item_name": item,
                        "quantity": -1 // Negative quantity to indicate selling
                    },
                    {
                        headers: {
                            Authorization: `Bearer ${token}`,
                            "Content-Type": "application/json"
                        },
                    }
                );
                if (response.status === 200) {
                    alert(`You have successfully sold ${item.name}!`);
                    // Optionally, you can refresh the page or update the state to reflect the new inventory.
                }
            } else {
                console.error("Invalid action. Use 'buy' or 'sell'.");
            }
            
        } catch (error) {
            console.error("Error buying item:", error);
            alert("Failed to buy item. Please try again.");
        }
};