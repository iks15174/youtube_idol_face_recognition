import {
    ERROR_400,
    ERROR_401,
    ERROR_403,
    ERROR_404,
    ERROR_405,
    ERROR_500,
    ERROR_OTHER
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
    else {
        return state
    }

}