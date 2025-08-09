import React, { useState, useEffect} from "react";
import Header from "../components/Header";

export default function Inventory() {
    const [items, setItems] = useState([]);

    const API_BASE = "http://localhost:8000/api/";

    useEffect(() => {
        fetch("")
    return (
        <>
            <Header />
            <h1>Inventory</h1>
            <div className="inventory-container">
                
            </div>
        </>
    );
    })
}