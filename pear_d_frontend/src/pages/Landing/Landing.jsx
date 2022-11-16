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
                <h2>
                    Connecting you with restaurants that care.
                </h2>
                <button onClick={() => navigate('/login')}>Login</button>           
        </div>
        <div className="image">
            <img src={pear}/>
        </div>
    </div>
  )
}

export default Landing;