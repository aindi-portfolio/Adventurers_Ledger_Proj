import { createBrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import HomePage from "./pages/HomePage.jsx";
import LogIn_SignUp from "./pages/LogIn_SignUp.jsx";

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
            }
        ]
    }
]);

export default router;