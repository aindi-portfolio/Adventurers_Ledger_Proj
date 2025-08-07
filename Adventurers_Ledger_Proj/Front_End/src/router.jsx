import App from "./App.jsx";
import HomePage from "./pages/HomePage.jsx";
import { createBrowserRouter } from "react-router-dom";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {
                index: true,
                element: <HomePage />,
            },
        ],
    },
]);

export default router;