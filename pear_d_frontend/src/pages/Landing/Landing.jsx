import React from 'react'
import pear from '../../assets/images/landing.png';
import { useNavigate } from 'react-router-dom';
import './Landing.css'

const Landing = () => {
  const navigate = useNavigate();
  return (
    <div className="landing">
        <div className="intro">
                <h1>Pear'd</h1>
                <p>
                    This is where I will put a nice paragraph about Pear'd
                </p>
                <button onClick={() => navigate('/login')}>Login</button>            
        </div>
        <div className="image">
            <img src={pear}/>
            <button onClick={() => navigate('/login')}>Login</button>
        </div>
    </div>
  )
}

export default Landing;