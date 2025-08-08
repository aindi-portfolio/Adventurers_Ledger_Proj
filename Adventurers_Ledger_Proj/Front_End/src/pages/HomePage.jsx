import React from "react";
import "../styles/HomePage.css";
import Header from "../components/Header";
import NavBar from "../components/NavBar";

function HomePage() {
  return (
    <>
      <Header />
      <NavBar />  
        <body className="home-body">
        </body>
        <footer className="home-footer">
            <p>&copy; 2025 Adventurer's Ledger. All rights reserved.</p>
        </footer>
    </>
  );
}

export default HomePage;