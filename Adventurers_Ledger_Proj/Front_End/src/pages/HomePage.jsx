import React from "react";
import "../styles/HomePage.css";
import NavBar from "../components/NavBar";

function HomePage() {
  return (
    <>
        <header className="home-header">
            <h1>Welcome to the Adventurer's Ledger</h1>
            <NavBar />
        </header>
        <body className="home-body">
        </body>
        <footer className="home-footer">
            <p>&copy; 2025 Adventurer's Ledger. All rights reserved.</p>
        </footer>
    </>
  );
}

export default HomePage;