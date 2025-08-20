import { Link } from "react-router-dom";

export default function Header() {
    return (
        <header className="home-header bg-amber-400 text-center font-semibold">
            <h1><Link to="/">Return to Town</Link></h1>
        </header>
    )
}