// context/GameContext.js
import { ItemsProvider } from '../pages/InventoryPage'; // Ensure ItemsProvider is exported correctly
import { EncounterProvider } from '../pages/EncounterPage'; // Ensure EncounterProvider is exported correctly

export const GameProvider = ({ children }) => (
  <EncounterProvider>
    <ItemsProvider>
      {children}
    </ItemsProvider>
  </EncounterProvider>
);
