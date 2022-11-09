import React, { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { connect } from 'react-redux';
import { verify } from '../../actions/auth';

const Activate = ({ verify, match }) => {
    const navigate = useNavigate();
    const [verified, setVerified] = useState(false);
    const { uid, token} = useParams();
    const verify_account = e => {
        verify(uid, token);
        setVerified(true);
    };

    if (verified) {
        return navigate('/')
    }

    return (
        <div className='container'>
            <div>
                <h1>Verify your Account:</h1>
                <button
                    onClick={verify_account}
                    style={{ marginTop: '50px' }}
                    type='button'
                >
                    Verify
                </button>
            </div>
        </div>
    );
};

export default connect(null, { verify })(Activate);