import React, { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { connect } from 'react-redux';
import { reset_password_confirm } from '../../actions/auth';


const ResetPasswordConfirm = ({ reset_password_confirm}) => {
  const navigate = useNavigate();
  const [requestSent, setRequestSent] = useState(false);

  const [formData, setFormData] = useState({
    new_password: '',
    new_re_password: '',
  });

  const { new_password, new_re_password } = formData;

  const {uid, token} = useParams();

  const onChange = e => setFormData({...formData, [e.target.name]: e.target.value});

 const onSubmit = e => {
  e.preventDefault();

  reset_password_confirm(uid, token, new_password, new_re_password);
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
              type="password"
              placeholder="new password"
              name='new_password'
              value={new_password}
              onChange={e => onChange(e)}
              minLength='6'
              required
          />
          <input 
              type="password"
              placeholder="confirm new password"
              name='new_re_password'
              value={new_re_password}
              onChange={e => onChange(e)}
              minLength='6'
              required
           />
            <button type="submit">reset password</button>
          </form>

        </div>
    </div>   
    </>
  )
};



export default connect(null, { reset_password_confirm })(ResetPasswordConfirm);