import React from 'react'
import { Navigate, useNavigate } from 'react-router-dom'
import { logout } from '../../actions/auth'
import { connect } from 'react-redux'
import './Home.css'

const Home = ({logout}) => {
  const navigate = useNavigate();

  const logout_user = () => {
    logout();
    navigate('/');
  }
  return (
    <div className='home'>
      <h1 className='home-title'>Home Page</h1>
      <button onClick={logout_user}>logout</button>
    </div>
  )
};

const mapStateToProps = state => ({
     isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, { logout })(Home);