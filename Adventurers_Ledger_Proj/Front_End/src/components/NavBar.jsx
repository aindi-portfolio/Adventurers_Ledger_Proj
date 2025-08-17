import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import '../styles/NavBar.css';
import Button from './Button';
import InputField from './InputField';
import { Sign_Up, Log_In, Log_Out } from '../services/authServices';
import { SeedItems, SeedMonsters } from "../services/SeedFunctions";

export default function NavBar() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [showLogin, setShowLogin] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSignUp = async () => {
      try {
        const userData = {
          email: email,
          password: password
        };
        if (!userData.email || !userData.password) {
          alert('Please fill out all fields.');
          return;
        }
        await Sign_Up(userData);
        console.log('Sign Up Successful');
      } catch (error) {
        console.error('Sign Up Error:', error);
      }
    }
  
  const handleLogIn = async () => {
      try {
        const userData = {
          email: email,
          password: password
        };
        if (!userData.email || !userData.password) {
          alert('Please fill out all fields.');
          return;
        }
        console.log("Logging in with:", email, password);
        await Log_In(userData);
        console.log('Log In Successful');
        // Redirect to create player page
        window.location.href = '/create-character';
      } catch (error) {
        console.error('Log In Error:', error);
      }
    }

    useEffect(() => {
      const token = localStorage.getItem('authToken');
      setIsAuthenticated(!!token);
    }, []);

    const challenge_rating = 1; // Example challenge rating, can be adjusted as needed
    return (
        <div className="navbar">
            <ul>
                <li>
                    <Link to="/encounter">Go to Battle</Link>
                </li>
                <li>
                    <Link to="/quest">Quests</Link>
                </li>
                <li>
                    <Link to="/inventory">Inventory</Link>
                </li>
                <li>
                    <Link to="/stats">Stats</Link>
                </li>
                <li>
                    <Link to="/shop">Shop</Link>
                </li>
                
                { !isAuthenticated ? (
                    <div style={{ color: 'black' }}>
                    <form className='' onSubmit={(e) => e.preventDefault()}>
                      <InputField type='email' value={email} placeholder='email' className='text-center' onChange={(e) => setEmail(e.target.value)}/>
                    <br />
                      <InputField type="password" value={password} placeholder='password' className='text-center' onChange={(e) => setPassword(e.target.value)}/>
                    <br />
                    <Button onClick={handleLogIn}>Log In</Button>
                    <br />
                    <Button onClick={handleSignUp}>Sign Up</Button>
                    </form>
                  </div> /* This will render the login/signup form */
                ) : (
                    <li>
                        <Button onClick={() => {
                            Log_Out();
                            setIsAuthenticated(false);
                        }}>Log Out</Button>
                    </li>
                )}
            </ul>
            <div className="">
              <Button onClick={SeedItems}>Seed Equipment</Button>
              <br />
              <Button type="button" onClick={async () => SeedMonsters(challenge_rating)}>Seed Monsters</Button>
            </div>
        </div>
    );
}