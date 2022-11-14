import React from 'react'
import pear from '../../assets/images/landing.png'
import './Landing.css'

const Landing = () => {
  return (
    <div className="landing">
        <div className="intro">
                <h1>Pear'd</h1>
                <p>
                    This is where I will put a nice paragraph about Pear'd
                </p>
                <button>Login</button>            
        </div>
        <div className="image">
            <img src={pear}/>
            <button>Login</button>
        </div>
    </div>
  )
}

export default Landing;