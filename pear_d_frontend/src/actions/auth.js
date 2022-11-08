import axios from 'axios';
import {
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    USER_LOADED_SUCCESS,
    USER_LOADED_FAIL
} from './types';

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
                const res = await axios.get(`${process.env.PEARD_API_URL}/auth/users/me/`, config);
        
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

        console.log(res)
        console.log(res.data)
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
