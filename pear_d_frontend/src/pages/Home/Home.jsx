import React from 'react'
import { useNavigate } from 'react-router-dom'
import { logout } from '../../actions/auth'
import { connect } from 'react-redux'
import profile from '../../assets/images/profile.jpg';
import { getAll, getFavorite } from "../../actions/profile"
import './Home.css'
import { useState, useEffect } from 'react';

const Home = ({logout, getAll, getFavorite}) => {
  const navigate = useNavigate();
  const [userInfo, setUserInfo] = useState("");

  useEffect(()=>{
    getAll().then(function(result){setUserInfo(result)
  })})

  const logout_user = () => {
    logout();
    navigate('/');
  }

  return (
    <>
      <div className="container">
        <div className="user-fav">
        <h3>Favorite Restaurants</h3>
        </div>
        <div className="container-two">
          <div className="user-info">
          <img src={profile}/>
            <h4>Welcome to Pear'd</h4>
            <h4>{userInfo.name} !</h4>
          </div>
          <div className="user-preferences">
              <h4>Preferences</h4>
              <div className="preference">
                <div className="pref-type">
                {userInfo.prefer_env_conscious}
                <br/>
                <br/>
                {userInfo.prefer_minority}
                <br/>
                <br/>
                {userInfo.philanthropic}
                </div>
                <div className="pref-price">
                  <h5>Price: {userInfo.prefer_price}</h5>
                </div>
              </div>
          </div>
        </div>
      </div>
      <button>Find a Restaurant!</button>
    </>
  
  )
};

const mapStateToProps = state => ({
     isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, { logout, getAll, getFavorite })(Home);