import { useContext } from 'react';
import { GlobalStateContext } from '../context/GlobalStateContext';

const useAttack = () => {
    const { character, setCharacter, enemy, setEnemy, items } = useContext(GlobalStateContext);

    const attack = () => {

        let character_attack_damage = character.damage ? character.damage : 5; // can be modified to pull from character stats
        // console.log("Character attack damage:", character_attack_damage);

        // console.log("Items in inventory:", items);

        let item_damage = 0; // Initialize item damage
        for (let i = 0; i < items.length; i++) {
            let counter = 0; // Reset counter for each item
            while (counter <= items[i].quantity) { // Loop through the quantity of each item
                if (items[i].item.item_category === "Weapon") { // Check if the item is a weapon
                    item_damage += items[i].item.damage; // Add the item's damage to item_damage
                }
                counter++; // Increment the counter
            }
        }
        // console.log("Item damage:", item_damage);

        character_attack_damage += item_damage; // Add item damage to character attack damage
        // console.log("Total character attack damage:", character_attack_damage);

        // ATTACK ENEMY AND UPDATE ENEMY HEALTH
        enemy.health -= character_attack_damage;

        // ENEMY ATTACKS BACK
        character.health -= enemy.damage;

        // Check if either character or enemy is dead
        if (enemy.health <= 0) {
            console.log("Enemy defeated!");
            enemy.health = 0; // Ensure health doesn't go negative
        } else if (character.health <= 0) {
            console.log("Character defeated!");
            character.health = 0; // Ensure health doesn't go negative
        }

        if (enemy.health <= 0 && character.health > 0) {
            alert("You win!");
            window.location.href = '/encounter'; // Redirect to home page after victory
            return { enemyHealth: enemy.health, characterHealth: character.health };
        }
        if (character.health <= 0) {
            alert("You lose!");
            window.location.href = '/'; // Redirect to home page after defeat
            return { enemyHealth: enemy.health, characterHealth: character.health };
        }

        // Update state if necessary
        setEnemy({ ...enemy, health: enemy.health });
        setCharacter({ ...character, health: character.health });


        
    };

    return attack;
};

export { useAttack };