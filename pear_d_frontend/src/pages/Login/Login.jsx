import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { GoogleLogin } from 'react-google-login';
import { gapi } from 'gapi-script';
import { connect } from 'react-redux';
import { login } from '../../actions/auth';
import './Login.css'

const clientId = '404551726935-eemo8staqeue42oa2j4hncrsdlqijnlc.apps.googleusercontent.com';

const Login = ({ login, isAuthenticated }) => {
  const navigate = useNavigate(); {/*allows user to navigate to another page with the click of a button*/}
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });

  const { email, password } = formData;

  const onChange = e => setFormData({...formData, [e.target.name]: e.target.value});

 const onSubmit = e => {
  e.preventDefault();
  login(email, password);
 }

 //if user authentication go to home page
  if (isAuthenticated) {
    navigate('/home')
  }

  return (
    <>
    <div className="login"> {/*this will set the structure of the divs inside covering the entire page*/} 
        <div className="left-side"> {/*Covers the left side of page with login info and title*/}
          <div className="title">
            <h1>Pear'd</h1>
          </div>
          <form onSubmit={e => onSubmit(e)} className="login-fields">
            <input
              type='email' 
              placeholder='email'
              name='email'
              value={email}
              onChange={e => onChange(e)}
              required
            />
            <input 
              type="password"
              placeholder="password"
              name='password'
              value={password}
              onChange={e => onChange(e)}
              minLength='6'
              required
            />
            <button onClick={login}>login</button>
            <a onClick={() => navigate('/signup')}>sign up</a>
            {/*<GoogleLogin
              className="custom"
              clientId={clientId}
              buttonText={"Sign in with Google"}
              onSuccess={googleSuccess}
              onFailure={googleFailure}
              cookiePolicy={'single_host_origin'}
              isSignedIn={true}
  />*/}
          </form>
          
          
        </div>
    </div>   
    </>
  )
};

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, { login })(Login);