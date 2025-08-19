import React, { useState, useEffect, useContext } from "react";
import { GlobalStateContext } from "../context/GlobalStateContext";
import axios from "axios";
import Header from "../components/Header";
import Footer from "../components/Footer";

const QuestPage = () => {
  const { character, setCharacter, isAuthenticated, setIsAuthenticated } = useContext(GlobalStateContext);
  const [loading, setLoading] = useState(false);
  const [quest, setQuest] = useState(null); // quest data from the DB
  const [storyIntro, setStoryIntro] = useState(null); // from 3rd party API
  const [questFinally, setQuestFinally] = useState(null); // final quest data after player choices

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
      // console.log("quest:", quest); // Debugging line to check quest data
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
      setStoryIntro(res.data.quest);
      console.log("Fetched generated quest:", res.data.quest);
    } catch (err) {
      console.error("Failed to fetch generated quest:", err);
    } 
  }
  
  // Advance quest based on player choice
  const advanceQuest = async (player_choice) => {
    try {
      const token = localStorage.getItem("authToken");
      const res = await axios.post(
        `${API_BASE}/quests/advance-quest`,
        {
          quest: storyIntro,
          choice: player_choice
        },
        {
          headers: {
            Authorization: `Token ${token}`,
            "Content-Type": "application/json",
          }
        }
      )

      setQuestFinally(res.data.result);
      console.log("Quest finally:", res.data.result);
    } catch (err) {
      console.error("Failed to advance quest:", err);
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
              <p className="text-sm mb-1">TESTING Reward Experience: {quest.reward_experience}</p>
              <p className="text-sm mb-4">TESTING Reward: {quest.reward_item}</p>
  
              {!storyIntro ? (
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
                  <h6 className="text-xl font-semibold mb-2">Some time after accepting...</h6>
                  <h3 className="text-2xl font-bold mb-2">{storyIntro.title}</h3>
                  <p>{storyIntro.description}</p>
                  <p>Decision Point: {storyIntro.decision_point}</p>
                  {!questFinally ? (
                    <div className="">
                      <button
                        className="mt-4 px-4 py-2 bg-blue-400 text-white rounded"
                        onClick={() => advanceQuest(storyIntro.choices[0])}>
                        {storyIntro.choices[0]}
                      </button>
                      <button
                        className="mt-4 px-4 py-2 bg-yellow-400 text-white rounded"
                        onClick={() => advanceQuest(storyIntro.choices[1])}>
                          {storyIntro.choices[1]}
                      </button>
                    </div>
                    ) : (
                      <div className="mt-6 bg-gray-100 p-4 rounded shadow">
                        <h3 className="text-xl font-bold mb-2">Quest Outcome: {questFinally.outcome.toUpperCase()}</h3>
                        <p>{questFinally.summary}</p>
                        <p className="mt-2 text-sm">Health Change: {questFinally.health_change}</p>
                        <p className="text-sm">Gold Change: {questFinally.gold_change}</p>
                        <p className="text-sm">Quest Complete: {questFinally.quest_complete ? "Yes" : "No"}</p>
                      </div>
                    )
                  }
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
