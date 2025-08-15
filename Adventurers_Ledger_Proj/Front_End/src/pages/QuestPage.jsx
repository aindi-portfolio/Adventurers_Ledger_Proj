import React, { useState, useEffect } from "react";
import axios from "axios";
import Header from "../components/Header";
import Footer from "../components/Footer";

const QuestPage = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [loading, setLoading] = useState(false);
  const [quest, setQuest] = useState(null); // quest data from the DB
  const [genQuest, setGenQuest] = useState(null); // from 3rd party API

  const API_BASE = "http://localhost:8000/api";

  // Fetch quest from the DB
  const fetchQuestDB = async () => {
    try {

      const res = await axios.get(`${API_BASE}/quests`);
      // console.log("Fetched quest from DB:", res.data.quest);
      setQuest(res.data.quest);
      console.log("Fetched quest:", res.data.quest);
    } catch (err) {
      console.error("Failed to fetch quest:", err);
    }
  };

  // This posts information to back-end and back-end calls from 3rd party API with that info
  const fetchGenQuest = async (quest) => {
    try {
      const token = localStorage.getItem("authToken");
      console.log("quest:", quest); // Debugging line to check quest data
      const res = await axios.post(
        `${API_BASE}/quests/gen-quest`,
        quest,
        {
          headers: {
            Authorization: `Token ${token}`,
            "Content-Type": "application/json",
          },
        }
      );
      setGenQuest(res.data.quest);
      console.log("Fetched generated quest:", res.data.quest);
    } catch (err) {
      console.error("Failed to fetch generated quest:", err);
    } 
  }

  useEffect(() => {
    const token = localStorage.getItem('authToken');
    setIsAuthenticated(!!token);
  }, []);

  useEffect(() => {
    if (quest) return;
    fetchQuestDB();
  }, []);

  const restartQuest = () => {
    setQuest(null);
    fetchQuestDB();
  };

  return (
    <>
      <Header />
      <div className="quest-page text-center p-6">
        {isAuthenticated ? (
          quest ? ( //-------- if quest exists, display it
            <>
              <h2 className="text-2xl font-bold mb-2">{quest.title}</h2>
              <p className="mb-2">{quest.description}</p>
              <p className="text-sm mb-1">Reward Experience: {quest.reward_experience}</p>
              <p className="text-sm mb-4">Reward: {quest.reward_item}</p>
  
              {!genQuest ? (
                <>
                  <button
                  className="mt-4 px-4 py-2 bg-blue-600 text-white rounded"
                  onClick={() => fetchGenQuest(quest)}
                  >
                    Accept
                  </button>
                  <button
                    className="mt-4 px-4 py-2 bg-red-400 text-white rounded"
                    onClick={restartQuest}
                  >
                    Explore Another Quest
                  </button>
                </> 
                ) : (
                <>
                <div className="mt-4">
                  <h3 className="text-xl font-semibold mb-2">Some time after accepting...</h3>
                  <p>{genQuest.description}</p>
                  <p className="mt-2">{genQuest}</p>
                </div>
                </>
                )
              }
            </>
          ) : (
            <p>Loading quest...</p>
          )
          ) : (<p>Please log in to view and accept quests.</p>)
        }
        
      </div>
      <Footer />
    </>
  );
};

export default QuestPage;
