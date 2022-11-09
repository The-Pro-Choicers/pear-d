import React, { useState } from 'react';
import { connect } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { signup } from '../../actions/auth';
import './SignUp.css';

const SignUp = ({ signup, isAuthenticated }) => {
  const navigate = useNavigate();
  const [accountCreated, setAccountCreated] = useState(false);
  const [formData, setFormData] = useState({
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        re_password: ''
  });

 const { first_name, last_name, email, password, re_password } = formData;

 const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

 const onSubmit = e => {
     e.preventDefault();

     if (password === re_password) {
        signup(first_name, last_name, email, password, re_password);
        setAccountCreated(true);
     }
 };

 if (isAuthenticated) {
    navigate('/home');
 }

 if (accountCreated) {
   navigate('/login');
 }

  return (
    <div className="signup"> {/*this will set the structure of the divs inside covering the entire page*/} 
        <div className="left-side"> {/*Covers the left side of page with login info and title*/}
          <div className="signup-title">
            <h1>Create Your Account</h1>
          </div>
          <form onSubmit={e => onSubmit(e)} className="signup-fields">
            <input
                type='text' 
                placeholder='first name'
                name='first'
                value={first_name}
                onChange={e => onChange(e)}
                required
            />
            <input
              type='text' 
              placeholder='last name'
              name='last'
              value={last_name}
              onChange={e => onChange(e)}
              required
            />
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
            <input 
              type="password"
              placeholder="confirm password"
              name='password'
              value={re_password}
              onChange={e => onChange(e)}
              minLength='6'
              required
            />
            <button type="submit" onClick={signup}>sign up</button>
            <a onClick={() => navigate('/')}>already have an account?</a>
          </form>
          
          
        </div>
    </div>   
  )
}

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, {signup})(SignUp);