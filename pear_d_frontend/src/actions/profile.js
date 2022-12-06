import axios from 'axios';
import {
    USER_PROFILE_SUCCESS,
    USER_PROFILE_FAILURE
} from './types';
export const getAll = () => async dispatch => {

    console.log("in get all");
    const config = {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `JWT ${localStorage.getItem('access')}`,
        }
    };

    try {
        
        const res = await axios.get('http://127.0.0.1:8000/api/profile/myprofile/view/', config);

        dispatch({
            type: USER_PROFILE_SUCCESS,
            payload: res.data
        });
        console.log(res.data);
  

    } catch (err) {

        console.log(err);
        dispatch({
            type: USER_PROFILE_FAILURE
        });
    }
};