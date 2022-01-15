import axios from 'axios';
import { handleError } from '../error';
import {
    JOB_CREATED,
    FOLDER_CREATED,
    GET_FOLDEDRS
} from './faceimageTypes';

export const getFaces = (fileType, link) => async (dispatch, getState) => {
    try {
        const res = await axios.post('face-image/faces/', {
            type : fileType,
            link
        })
        if (res.status === 201) {
            dispatch({
                type: JOB_CREATED,
            })
        }
    } catch (err) {
        dispatch(handleError(err.response.status))
    }
}

export const getFolders = (email, password) => async (dispatch) => {
    try {
        const res = await axios.get('face-image/folders/')
        if (res.status === 200) {
            dispatch({
                type: GET_FOLDEDRS,
            })
        }
    } catch (err) {
        dispatch(handleError(err.response.status))
    }
}

export const makeFolder = (parent, name) => async (dispatch) => {
    try {
        const res = await axios.post('face-image/folders/', {
            parent,
            name,
        })
        if (res.status === 201) {
            dispatch({
                type: FOLDER_CREATED,
            })
        }
    } catch (err) {
        dispatch(handleError(err.response.status))
    }
}