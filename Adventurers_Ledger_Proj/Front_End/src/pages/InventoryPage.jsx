import React, { useState, useEffect, createContext} from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import axios from "axios";

export default function Inventory() {
    const [items, setItems] = useState([]);

    // Fetch items from the API when the component mounts
    const fetchItems = async () => {
        try {
            const token = localStorage.getItem('authToken');
            const response = await axios.get('http://localhost:8000/api/character/inventory', {
                headers: {
                    authorization: `Token ${token}`,
                    'Content-Type': 'application/json'
                }
            });
            setItems(response.data);
            console.log('Fetched items:', response.data);
        } catch (error) {
            console.error('Error fetching items:', error);
        }

    }
    useEffect(() => {
        // Check if the user is authenticated
        const token = localStorage.getItem('authToken');
        if (!token) {
            // Redirect to login page if not authenticated
            alert('You must be logged in to view character stats.');
            window.location.href = '/';
        }
        fetchItems();
    }, []);

    return (
        <>
            <Header />
            <div className="inventory-container flex-col text-center">
                <h1>Inventory</h1>
                <p>This is where your items will be displayed.</p>
                {/* Future implementation for displaying items */}
                {items && items.length > 0 ? (
                    <div className="items-list grid grid-cols-2 gap-4 border-2 w-full">
                        {items.map((item) => (
                            <div key={item.id} className="item bg-yellow-100 p-4 rounded shadow">
                                <strong className="text-yellow-800">{item.item.name}</strong>
                                <img src={item.item.image_url} alt={item.item.item_type} className="w-16 h-16 object-cover mb-2" />
                                <p>{item.item.description}</p>
                                <p>Quantity: {item.quantity}</p>
                            </div>
                        ))}
                    </div>
                ) : (
                    <p>No items in inventory.</p>
                )}
            </div>
            <Footer />
        </>  
    );
}



// Create the context
export const ItemsContext = createContext();

// Create a provider component
export const ItemsProvider = ({ children }) => {
    const [items, setItems] = useState([]);

    return (
        <ItemsContext.Provider value={{ items, setItems }}>
            {children}
        </ItemsContext.Provider>
    );
}


