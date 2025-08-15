import React, {useState, useEffect} from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

export default function EncounterPage() {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [fighting, setFighting] = useState(false);
    const [enemy, setEnemy] = useState(null);
    const [character, setCharacter] = useState(null);


    useEffect(() => {
        const token = localStorage.getItem('authToken');
        setIsAuthenticated(!!token);
        // Fetch character and enemy data here if needed
        // Example: fetchCharacterData() and fetchEnemyData()
    }, []);

    return (
        <>
        <Header />
        <div className="encounter-page flex flex-col items-center">
            {!isAuthenticated && (
                <div className="alert alert-warning">
                    <p>Please log in to access the encounter page.</p>
                </div>
            ) : (
                <h1>Encounter Page</h1>
                <p>Welcome to the Encounter Page! Here you can manage your encounters.</p>

                {/* Additional content for the encounter page can be added here */}
                <div className='Battle_Container flex gap-5 text-center m-5'> 
                    <div className='Character_Container border-4 border-green-600 w-40'>
                        <h1 className='text-2xl'>Character Name</h1>
                        <img src='https://via.placeholder.com/150' alt='Character Image' className='w-40 h-40' />
                    </div>
                    <div className='Enemy_Container border-4 border-red-600 w-40'>
                        <h1 className='text-2xl'>Enemy Name</h1>
                        <img src='https://via.placeholder.com/150' alt='Enemy Image' className='w-40 h-40' />
                    </div>
                </div>
            )}
            
        </div>
        <Footer />
        </>
    )
}