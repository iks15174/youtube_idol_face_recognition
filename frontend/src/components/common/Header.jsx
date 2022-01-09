import { useSelector } from "react-redux";
import { useHistory } from 'react-router-dom';

function Header() {
    const history = useHistory();
    const isLogin = useSelector(state => state.auth.isAuthenticated)
    return (
        <nav className="mb-5 navbar navbar-expand navbar-light bg-light">
            <div className="container-fluid">
                <a className="navbar-brand" href='#!'>VIDOL</a>
                <ul className="d-flex flex-row-reverse navbar-nav mb-2">
                    <li className="nav-item px-1">
                        <a className="nav-link" aria-current="page" href='#!'>Home</a>
                    </li>
                    {isLogin
                        ? (
                            <>
                                <li className="nav-item px-1">
                                    <a className="nav-link" href='#!'>Logout</a>
                                </li>
                            </>
                        ) : (
                            <>
                                <li className="nav-item px-1">
                                    <a className="nav-link" href='#!' onClick={() => history.push('/login')}>SignIn</a>
                                </li>
                                <li className="nav-item px-1">
                                    <a className="nav-link" href='#!' onClick={() => history.push('/signup')}>SingUp</a>
                                </li>
                            </>
                        )
                    }
                </ul>
            </div>
        </nav>
    )
}

export default Header