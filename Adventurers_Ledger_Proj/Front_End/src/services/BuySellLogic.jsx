import axios from "axios";
// This component is responsible for handling the purchase logic for the item selected.
const API_BASE = import.meta.env.VITE_API_URL; // Adjust the API base URL as needed
export default async function Buy_or_Sell_Item(action, item ) {
    const token = localStorage.getItem('authToken');
    try {
            let quantity = action === "buy" ? 1 : action === "sell" ? -1 : 0;
            if (quantity === 0) {
                console.error("Invalid action. Use 'buy' or 'sell'.");
                return;
            }
            
            const response = await axios.put(
                `${API_BASE}/character/inventory`,
                {
                    "item_name": item.name,
                    "quantity": quantity
                },
                {
                    headers:
                        { Authorization: `Token ${token}`,
                        "Content-Type": "application/json" }
                }
            );
            console.log("Response from server:", response.data);
            console.log(`Status code: ${response.status}`);
            if (response.status === 200) {
                alert(`You have successfully ${action === "buy" ? "bought" : "sold"} ${item.name}!`);
            } else {
                console.error("Invalid action. Use 'buy' or 'sell'.");
            }
    } catch (error) {
        console.error(`Error trying to ${action} item:`, error);
        alert(`Failed to ${action} ${item.name}. Please try again.`);
    }
}