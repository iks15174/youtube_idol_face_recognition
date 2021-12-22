import {
    LOGIN_FAIL,
    LOGIN_SUCCESS,
    LOGOUT_SUCCESS,
    GET_USERS
} from '../action/types'

const initialState = {
    isAuthenticated: false,
    user: null,
}

export default function (state = initialState, action) {
    switch (action.type) {
        case LOGIN_SUCCESS:
            return {
                ...state,
                user: { ...action.payload },
                isAuthenticated: true
            };
        case LOGIN_FAIL:
        case LOGOUT_SUCCESS:
            return {
                ...state,
                user: null,
                isAuthenticated: false
            }
        default:
            return state;
    }

}