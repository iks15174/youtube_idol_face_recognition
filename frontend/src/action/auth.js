import axios from 'axios';
import { handleError } from './error';
import {
    LOGIN_SUCCESS,
    SIGNUP_SUCCESS,
} from './authTypes';

export const isLogin = () => async (dispatch, getState) => {
    try {
        const res = await axios.get('account/islogin/')
        if (res.status === 204) {
            dispatch({
                type: LOGIN_SUCCESS,
            })
        }
    } catch (err) {
        if (err.response.status !== 401) dispatch(handleError(err.response.status))
    }
}

export const signin = (email, password) => async (dispatch) => {
    try {
        const res = await axios.post('account/signin/', {
            email,
            password
        })
        if (res.status === 204) {
            dispatch({
                type: LOGIN_SUCCESS,
            })
        }
    } catch (err) {
        dispatch(handleError(err.response.status))
    }
}

export const signup = (email, nickName, password) => async (dispatch) => {
    try {
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
        dispatch(handleError(err.response.status))
    }
}


export const token = () => async (dispatch, getState) => {
    try {
        await axios.get('account/token/')
    } catch (err) {
        dispatch(handleError(err.response.status))
    }
}