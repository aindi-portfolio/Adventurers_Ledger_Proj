import { createBrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import HomePage from "./pages/HomePage.jsx";
import LogIn_SignUp from "./pages/LogIn_SignUp.jsx";
import Inventory from "./pages/Inventory.jsx";
import CharacterPage from "./pages/CharacterPage.jsx";

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
                path: "/login_signup",
                element: <LogIn_SignUp />
            },
            {
                path: "/inventory",
                element: <Inventory />
            },
            {
                path: "/create-character",
                element: <CharacterPage />
            }
        ]
    }
]);

export default router;