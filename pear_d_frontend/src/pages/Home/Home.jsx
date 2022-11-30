import React from 'react'
import { useNavigate } from 'react-router-dom'
import { logout } from '../../actions/auth'
import { connect } from 'react-redux'
import profile from '../../assets/images/profile.jpg';
import './Home.css'

const Home = ({logout}) => {
  const navigate = useNavigate();

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
        <h1 className="welcome">Welcome User!</h1>
        <h1 className="liked">Your Favorite Restaurants</h1>
        <div className='history'>

        </div>


        <nav className='navigation'>
        <button onClick={() => navigate('/login')}>restaurants</button>
        <button onClick={() => navigate('/rest')}>find restaurants</button>
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