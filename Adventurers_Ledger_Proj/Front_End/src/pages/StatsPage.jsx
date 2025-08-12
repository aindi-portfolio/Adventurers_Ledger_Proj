import React, { useState, useEffect } from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import axios from "axios";



export default function StatsPage() {
    const [stats, setStats] = useState(null);

    // Fetch character stats from the backend
    async function fetchCharacterStats() {
        try {
            const token = localStorage.getItem('authToken');
            const response = await axios.get('http://localhost:8000/api/character/stats', {
                headers: {
                    Authorization: `Token ${token}`,
                    'Content-Type': 'application/json'
                }
            });
            console.log("Fetched stats:", response.data); // Handle the fetched stats data
            setStats(response.data);
        } catch (error) {
            console.error('Error fetching character stats:', error);
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
        // Fetch character stats when the component mounts
        fetchCharacterStats();
    }, []);


    return (
        <>
            <Header />
            <div className="stats-container">
                <h1>Character Stats</h1>
                <p>This is where your character stats will be displayed.</p>
                { stats ? (
                    <div className="stats-list grid grid-cols-2 gap-4">
                        {Object.entries(stats).map(([key, value]) => (
                            <div key={key} className="stat-item bg-yellow-100 p-4 rounded shadow">
                                <strong className="text-yellow-800">{key.replace(/_/g, ' ')}:</strong> {value}
                            </div>
                        ))}
                    </div>  
                ) : (
                    <p>Loading character stats...</p>
                )    
                }
            </div>
            <Footer />
        </>
    );
}