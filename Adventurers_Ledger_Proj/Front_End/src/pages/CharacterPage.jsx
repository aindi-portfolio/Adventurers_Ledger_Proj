import React from "react";
import InputField from "../components/InputField";
import { Create_Character } from "../services/authService";

export default function CharacterPage() {

    function handleClick() {
        // Handle character creation logic here
        characterData = {
            name: document.getElementById('characterName').value,
            character_class: document.getElementById('characterClass').value
        }
        const response = Create_Character(characterData);
        if (response.status === 201) {
            alert('Player Created!');
        }
        else {
            alert('Error creating player. Please try again.');
        }
    }
    

    return (
        <div className="create-character-container">
        <h1>Build your character</h1>
        <form className="create-character-form">
            <div className="form-group">
            <label htmlFor="characterName">Player Name:</label>
            <InputField typte="text" id="characterName" name="characterName" required />
            </div>
            <div className="form-group">
            <label htmlFor="characterClass">Character Class:</label>
            <select id="characterClass" name="characterClass" required>
                <option value="">Select Class</option>
                <option value="warrior">Warrior</option>
                <option value="mage">Mage</option>
                <option value="rogue">Rogue</option>
            </select>
            </div>
            <button onClick={handleClick}>Create Player</button>
        </form>
        </div>
    );
    }