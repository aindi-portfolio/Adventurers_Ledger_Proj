import React, { useState, useEffect, useContext } from "react";
import { GlobalStateContext } from "../context/GlobalStateContext";
import Header from "../components/Header";
import Footer from "../components/Footer";
import fetchShopItem from "../services/FetchShopItems";
import ItemCardShop from "../components/ItemCardShop";
import ItemCardShopInventory from "../components/ItemCardShopInventory";
import Layout from "../components/Layout";
import "../styles/ShopPage.css"; // Assuming you have a CSS file for styling the shop page

export default function ShopPage() {
    const { isAuthenticated, setIsAuthenticated, character, setCharacter, items, setItems } = useContext(GlobalStateContext);
    const [shopItems, setShopItems] = useState([]);
    const [itemCount, setItemCount] = useState(0);

    // Handle for fetch items from the ShotItem mode in DB
    const handleFetchShopItems = async () => {
        try {
            // Get the count of items in the shop
            // If the itemCount is less than 10, fetch items from the shop
            if (itemCount >= 10) {
                console.log("Item count is sufficient, no need to fetch more items.");
                return;
            }
            let count = 10 - itemCount; // Calculate how many items to fetch
            console.log("Fetching shop items...");
            const data = await fetchShopItem({ fetch_count: count, recycle: false });
            setShopItems(data);
            setItemCount(data.length);
            console.log("Fetched shop items:", data);
        } catch (error) {
            console.error("Error fetching shop items:", error);
        }
    };

    //Handle force fetch items from the shop
    const handleForceFetchShopItems = async () => {
        try {
            console.log("Force fetching shop items...");
            const data = await fetchShopItem({ fetch_count: 10, recycle: true });
            setShopItems(data);
            setItemCount(data.length);
            console.log("Force fetched shop items:", data);
        } catch (error) {
            console.error("Error force fetching shop items:", error);
        }
    };


    // Fetch shop items from the API when the component mounts or when the shopItems state changes
    useEffect(() => {
        handleFetchShopItems();
    }, [itemCount]);
    


    return (
        <>
        <Layout>
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
        </Layout>
        </>
    );
}