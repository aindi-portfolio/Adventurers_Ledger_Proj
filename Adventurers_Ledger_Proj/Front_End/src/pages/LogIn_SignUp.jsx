import React, { useState } from 'react';
import { Sign_Up, Log_In, Log_Out } from '../services/authService';
import Header from '../components/Header';
import Button, { MysticButton, EncounterButton } from '../components/Button';
import InputField from '../components/InputField';

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

const handleLogIn = async () => {
  try {
    const userData = {
      email: document.querySelector('input[name="email"]').value,
      password: document.querySelector('input[name="password"]').value
    };
    await Log_In(userData);
    console.log('Log In Successful');
  } catch (error) {
    console.error('Log In Error:', error);
  }
}

function user_authentication() {

    return (
      <>
        <Header />
        <div>
            <form className='text-center'>
                <InputField type='email' name='email' placeholder='email' className='text-center'/>
            <br />
                <InputField type="password" name="password" placeholder='password' className='text-center'/>
            <br />
            <Button onClick={handleLogIn}>Log In</Button>
            <br />
            <Button onClick={handleSignUp}>Sign Up</Button>
            
            </form>
        </div>
      </>
      
    )
  }

export default user_authentication;