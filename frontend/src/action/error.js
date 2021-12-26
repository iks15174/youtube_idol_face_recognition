import axios from 'axios';

import {
    ERROR_400,
    ERROR_401,
    ERROR_403,
    ERROR_404,
    ERROR_405,
    ERROR_500,
    ERROR_OTHER
} from './errorTypes';

export const handleError = (errorCode, dispatch) => {
    switch (errorCode) {
        case 400:
            dispatch({ type: ERROR_400 })
            break;
        case 401:
            dispatch({ type: ERROR_401 })
            break;
        case 403:
            dispatch({ type: ERROR_403 })
            break;
        case 404:
            dispatch({ type: ERROR_404 })
            break;
        case 405:
            dispatch({ type: ERROR_405 })
            break;
        case 500:
            dispatch({ type: ERROR_500 })
            break;
        default:
            dispatch({ type: ERROR_OTHER })

    }
}