// SeedEquipmentButton.jsx
import React, { useState } from "react";
import axios from "axios";

const SeedEquipmentButton = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSeed = async () => {
    setLoading(true);
    setError("");
    try {
      const response = await axios.post("http://localhost:8000/api/items/seed-weapons", {
        headers: {
          Authorization: `Token ${localStorage.getItem("authToken")}`,
          "Content-Type": "application/json",
        },
      });
    } catch (err) {
      setError("Seeding failed. Check server logs.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "1rem", border: "1px solid #ccc" }}>
      <button onClick={handleSeed} disabled={loading}>
        {loading ? "Seeding..." : "Seed Equipment"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

    </div>
  );
};

export default SeedEquipmentButton;
