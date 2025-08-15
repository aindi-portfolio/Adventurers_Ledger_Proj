import React, { useState, useEffect } from "react";
import axios from "axios";
import Header from "../components/Header";
import Footer from "../components/Footer";

const ExplorePage = () => {
  const [quest, setQuest] = useState(null);
  const [storyIntro, setStoryIntro] = useState("");
  const [history, setHistory] = useState([]);
  const [choices, setChoices] = useState(["Yes", "No"]);
  const [loading, setLoading] = useState(false);
  const [isComplete, setIsComplete] = useState(false);
  const [outcome, setOutcome] = useState(null);

  const API_BASE = 'http://localhost:8000/api';

  // Fetch initial quest + story intro
  useEffect(() => {
    const fetchQuest = async () => {
      try {
        const res = await axios.get(`${API_BASE}/quests/explore-quest`);
        setQuest(res.data.quest);
        setStoryIntro(res.data.story_intro);
        console.log("Fetched story intro:", storyIntro);
      } catch (err) {
        console.error("Failed to fetch quest:", err);
      }
    };

    fetchQuest();
  }, []);

  // Handle player choice
  const handleChoice = async (choice) => {
    if (!quest) return;

    setLoading(true);

    try {
        const res = await axios.post(`${API_BASE}/quests/advance-quest`, {
        quest_title: quest.title,
        quest_description: quest.description,
        history,
        choice,
      });

      const { response, choices: newChoices, is_complete, outcome } = res.data;

      setHistory((prev) => [...prev, { choice, response }]);
      setChoices(newChoices);
      setIsComplete(is_complete);
      setOutcome(outcome);
    } catch (err) {
      console.error("Failed to advance quest:", err);
    } finally {
      setLoading(false);
    }
  };

  // Restart quest
  const restartQuest = () => {
    setHistory([]);
    setChoices(["Yes", "No"]);
    setIsComplete(false);
    setOutcome(null);
    setStoryIntro("");
    setQuest(null);
    // Re-fetch a new quest
    axios.get(`${API_BASE}/quests/explore-quest`).then((res) => {
      setQuest(res.data.quest);
      setStoryIntro(res.data.story_intro);
    });
  };

  return (
    <>
        <Header />
        <div className="explore-page">
        {quest ? (
            <>
            <h2>{quest.title}</h2>
            <p>{quest.description}</p>

            {history.length === 0 && <p><strong>Intro:</strong> {storyIntro}</p>}

            <div className="story-log">
                {history.map((entry, idx) => (
                <div key={idx} className="story-entry">
                    <p><strong>Choice:</strong> {entry.choice}</p>
                    <p><strong>Result:</strong> {entry.response}</p>
                </div>
                ))}
            </div>

            {loading ? (
                <p>Loading next part of the story...</p>
            ) : isComplete ? (
                <div className="story-outcome">
                <h3>Quest {outcome === "success" ? "Completed!" : "Failed!"}</h3>
                <button onClick={restartQuest}>Start New Quest</button>
                </div>
            ) : (
                <div className="choice-buttons">
                {choices.map((choice, idx) => (
                    <button key={idx} onClick={() => handleChoice(choice)}>
                    {choice}
                    </button>
                ))}
                </div>
            )}
            </>
        ) : (
            <p>Loading quest...</p>
        )}
        </div>
        <Footer />
    </>
  );
};

export default ExplorePage;
