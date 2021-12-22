import axios from 'axios';

import {
    LOGIN_SUCCESS,
    LOGOUT_SUCCESS,
} from './types';
export const loadUser = () => (dispatch, getState) => {
    let user = JSON.parse(localStorage.getItem('user'))
    if (user) {
        axios
            .get(`/api/user/${user.id}`)
            .then((res) => {
                if (res.data.logged_in) {
                    delete res.data['password']
                    dispatch({
                        type: LOGIN_SUCCESS,
                        payload: res.data,
                    });
                }
                else {
                    dispatch({
                        type: LOGOUT_SUCCESS,
                    });
                }
            })
            .catch((err) => {
                console.log('loadUsers Error');
            });
    }
}