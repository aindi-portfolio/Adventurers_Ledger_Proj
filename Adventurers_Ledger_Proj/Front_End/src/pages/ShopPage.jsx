import React, { useState, useEffect, useContext } from "react";
import { GlobalStateContext } from "../context/GlobalStateContext";
import Header from "../components/Header";
import Footer from "../components/Footer";


export default function ShopPage() {
    const { isAuthenticated, setIsAuthenticated, character, setCharacter, items, setItems } = useContext(GlobalStateContext);

    return (
        <>
            <Header />
            <h1>Shop</h1>
            <p>This is where you can buy items.</p>
            {/* Future implementation for shop functionality */}
            <Footer />
        </>
    );
}