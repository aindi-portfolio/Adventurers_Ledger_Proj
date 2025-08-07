import { useState } from 'react';
import { Link } from 'react-router-dom';
import '../styles/NavBar.css'; 

export default function NavBar() {
    return (
        <nav className="navbar">
            <ul>
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/characters">Characters</Link>
                </li>
                <li>
                    <Link to="/campaigns">Campaigns</Link>
                </li>
                <li>
                    <Link to="/settings">Settings</Link>
                </li>
                <li>
                    Login
                </li>
            </ul>
        </nav>
    );
}