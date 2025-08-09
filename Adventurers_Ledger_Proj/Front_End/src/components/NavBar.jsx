import { useState } from 'react';
import { Link } from 'react-router-dom';
import '../styles/NavBar.css'; 


export default function NavBar() {
    return (
        <div className="navbar">
            <ul>
                <li>
                    <Link to="/explore">Explore</Link>
                </li>
                <li>
                    <Link to="/quests">Quests</Link>
                </li>
                <li>
                    <Link to="/inventory">Inventory</Link>
                </li>
                <li>
                    <Link to="/stats">Stats</Link>
                </li>
                <li>
                    <Link to="/login_signup">Login</Link>
                </li>
            </ul>
        </div>
    );
}