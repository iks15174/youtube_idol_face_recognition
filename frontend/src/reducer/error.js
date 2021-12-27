import {
    ERROR_400,
    ERROR_401,
    ERROR_403,
    ERROR_404,
    ERROR_405,
    ERROR_500,
    ERROR_OTHER,
    CLEAN_ERROR
} from '../action/errorTypes';

const initialState = {
    errorType: "",
    errorMessage: "",
}

const errorTypes = [ERROR_400, ERROR_401, ERROR_403, ERROR_404, ERROR_405, ERROR_500, ERROR_OTHER]

export default function errorReducer(state = initialState, action) {
    if (errorTypes.includes(action.type)) {
        return {
            ...state,
            errorType: action.type
        }
    }
    else if (action.type === CLEAN_ERROR) {
        return {
            ...state,
            errorType: ""
        }
    }
    else {
        return state
    }

}