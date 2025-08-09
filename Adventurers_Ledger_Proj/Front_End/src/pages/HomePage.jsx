import React from "react";
import "../styles/HomePage.css";
import Header from "../components/Header";
import NavBar from "../components/NavBar";
import Footer from "../components/Footer";

function HomePage() {
  return (
    <>
      <Header />
      <NavBar />  
        <body className="home-body">
        </body>
      <Footer />
    </>
  );
}

export default HomePage;