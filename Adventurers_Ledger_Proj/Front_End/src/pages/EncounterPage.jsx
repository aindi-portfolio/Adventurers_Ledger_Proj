import React, { useState, useEffect, useContext } from 'react';
import { GlobalStateContext } from '../context/GlobalStateContext';
import Header from '../components/Header';
import Footer from '../components/Footer';
import { EncounterButton } from '../components/Button';
import { SeedMonsters } from '../services/SeedFunctions';
import fetchCharacterStats from '../services/FetchStats';
import fetchMonster from '../services/FetchMonster';
import { useAttack } from '../services/EncounterActions';
import fetchInventory from '../services/FetchInventory';
import '../styles/EncounterPage.css'; // Assuming you have a CSS file for styles


export default function EncounterPage() {
    const { isAuthenticated, setIsAuthenticated, isFighting, setIsFighting, enemy, setEnemy, character, setCharacter, items, setItems } = useContext(GlobalStateContext);

    const handleMonsterFetch = async () => {
        try {
            const monster_data = await fetchMonster(character.level);
            setEnemy(monster_data);
            console.log("Enemy data:", monster_data);
        } catch (error) {
            console.error("Failed to fetch monster:", error);
        }
    }

    const seed_monsters = async (character_level) => {
        if (character_level) {
            SeedMonsters(character_level)
                // .then(() => console.log("Monsters seeded successfully."))
                .catch(err => console.error("Error seeding monsters:", err));
        }
    }

    useEffect(() => {
        const fetchData = async () => {
            const token = localStorage.getItem('authToken');
            setIsAuthenticated(!!token);
            // Fetch character and enemy data here if needed
            const stats_data = await fetchCharacterStats();
            setCharacter(stats_data);
            console.log("Character data:", stats_data);
            const fetched_inventory = await fetchInventory();
            setItems(fetched_inventory);
            seed_monsters(stats_data.level);
        };
        fetchData();
    }, []);

    

    // the isDisabled to prevent fetch failure on rapid clicks
    const [isDisabled, setIsDisabled] = useState(false);

    const handleAction = (action) => {
        if (!isDisabled) {
            setIsDisabled(true);
            alert(action);
            setTimeout(() => {
                setIsDisabled(false);
            }, 1000);
        }
    };

    const attack = useAttack();

    const handleAttack = () => {
        const attackResult = attack();
        console.log("Attack result:", attackResult);
        console.log("Enemy health after attack:", attackResult.enemyHealth);
        console.log("Character health after attack:", attackResult.characterHealth);
    }

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
                    <EncounterButton 
                    onClick={() => { handleAction('You are hunting!'); setIsFighting(true); setEnemy(handleMonsterFetch()); }} 
                    children="Hunt" 
                    className='bg-gradient-to-r from-green-700 to-green-500 text-white font-semibold rounded-lg shadow-md hover:from-green-600 hover:to-green-400 hover:scale-105 transition-transform duration-200 border-2 border-green-800'/>
                </>
                ) : (
                <div className="Battle-Container text-center m-5">

                    <div className='stats-container flex gap-5 mb-4'>
                        <div className="Character-Container border-4 border-green-600 w-40">
                        <h1 className="text-2xl">{character.name}</h1>
                        <img alt="Character Image" className="w-40 h-40" />
                        <p>Level: {character.level}</p>
                        <p>HP: {character.health}</p>
                        </div>
                        <img alt="Battle Scene" className="w-40 h-40 self-center border-2" /> {/* Placeholder for battle scene image */ }
                        <div className="Enemy-Container border-4 border-red-600 w-40">
                        <h1 className="text-2xl">{enemy.name}</h1>
                        <img src={enemy.image_url}  alt="Enemy Image" className="w-40 h-40" />
                        <p>Type: {enemy.type}</p>
                        <p>HP: {enemy.health}</p>
                        </div>
                    </div>
                    
                    <div className='battle-actions space-x-5'>
                        <EncounterButton 
                        onClick={handleAttack} 
                        children="Attack" 
                        className='bg-gradient-to-r from-green-700 to-green-500 text-white font-semibold rounded-lg shadow-md hover:from-green-600 hover:to-green-400 hover:scale-105 transition-transform duration-200 border-2 border-green-800'/>

                        <EncounterButton 
                        onClick={() => alert('Defend!')} 
                        children="Defend" 
                        className='bg-gradient-to-r from-blue-700 to-blue-500 text-white font-semibold rounded-lg shadow-md hover:from-blue-600 hover:to-blue-400 hover:scale-105 transition-transform duration-200 border-2 border-blue-800'/>

                        <EncounterButton 
                        onClick={() => alert('Run!')} 
                        children="Escape" 
                        className='bg-gradient-to-r from-red-700 to-red-500 text-white font-semibold rounded-lg shadow-md hover:from-red-600 hover:to-red-400 hover:scale-105 transition-transform duration-200 border-2 border-red-800'/>
                    </div>
                </div>
                )}
            </div>
            <Footer />
        </>

    )
}
