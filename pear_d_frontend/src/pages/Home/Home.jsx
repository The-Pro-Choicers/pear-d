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
      <div className='left-side'>
        <div className="title">
          <h1>Pear'd</h1>
        </div>
        <nav className='navigation'>
        <button onClick={() => navigate('/restaurants')}>restaurants</button>
        <button onClick={() => navigate('/login')}>settings</button>
        <button onClick={logout_user}>logout</button>
      </nav>
      </div>
    </div>
  )
};

const mapStateToProps = state => ({
     isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, { logout })(Home);