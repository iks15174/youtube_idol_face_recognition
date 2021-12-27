import {
    LOGIN_FAIL,
    LOGIN_SUCCESS,
    LOGOUT_SUCCESS,
} from '../action/authTypes'

const initialState = {
    isAuthenticated: false,
}

export default function authReducer(state = initialState, action) {
    switch (action.type) {
        case LOGIN_SUCCESS:
            return {
                ...state,
                isAuthenticated: true
            };
        case LOGIN_FAIL:
        case LOGOUT_SUCCESS:
            return {
                ...state,
                isAuthenticated: false
            }
        default:
            return state;
    }

}