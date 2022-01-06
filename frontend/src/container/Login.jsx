import React, { useState } from "react";
import { useDispatch } from 'react-redux'
import { useHistory } from 'react-router-dom';
import { signin } from "../action/auth";

const Login = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const [email, setEmail] = useState("hi");
    const [password, setPassword] = useState("");
    const [formValid, setFormValid] = useState(false);


    const [emailError, setemailError] = useState("");
    const [passwordError, setpasswordError] = useState("");


    const handleValidation = () => {
        if (!email.match(/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/)) {
            setFormValid(false);
            setemailError("올바르지 않은 이메일 형식 입니다.");
            return
        } else {
            setemailError("");
        }

        if (!password.match(/^[0-9]{4,22}$/)) {
            setFormValid(false);
            setpasswordError(
                "4자리 이상 22자리 이햐의 숫자로 이루어져야 합니다."
            );
            return
        } else {
            setpasswordError("");
        }
        setFormValid(true);
    };

    const loginSubmit = async (e) => {
        e.preventDefault();
        handleValidation();
        if (formValid) {
            try {
                await dispatch(signin(email, password))
                history.push("/")
            }
            catch {

            }
        }
    };

    return (
        <div className="container">
            <div className="row d-flex justify-content-center">
                <div className="col-md-4">
                    <form id="loginform" onSubmit={loginSubmit}>
                        <div className="form-group">
                            <label>Email</label>
                            <input
                                type="email"
                                className="form-control"
                                id="email"
                                name="email"
                                aria-describedby="emailHelp"
                                placeholder="Email"
                                onChange={(event) => setEmail(event.target.value)}
                            />
                            <small id="emailError" className="text-danger form-text">
                                {emailError}
                            </small>
                        </div>
                        <div className="form-group">
                            <label>Password</label>
                            <input
                                type="password"
                                className="form-control"
                                id="password"
                                placeholder="Password"
                                onChange={(event) => setPassword(event.target.value)}
                            />
                            <small id="passworderror" className="text-danger form-text">
                                {passwordError}
                            </small>
                        </div>
                        <button type="submit" className="btn btn-primary mt-1">
                            Submit
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default Login