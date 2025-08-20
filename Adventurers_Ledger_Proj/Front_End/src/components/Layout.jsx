import React from "react";
import Footer from "./Footer";

export default function Layout({ children }) {
  return (
    <div className="bg-parchment min-h-screen text-textmain font-body">
      <header className="bg-wood text-gold font-heading p-4 drop-shadow-fantasy">
        <h1 className="text-3xl text-center">Adventurer's Ledger</h1>
      </header>
      <main className="p-6">{children}</main>
        <Footer />
    </div>
  );
}