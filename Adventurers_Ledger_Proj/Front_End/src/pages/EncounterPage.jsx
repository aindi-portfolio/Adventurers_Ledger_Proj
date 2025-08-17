import React, {useState, useEffect} from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import {EncounterButton} from '../components/Button';
import fetchCharacterStats from '../services/FetchStats';

export default function EncounterPage() {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [isFighting, setIsFighting] = useState(false);
    const [enemy, setEnemy] = useState(null);
    const [character, setCharacter] = useState(null);


    useEffect(async () => {
        const token = localStorage.getItem('authToken');
        setIsAuthenticated(!!token);
        // Fetch character and enemy data here if needed
        const stats_data = await fetchCharacterStats();
        setCharacter(stats_data);
        console.log("Character data:", stats_data);
        // Example: fetchCharacterData() and fetchEnemyData()
    }, []);

    return (
        <>
            <Header />
            <div className="encounter-page flex flex-col items-center">
                {!isAuthenticated ? (
                <div className="alert alert-warning">
                    <p>Please log in to access the encounter page.</p>
                </div>
                ) : !isFighting ? (
                <>
                    <h1>Encounter Page</h1>
                    <p>Welcome to the Encounter Page! Here you can manage your encounters.</p>
                    <EncounterButton onClick={() => setIsFighting(true)} children="Hunt" className='bg-gradient-to-r from-green-700 to-green-500 text-white font-semibold rounded-lg shadow-md hover:from-green-600 hover:to-green-400 hover:scale-105 transition-transform duration-200 border-2 border-green-800'/>
                </>
                ) : (
                <div className="Battle-Container text-center m-5">

                    <div className='stats-container flex gap-5 mb-4'>
                        <div className="Character-Container border-4 border-green-600 w-40">
                        <h1 className="text-2xl">{character.name}</h1>
                        <img src="" alt="Character Image" className="w-40 h-40" />
                        <p>Level: {character.level}</p>
                        <p>HP: {character.health}</p>
                        </div>
                        <img src="https://via.placeholder.com/150" alt="Battle Scene" className="w-40 h-40 self-center border-2" />
                        <div className="Enemy-Container border-4 border-red-600 w-40">
                        <h1 className="text-2xl">Enemy Name</h1>
                        <img src="" alt="Enemy Image" className="w-40 h-40" />
                        </div>
                    </div>
                    
                    <div className='battle-actions space-x-5'>
                        <EncounterButton onClick={() => alert('Attack!')} children="Attack" className='bg-gradient-to-r from-green-700 to-green-500 text-white font-semibold rounded-lg shadow-md hover:from-green-600 hover:to-green-400 hover:scale-105 transition-transform duration-200 border-2 border-green-800'/>
                        <EncounterButton onClick={() => alert('Defend!')} children="Defend" className='bg-gradient-to-r from-blue-700 to-blue-500 text-white font-semibold rounded-lg shadow-md hover:from-blue-600 hover:to-blue-400 hover:scale-105 transition-transform duration-200 border-2 border-blue-800'/>
                        <EncounterButton onClick={() => alert('Run!')} children="Escape" className='bg-gradient-to-r from-red-700 to-red-500 text-white font-semibold rounded-lg shadow-md hover:from-red-600 hover:to-red-400 hover:scale-105 transition-transform duration-200 border-2 border-red-800'/>
                    </div>
                </div>
                )}
            </div>
            <Footer />
        </>

    )
}