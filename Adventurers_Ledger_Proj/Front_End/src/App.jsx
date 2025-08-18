import { useState } from 'react'
import './App.css'
import { Outlet } from 'react-router-dom'
import { GameProvider } from './context/GameContext'

function App() {
  const [enemy, setEnemy] = useState(null);
  const [character, setCharacter] = useState(null);
  const [items, setItems] = useState([]);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isFighting, setIsFighting] = useState(false);
  const myContextObject = {
    enemy,
    setEnemy,
    character,
    setCharacter,
    items,
    setItems,
    isAuthenticated,
    setIsAuthenticated,
    isFighting,
    setIsFighting
  };

  return (
    <>
      <Outlet context={{myContextObject}}/>
    </>
  )
}

export default App;
