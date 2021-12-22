import React from 'react'
import { Route, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';

const PrivateRoute = ({ component, auth, ...rest }) => {
    return (
        <Route
            {...rest}
            render={(props) => {
                if (!auth.isAuthenticated) {
                    return <Redirect to="/login" />;
                } else {
                    return <component {...props} />;
                }
            }}
        />
    )
}

const mapStateToProps = (state) => {
    return {
        auth: state.auth,
    }
}
export default connect(mapStateToProps)(PrivateRoute);
