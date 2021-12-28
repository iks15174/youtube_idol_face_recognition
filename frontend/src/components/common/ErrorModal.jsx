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
        }
    }, [error])


    const handleClose = () => {
        setShow(false)
        dispatch(cleanError())
    };
    return (
        <>
            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Error</Modal.Title>
                </Modal.Header>
                <Modal.Body>{error}</Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Close
                    </Button>
                </Modal.Footer>
            </Modal>
        </>
    )
}

export default ErrorModal