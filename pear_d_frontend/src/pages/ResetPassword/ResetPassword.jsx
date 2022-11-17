import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { connect } from 'react-redux';
import { password_reset } from '../../actions/auth';

const ResetPassword = ({ password_reset }) => {
  const navigate = useNavigate();
  const [requestSent, setRequestSent] = useState(false);

  const [formData, setFormData] = useState({
    email: '',
  });

  const { email } = formData;

  const onChange = e => setFormData({...formData, [e.target.name]: e.target.value});

 const onSubmit = e => {
  e.preventDefault();
  password_reset(email);
  setRequestSent(true);
 }

 //if user authentication go to home page
  if (requestSent) {
    navigate('/login')
  }

  return (
    <>
    <div className="login"> {/*this will set the structure of the divs inside covering the entire page*/} 
        <div className="left-side"> {/*Covers the left side of page with login info and title*/}
          <div className="title">
            <h1>Request Password Reset</h1>
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
            <button type="submit">reset password</button>
          </form>

        </div>
    </div>   
    </>
  )
};



export default connect(null, { password_reset })(ResetPassword);