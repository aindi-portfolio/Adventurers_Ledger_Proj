import React, { createContext, useState } from 'react';

// Create the context
export const GlobalStateContext = createContext();

// Create the provider component
export const GlobalStateProvider = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [isFighting, setIsFighting] = useState(false);
    const [enemy, setEnemy] = useState(null);
    const [character, setCharacter] = useState(null);
    const [items, setItems] = useState([]);

    return (
        <GlobalStateContext.Provider value={{ isAuthenticated, setIsAuthenticated, isFighting, setIsFighting, enemy, setEnemy, character, setCharacter, items, setItems }}>
            {children}
        </GlobalStateContext.Provider>
    );
};