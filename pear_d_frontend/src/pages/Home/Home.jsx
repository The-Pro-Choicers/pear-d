import React from 'react'
import { Navigate, useNavigate } from 'react-router-dom'
import { logout } from '../../actions/auth'
import { connect } from 'react-redux'
import profile from '../../assets/images/profile.jpg';
import { getAll } from "../../actions/profile"
import './Home.css'
import { useState, useEffect } from 'react';

const Home = ({logout, getAll}) => {
  const navigate = useNavigate();
  const [userInfo, setUserInfo] = useState("");
  useEffect(()=>{
    getAll() .then(function(result){setUserInfo(result)
  })})
  

  const logout_user = () => {
    logout();
    navigate('/');
  }

  return (
    <div className='home'>
      <div className='card'>
      <div className="profilepic">
            <img src={profile}/>
        </div>
        <h1 className='welcome'>Welcome {userInfo.name}!</h1>
        <div className='favorites'>
          <h2>you believe in</h2>
          <p>{userInfo.prefer_env_conscious}</p>
          <p>{userInfo.prefer_minority}</p>
          <p>{userInfo.prefer_philanthropic}</p>
        </div>
        <nav className='navigation'>
        <button onClick={() => navigate('/restaurants')}>restaurants</button>           
        <button onClick={logout_user}>logout</button>
      </nav>
      </div>
    </div>
  )
};

const mapStateToProps = state => ({
     isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, { logout, getAll })(Home);