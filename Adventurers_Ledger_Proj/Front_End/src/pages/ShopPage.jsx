import React, { useState, useEffect, useContext } from "react";
import { GlobalStateContext } from "../context/GlobalStateContext";
import Header from "../components/Header";
import Footer from "../components/Footer";
import fetchShopItem from "../services/FetchShopItems";
import ItemCardShop from "../components/ItemCardShop";
import ItemCardShopInventory from "../components/ItemCardShopInventory";


export default function ShopPage() {
    const { isAuthenticated, setIsAuthenticated, character, setCharacter, items, setItems } = useContext(GlobalStateContext);
    const [shopItems, setShopItems] = useState([]);
    const [itemCount, setItemCount] = useState(0);

    useEffect(() => {
        const token = localStorage.getItem('authToken');
        if (!token) {
          alert('You must be logged in to view character stats.');
          window.location.href = '/';
        } else {
          setIsAuthenticated(true);
          const count = 10 - shopItems.length;
      
          const loadItems = async () => {
            const newItems = await fetchShopItem(count);
            if (newItems) setShopItems(prev => [...prev, ...newItems]);
          };
      
          if (count > 0) loadItems();
        }
      }, [shopItems.length]);
      

    return (
        <>
            <Header />
            <div className="shop-container flex-col text-center mb-4">
                <h1>Shop</h1>
                <p>Welcome to the Adventurer's Shop!</p>
                <h2>Buy Items</h2>
            </div>
            <div className="items-list flex flex-wrap justify-center gap-6">
            {shopItems && shopItems.length > 0 ? (
                  shopItems.map((item) => (
                    <ItemCardShop key={item.name} item={item} />
                ))
            ) : (
                <p>No items available in the shop.</p>
            )}
            </div>
            <div className="flex justify-center mt-8 mb-4">
                  <h2>Sell Items</h2>
            </div>
            <div className="items-list flex flex-wrap justify-center gap-6">
              {console.log("User's inventory items:", items)}
            {items && items.length > 0 ? (
                  // Displaying items from the user's inventory by iterating through the items
                  items.map((item) => (
                        <ItemCardShopInventory key={item.name} item={item.item} />
                  ))
            ) : (
                <p>No items available in the shop.</p>
            )}
            </div>
            <Footer />
        </>
    );
}