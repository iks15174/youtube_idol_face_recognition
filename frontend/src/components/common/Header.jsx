function Header() {
    return (
        <nav class="navbar navbar-expand navbar-light bg-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Navbar</a>
                <ul class="d-flex flex-row-reverse navbar-nav mb-2">
                    <li class="nav-item px-1">
                        <a class="nav-link" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item px-1">
                        <a class="nav-link" href="#">Link</a>
                    </li>
                    <li class="nav-item px-1">
                        <a class="nav-link disabled">Disabled</a>
                    </li>
                </ul>
            </div>
        </nav>
    )
}

export default Header