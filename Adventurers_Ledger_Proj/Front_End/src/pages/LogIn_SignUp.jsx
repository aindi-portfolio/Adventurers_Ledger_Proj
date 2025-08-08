import React from 'react';
import { Sign_Up, Log_In, Log_Out } from '../services/authService';

const handleSignUp = async () => {
  try {
    const userData = {
      email: document.querySelector('input[name="email"]').value,
      password: document.querySelector('input[name="password"]').value
    };
    await Sign_Up(userData);
    console.log('Sign Up Successful');
  } catch (error) {
    console.error('Sign Up Error:', error);
  }
}
function user_authentication() {
    return (
      <>
        <NavBar />
        <div>
            <form>
            <label>
                Email:
                <input type="text" name="email" />
            </label>
            <br />
            <label>
                Password:
                <input type="password" name="password" />
            </label>
            <br />
            <button type="submit">Log In</button>
            <br />
            <button type="submit">Sign Up</button>
            </form>
        </div>
      </>
      
    )
  }

export default user_authentication;