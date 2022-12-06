import axios from 'axios';
import Cookies from 'js-cookie';
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


export const filterRestaurants = (food, env, phil, min, price) => async dispatch => {

    console.log("in filter restaurants");
    const config = {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
    };


    try {

        if (!env) {
            env = 0
        } else {
            env = 1
        }

        if (!min) {
            min = 0
        } else {
            min = 1
        }

        if (!phil) {
            phil = 0
        } else {
            phil = 1
        }

        console.log(food,env,phil,min,price)
        
        const res = await axios.get(`http://127.0.0.1:8000/api/restaurants/filter/fc${food}e${env}ph${phil}m${min}p${price}/`, config);

        dispatch({
            type: REST_DATA_SUCCESS,
            payload: res.data
        });

        console.log("Filtered Data!");
        console.log(res);
        return res.data;
  

    } catch (err) {

        console.log(err);
        dispatch({
            type: REST_DATA_FAIL
        });
    }
};

export const addFav = (id) => async dispatch => {

    const config = {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `JWT ${localStorage.getItem('access')}`,
            'Accept': 'application/json',
            'X-CSRFToken': Cookies.get('csrftoken'),
        }
    };

    const body = {
        "restaurant_id": id
    };


    try {
        
        const res = await axios.put('http://127.0.0.1:8000/api/profile/myprofile/favorites/add/', body, config);

        dispatch({
            type: REST_DATA_SUCCESS,
            payload: res.data
        });

        console.log("Got Data!");
  

    } catch (err) {

        console.log(err);
        dispatch({
            type: REST_DATA_FAIL
        });
    }
};


export const removeFav = (id) => async dispatch => {

    const config = {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `JWT ${localStorage.getItem('access')}`,
            'Accept': 'application/json',
            'X-CSRFToken': Cookies.get('csrftoken'),
        }
    };


    try {
        
        const res = await axios.get(`http://127.0.0.1:8000/api/profile/myprofile/favorites/delete/${id}/`, config);

        dispatch({
            type: REST_DATA_SUCCESS,
            payload: res.data
        });

        console.log(res.data);
  

    } catch (err) {

        console.log(err);
        dispatch({
            type: REST_DATA_FAIL
        });
    }
};