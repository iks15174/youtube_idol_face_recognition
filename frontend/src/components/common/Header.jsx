function Header() {
    return (
        <nav className="mb-5 navbar navbar-expand navbar-light bg-light">
            <div className="container-fluid">
                <a className="navbar-brand" href="#">VIDOL</a>
                <ul className="d-flex flex-row-reverse navbar-nav mb-2">
                    <li className="nav-item px-1">
                        <a className="nav-link" aria-current="page" href="#">Home</a>
                    </li>
                    <li className="nav-item px-1">
                        <a className="nav-link" href="#">SignIn</a>
                    </li>
                    <li className="nav-item px-1">
                        <a className="nav-link">SingUp</a>
                    </li>
                </ul>
            </div>
        </nav>
    )
}

export default Header