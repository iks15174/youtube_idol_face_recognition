import {
    CLEAN_ERROR,
    ERROR_400,
    ERROR_401,
    ERROR_403,
    ERROR_404,
    ERROR_405,
    ERROR_500,
    ERROR_OTHER
} from './errorTypes';

export const handleError = (errorCode) => {
    switch (errorCode) {
        case 400:
            return { type: ERROR_400 }
        case 401:
            return { type: ERROR_401 }
        case 403:
            return { type: ERROR_403 }
        case 404:
            return { type: ERROR_404 }
        case 405:
            return { type: ERROR_405 }
        case 500:
            return { type: ERROR_500 }
        default:
            return { type: ERROR_OTHER }

    }
}

export const cleanError = () => {
    return { type: CLEAN_ERROR }
}