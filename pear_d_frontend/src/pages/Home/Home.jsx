import React from 'react'
import { useNavigate } from 'react-router-dom'
import { logout } from '../../actions/auth'
import { connect } from 'react-redux'
import profile from '../../assets/images/profile.jpg';
import { getAll } from "../../actions/profile"
import './Home.css'
import { useState, useEffect } from 'react';

const Home = ({logout, getAll}) => {
  const navigate = useNavigate();
  const [userInfo, setUserInfo] = useState("");
  useEffect(() => {
    getAll().then(function(result){setUserInfo(result)
  }
  )})

  const logout_user = () => {
    logout();
    navigate('/');
  }

  return (
    <>
      <div className='page'>
      <h2>Welcome to Pear'd!</h2>
      <div className="container">
        <div className="user-fav">
        <h3>Favorite Restaurants</h3>
        <div className="restaurant-scroll">
          {userInfo.favorites?.map((fav) => (
              <div className="restaurants">
                <h3>{fav.restaurant.name}</h3>
                <h6>{fav.restaurant.address}</h6>
                <a href={fav.restaurant.url}>directions</a>
              </div>
          ))}
        </div>
        <button onClick={() => navigate('/rest')}>Find a Restaurant!</button>
        </div>
        <div className="container-two">
          <div className="user-info">
          <div className="info">
            <h4>{userInfo.name}</h4>
            <h4>{userInfo.email}</h4>
            <h4>Favorite Cuisine: </h4>
          </div>
          <img src={profile}/>
          </div>
          <div className="user-preferences">
              <h3>Preferences</h3>
              <div className="preferences">
                <div className="pref-type">
                {userInfo.prefer_env_conscious}
                <br/>
                <br/>
                {userInfo.prefer_minority}
                <br/>
                <br/>
                {userInfo.prefer_philanthropic}
                </div>
                <div className="pref-price">
                  <h4>Preferred Price: </h4>
                  <h5>{userInfo.prefer_price}</h5>
                </div>
              </div>
          </div>
        </div>
      </div>
      <button className="logout" onClick={logout_user}>logout</button>
      </div>
    </>
  )
};

const mapStateToProps = state => ({
     isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, { logout, getAll })(Home);