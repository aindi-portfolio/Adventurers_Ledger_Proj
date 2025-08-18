import { useContext } from "react";
import { useOutletContext } from "react-router-dom";
import { ItemsContext } from "../pages/InventoryPage";

const Attack = () => {
  const { items } = useContext(ItemsContext);
    const { enemy, setEnemy, character } = useOutletContext().myContextObject;
  

  if (!enemy || !character || !items) {
    console.error("Invalid parameters provided to Attack function.");
    return;
  }

  let character_attack_damage = character.damage ?? 2 * character.level;
  let item_damage = 0;

  for (let i = 0; i < items.length; i++) {
    if (items[i].item_type === "weapon") {
      item_damage += items[i].damage;
    }
  }

  const total_damage = character_attack_damage + item_damage;
  const new_enemy_health = Math.max(0, enemy.health - total_damage);

  console.log("Enemy health before:", enemy.health);
  console.log("Total attack damage:", total_damage);
  console.log("Enemy health after:", new_enemy_health);

  setEnemy({ ...enemy, health: new_enemy_health });
};

export { Attack };
