import React, { useContext } from 'react';
import { ItemsContext } from '../pages/InventoryPage';

const Attack = ({ enemy, character }) => {
    const { items, setItems } = useContext(ItemsContext);

    let character_attack_damage = character.damage ? character.damage : 5; // can be modified to pull from character stats
    console.log("Character attack damage:", character_attack_damage);
    let item_damage = 0; // Initialize item damage
    for (let i = 0; i < items.length; i++) {
        if (items[i].item.item_type === "weapon") {
            item_damage += items[i].item.damage;
        }
    }
    console.log("Item damage:", item_damage);
    character_attack_damage += item_damage; // Add item damage to character attack damage
    console.log("Total character attack damage:", character_attack_damage);
    // Check if the enemy is already defeated
    
    enemy.health -= character_attack_damage;
    return (enemy.health, character.health);
}

export { Attack };