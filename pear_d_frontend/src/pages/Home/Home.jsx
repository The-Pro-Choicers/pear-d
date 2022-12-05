import React from 'react'
import { Navigate, useNavigate } from 'react-router-dom'
import { logout } from '../../actions/auth'
import { connect } from 'react-redux'
import profile from '../../assets/images/profile.jpg';
import { getAll } from "../../actions/profile"
import './Home.css'

const Home = ({logout, getAll}) => {
  const navigate = useNavigate();

  const logout_user = () => {
    logout();
    navigate('/');
  }

  const getUserInfo = (e) => {
    e.preventDefault()
    getAll();
  }

  return (
    <div className='home'>
      <div className='card'>
      <div className="profilepic">
            <img src={profile}/>
        </div>
        <h1 className="welcome">Welcome User!</h1>
        <h1 className="liked">Your Favorite Restaurants</h1>
        <div className='history'>
          <button onClick ={e => getUserInfo(e)}>user profile</button>
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