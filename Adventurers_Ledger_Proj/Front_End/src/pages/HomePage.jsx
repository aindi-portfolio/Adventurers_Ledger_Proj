import React from "react";
import "../styles/HomePage.css";
import Header from "../components/Header";
import NavBar from "../components/NavBar";
import Layout from "../components/Layout";


function HomePage() {
  

  return (
    <>
      <Layout>
      <Header />
      <NavBar />
      </Layout> 
    </>
  );
}

export default HomePage;