import React, { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { connect } from 'react-redux';
import { verify } from '../../actions/auth';
import './Activate.css'

const Activate = ({ verify, match }) => {
    const navigate = useNavigate();
    const [verified, setVerified] = useState(false);
    const { uid, token} = useParams();
    const verify_account = e => {
        verify(uid, token);
        setVerified(true);
    };

    if (verified) {
        return navigate('/login')
    }

    return (
        <div className='activate'>
            <div>
                <h1 className='activate-title'>Verify your Account:</h1>
                <button
                    onClick={verify_account}
                    type='button'
                >
                    Verify
                </button>
            </div>
        </div>
    );
};

export default connect(null, { verify })(Activate);