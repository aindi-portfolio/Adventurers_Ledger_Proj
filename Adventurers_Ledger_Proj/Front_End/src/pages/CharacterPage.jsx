import React, { useRef } from 'react';
import Header from '../components/Header';
import InputField from '../components/InputField';

export default function CharacterPage() {
    // Refs for input fields
    const nameRef = useRef(null);
    const classRef = useRef();

    // Function to handle character creation
    async function Create_Character(characterData) {
        try {
            const token = localStorage.getItem('authToken');
            const response = await fetch('http://localhost:8000/api/character/create-character', {
                method: 'POST',
                headers: {
                    Authorization: `Token ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(characterData)
            });
            // Check if the response is ok (status in the range 200-299)
            if (!response.ok) {
                throw new Error(response.statusText);
                console.error(response);
                console.log(response);
            }
            return response;
        } catch (error) {
            console.error('Error creating character:', error);
            throw error;
        }
    }

    async function handleClick(event) {
        event.preventDefault();
    
        const name = nameRef.current?.value?.trim();
        const characterClass = classRef.current?.value;
    
        console.log("Name:", name); // Debug
        console.log("Class:", characterClass); // Debug
    
        if (!name || characterClass === "") {
            alert('Please fill out all fields.');
            return;
        }
    
        const characterData = {
            name,
            character_class: characterClass
        };
    
        try {
            const response = await Create_Character(characterData);
            if (response.status === 201) {
                alert('Player Created!');
                // Redirect to home page or another page after creation
                window.location.href = '/';
            } else {
                alert('Error creating player. Please try again.');
            }
        } catch (error) {
            alert('Error creating player. Please try again.');
        }
    }
    

    return (
        <div className="create-character-container">
            <Header />
            <h1>Build your character</h1>
            <form className="create-character-form" onSubmit={handleClick}>
                <div className="form-group">
                    <label htmlFor="characterName">Character Name:</label>
                    <input
                        ref={nameRef}
                        type="text"
                        id="characterName"
                        name="characterName"
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="characterClass">Character Class:</label>
                    <select ref={classRef} id="characterClass" name="characterClass" required>
                        <option value="" disabled>Select Class</option>
                        <option value="warrior">Warrior</option>
                        <option value="mage">Mage</option>
                        <option value="rogue">Rogue</option>
                    </select>
                </div>
                <button type="submit">CONFIRM</button>
            </form>
        </div>
    );
}
