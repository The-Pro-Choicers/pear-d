import React from 'react'
import pear from '../../assets/images/landing.png';
import Spline from '@splinetool/react-spline';
import { useNavigate } from 'react-router-dom';
import './Landing.css'

const Landing = () => {
  const navigate = useNavigate();
  return (
    <div className="landing">
      <div className="intro">
                <h1>Pear'd</h1>
                <div className="image">
                  <Spline scene="https://prod.spline.design/w8cAx66muvmkx9GV/scene.splinecode" />
                </div>
                <h2>
                    Connecting you with restaurants that care.
                </h2>
                <button onClick={() => navigate('/login')}>Login</button>                     
      </div>
    </div>
  )
}

export default Landing;