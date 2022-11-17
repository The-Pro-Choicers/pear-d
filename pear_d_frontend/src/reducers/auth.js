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
    RESET_SUCCESS,
    RESET_CONFIRM_FAIL,
    RESET_CONFIRM_SUCCESS,
    LOGOUT
} from '../actions/types';

const initialState = {
    access: localStorage.getItem('access'),
    refresh: localStorage.getItem('refresh'),
    isAuthenticated: null,
    user: null
};


export default function(state = initialState, action) {
    const { type, payload } = action;
    switch(type) {
        case AUTHENTICATED_SUCCESS:
            return {
                ...state,
                isAuthenticated: true
            }
        case SIGNUP_SUCCESS:
            return {
                ...state,
                isAuthenticated: false
            }
        case LOGIN_SUCCESS:
            localStorage.setItem('access', payload.access);
            return {
               ...state,
               isAuthenticated: true,
               access: payload.access,
               refresh: payload.refresh
            }
        case USER_LOADED_SUCCESS:
            return {
                ...state,
                user: payload
            }
        case AUTHENTICATED_FAIL:
            return {
                ...state,
                isAuthenticated: false
        }
        case USER_LOADED_FAIL:
            return {
                ...state,
                user: null
            }   
        case SIGNUP_FAIL:
        case LOGIN_FAIL:
        case LOGOUT:
            localStorage.removeItem('access');
            localStorage.removeItem('refresh');
            return {
               ...state,
               access: null,
               refresh: null,
               isAuthenticated: false,
               user: null
            }
        case ACTIVATION_SUCCESS:
        case ACTIVATION_FAIL:
            return {
                ...state
            }
        case RESET_SUCCESS:
        case RESET_CONFIRM_FAIL:
        case RESET_CONFIRM_SUCCESS:
        case RESET_CONFIRM_FAIL:
            return {
                ...state
            }
        default:
            return state
    }
}