import { createBrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import HomePage from "./pages/HomePage.jsx";
import Inventory from "./pages/InventoryPage.jsx";
import CharacterPage from "./pages/CharacterPage.jsx";
import StatsPage from "./pages/StatsPage.jsx";
import ShopPage from "./pages/ShopPage.jsx";


const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {
                index: true,
                element: <HomePage />
            },
            {
                path: "/inventory",
                element: <Inventory />
            },
            {
                path: "/create-character",
                element: <CharacterPage />
            },
            {
                path: "/stats",
                element: <StatsPage />
            },
            {
                path: "/shop",
                element: <ShopPage />
            }
        ]
    }
]);

export default router;