import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Button, Modal } from "react-bootstrap";
import { cleanError } from "../../action/error";

const ErrorModal = (props) => {
    const dispatch = useDispatch();
    const [show, setShow] = useState(false);
    const error = useSelector(state => state.error.errorType)

    useEffect(() => {
        if (error) {
            setShow(true)
            dispatch(cleanError())
        }
    }, [error])


    const handleClose = () => setShow(false); //error code 초기화 로직 추가해
    return (
        <>
            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Modal heading</Modal.Title>
                </Modal.Header>
                <Modal.Body>Woohoo, you're reading this text in a modal!</Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Close
                    </Button>
                    <Button variant="primary" onClick={handleClose}>
                        Save Changes
                    </Button>
                </Modal.Footer>
            </Modal>
        </>
    )
}

export default ErrorModal