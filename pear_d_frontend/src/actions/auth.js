import axios from 'axios';
import {
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    USER_LOADED_SUCCESS,
    USER_LOADED_FAIL,
    AUTHENTICATED_SUCCESS,
    AUTHENTICATED_FAIL,
    SIGNUP_SUCCESS,
    SIGNUP_FAIL,
    ACTIVATION_SUCCESS,
    ACTIVATION_FAIL,
    RESET_FAIL,
    RESET_SUCCESS,
    RESET_CONFIRM_FAIL,
    RESET_CONFIRM_SUCCESS,
    LOGOUT
} from './types';

export const checkAuthenticated = () => async dispatch => {
    console.log("in check auth")
        if (localStorage.getItem('access')) {
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }
            };

            const body = JSON.stringify({ token: localStorage.getItem('access') });

            try {
                const res = await axios.post('http://127.0.0.1:8000/auth/jwt/verify/', body, config);

                if (res.data.code !== 'token_not_valid') {
                    dispatch({
                        type: AUTHENTICATED_SUCCESS
                    });
                } else {
                    dispatch({
                        type: AUTHENTICATED_FAIL
                    });
                }
            } catch {
                dispatch({
                    type: AUTHENTICATED_FAIL
                });
            }

        } else {
            dispatch({
                type: AUTHENTICATED_FAIL
            });
        }
};

export const signup = (first_name, last_name, email, password, re_password) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const name = first_name +  " " + last_name;

    const body = JSON.stringify({ name, email, password, re_password });

    try {
        const res = await axios.post('http://127.0.0.1:8000/auth/users/', body, config);

        dispatch({
            type: SIGNUP_SUCCESS,
            payload: res.data
        });
    } catch (err) {
        console.log(err)
        dispatch({
            type: SIGNUP_FAIL
        })
    }
}

export const verify = (uid, token) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({ uid, token });
   console.log(body)
    try {
        await axios.post('http://127.0.0.1:8000/auth/users/activation/', body, config);

        dispatch({
            type: ACTIVATION_SUCCESS,
        });
    } catch (err) {
        console.log(err)
        dispatch({
            type: ACTIVATION_FAIL
        })
    }
};

export const load_user = () => async dispatch => {
    console.log("inside load user function")
        if (localStorage.getItem('access')) {
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `JWT ${localStorage.getItem('access')}`,
                    'Accept': 'application/json'
                }
            };

            try {
                const res = await axios.get('http://127.0.0.1:8000/auth/users/me/', config);
        
                dispatch({
                    type: USER_LOADED_SUCCESS,
                    payload: res.data
                });
            } catch (err) {
                dispatch({
                    type: USER_LOADED_FAIL
                });
            }
        } else {
            dispatch({
                type: USER_LOADED_FAIL
            });
        }
};

export const login = (email, password) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json',
        }
    };

    const body = JSON.stringify({ email, password});
    console.log(body);

    try {
        
        const res = await axios.post('http://127.0.0.1:8000/auth/jwt/create/', body, config);

        dispatch({
            type: LOGIN_SUCCESS,
            payload: res.data
        });

        console.log("Auth Success");

        dispatch(load_user());

    } catch (err) {

        console.log(err);
        dispatch({
            type: LOGIN_FAIL
        });
    }
};

export const password_reset = (email) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json',
        }
    };

    const body = JSON.stringify({ email });

    try {
        const res = await axios.post('http://127.0.0.1:8000/auth/users/reset_password/', body, config);
        console.log(res.data)
        dispatch({
            type: RESET_SUCCESS
        });

        console.log(res.data)
    } catch {
        dispatch({
            type: RESET_FAIL
        });
    }
};

export const reset_password_confirm = (uid, token, new_password, new_re_password) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json',
        }
    };

    const body = JSON.stringify({ uid, token, new_password, new_re_password });

    try {
        const res = await axios.post('http://127.0.0.1:8000/auth/users/reset_password_confirm/', body, config);
        console.log(res.data)
        dispatch({
            type: RESET_CONFIRM_SUCCESS
        });
    } catch {
        dispatch({
            type: RESET_CONFIRM_FAIL
        });
    }
}


export const logout = () => dispatch => {
        dispatch( {
            type: LOGOUT
        })
}
