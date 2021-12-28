import React, { useState } from "react";
import { useDispatch } from 'react-redux'
import { signup } from "../action/auth";

const Signup = (props) => {
    const dispatch = useDispatch();

    const [nickName, setNickName] = useState("");
    const [email, setEmail] = useState("hi");
    const [password, setPassword] = useState("");
    const [rePassword, setRePassword] = useState("");
    const [formValid, setFormValid] = useState(false);


    const [nickNameError, setNickNameError] = useState("");
    const [emailError, setemailError] = useState("");
    const [passwordError, setpasswordError] = useState("");
    const [rePasswordError, setRePasswordError] = useState("");


    const handleValidation = () => {
        if (!nickName.match(/^[0-9A-Za-z가-힣]{2,22}$/)) {
            setFormValid(false);
            setNickNameError(
                "2자리 이상 22자리 이햐의 숫자&문자로 이루어져야 합니다."
            );
            return
        } else {
            setNickNameError("");
        }

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

    const handleRePwd = () => {
        if (password !== rePassword) {
            setFormValid(false);
            setRePasswordError("비밀번호가 일치하지 않습니다.");
        }
        else {
            setRePasswordError("")
            setFormValid(true);
        }
    }

    const signupSubmit = (e) => {
        e.preventDefault();
        handleValidation();
        handleRePwd();
        if (formValid) {
            dispatch(signup(email, nickName, password))
        }
    };

    return (
        <div className="container">
            <div className="row d-flex justify-content-center">
                <div className="col-md-4">
                    <form id="loginform" onSubmit={signupSubmit}>
                        <div className="form-group">
                            <label>Nick name</label>
                            <input
                                type="text"
                                className="form-control"
                                id="nickName"
                                name="nickName"
                                aria-describedby="nameHelp"
                                placeholder="Nick Name"
                                onChange={(event) => setNickName(event.target.value)}
                            />
                            <small id="nickNameError" className="text-danger form-text">
                                {nickNameError}
                            </small>
                        </div>
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
                        <div className="form-group">
                            <label>Re-password</label>
                            <input
                                type="password"
                                className="form-control"
                                id="rePassword"
                                placeholder="Re-Password"
                                onChange={(event) => setRePassword(event.target.value)}
                            />
                            <small id="rePassworderror" className="text-danger form-text">
                                {rePasswordError}
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

export default Signup