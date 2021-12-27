import React, { useEffect, useState, useRef } from "react";
import { useSelector } from "react-redux";
import { Button, Modal } from "react-bootstrap";

const ErrorModal = (props) => {
    const isInitialMount = useRef(true);
    const [show, setShow] = useState(false);
    const error = useSelector(state => state.error.errorType)

    useEffect(() => {
        if (isInitialMount.current) {
            isInitialMount.current = false
        }
        else {
            setShow(true);
        }
    }, [error])


    const handleClose = () => setShow(false); //error code 초기화 로직 추가해 줄 것
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