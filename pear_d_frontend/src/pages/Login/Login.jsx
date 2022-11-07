import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import './Login.css'

const Login = () => {
  const navigate = useNavigate(); {/*allows user to navigate to another page with the click of a button*/}
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

 const login = () => {
      console.log(username);
      console.log(password);

      navigate('/home');
 }

  return (
    <>
    <div className="login"> {/*this will set the structure of the divs inside covering the entire page*/} 
      <div className="overlay"> {/* Will be the div overlaying the patchy gradient div created */}
        <div className="left-side"> {/*Covers the left side of page with login info and title*/}
          <div className="title">
            Pear'd
          </div>
          <div className="login-fields">
            <input 
              type="text" 
              placeholder="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <input 
              type="password"
              placeholder="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button onClick={login}>login</button>
            <a>sign up</a>
          </div>
        </div>
        <div className="right-side"> {/*Covers the right side where the main login image will be embedded with Spline*/}
          
        </div>
      </div>
      <div className="gradients"> {/* The div where I create a patchy background design*/}
      {/*  <div className="patches"></div>*/}
      </div>
    </div>   
    </>
  )
}

export default Login;