import axios from 'axios';
import { handleError } from './error';
import {
    LOGIN_SUCCESS,
    LOGOUT_SUCCESS,
    SIGNUP_SUCCESS,
} from './authTypes';

export const signin = () => async (dispatch, getState) => {
    try {
        const res = await axios.post('account/signin/')
        if (res.status === 204) {
            dispatch({
                type: LOGIN_SUCCESS,
            })
        }
    } catch (err) {
        console.log(err.response.status)
    }
}

export const signup = (email, nickName, password) => async (dispatch, getState) => {
    try {
        const error = new Error("message");
        error.response = { status: 400 }
        throw error;
        const res = await axios.post('account/signup/', {
            email,
            nickName,
            password
        })
        if (res.status === 201) {
            dispatch({
                type: SIGNUP_SUCCESS,
            })
        }
    } catch (err) {
        handleError(err.response.status, dispatch)
    }
}


export const token = () => async (dispatch, getState) => {
    try {
        const res = await axios.get('account/token/')
    } catch (err) {
        console.log(err)
    }
}