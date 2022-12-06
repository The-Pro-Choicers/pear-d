import axios from 'axios';
import {
    REST_DATA_SUCCESS,
    REST_DATA_FAIL
} from './types';


export const getAll = () => async dispatch => {

    console.log("in get all");
    const config = {
        headers: {
            'Content-Type': 'application/json',
        }
    };


    try {

        const res = await axios.get('http://127.0.0.1:8000/api/restaurants/filter/', config);

        dispatch({
            type: REST_DATA_SUCCESS,
            payload: res.data
        });

        console.log("Got Data!");
     
        return res.data;
 

    } catch (err) {

        console.log(err);
        dispatch({
            type: REST_DATA_FAIL
        });
    }
};