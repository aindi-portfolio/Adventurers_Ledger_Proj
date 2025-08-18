import React, { useState } from 'react';


const locations = [
  "Ancient Crypt", "Floating Island", "Volcanic Wasteland", "Haunted Forest"
];
const enemies = [
  "Skeletons", "Wraiths", "Fire Elementals", "Bandits"
];
const lighting = [
  "Moonlit", "Torch-lit", "Stormy", "Glowing Runes"
];
const actions = [
  "Combat erupts", "Ritual begins", "Ambush unfolds", "Portal opens"
];

function getRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function generateSceneMarkdown() {
  return {
    title: getRandom(locations),
    foreground: "Adventurers preparing for battle",
    midground: `${getRandom(enemies)} emerging from terrain`,
    background: `${getRandom(lighting)} atmosphere`,
    action: getRandom(actions),
    mood: "Tense and cinematic"
  };
}

export default function SceneGenerator({ questData }) {
  const [scene, setScene] = useState(generateSceneMarkdown());

  const regenerate = () => {
    setScene(generateSceneMarkdown());
  };

  return (
    <div className="scene-card">
      <h2>🗺️ Scene: {scene.title}</h2>
      <ul>
        <li><strong>Foreground:</strong> {scene.foreground}</li>
        <li><strong>Midground:</strong> {scene.midground}</li>
        <li><strong>Background:</strong> {scene.background}</li>
        <li><strong>Action:</strong> {scene.action}</li>
        <li><strong>Mood:</strong> {scene.mood}</li>
      </ul>
      <button onClick={regenerate}>🎲 Generate New Scene</button>
    </div>
  );
}
