import React, { useEffect } from 'react';
import { Route, Switch } from 'react-router'
import { ConnectedRouter } from 'connected-react-router'
import { useDispatch } from 'react-redux'

import { token, isLogin } from './action/auth/auth';


import Signup from './container/Signup';
import Login from './container/Login';
import Main from './container/Main';
import Mypage from './container/Mypage';
import Header from './components/common/Header';
import ErrorModal from './components/common/ErrorModal';

function App(props) {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(token())
    dispatch(isLogin())
  });

  return (
    <React.Fragment>
      <ErrorModal></ErrorModal>
      <ConnectedRouter history={props.history}>
        <Header />
        <div className="App" >
          <Switch>
            <Route path='/' exact render={() => <React.Fragment><Main /></React.Fragment>} />
            <Route path='/signup' exact render={() => <React.Fragment><Signup /></React.Fragment>} />
            <Route path='/login' exact render={() => <React.Fragment><Login /></React.Fragment>} />
            <Route path='/mypage' exact render={() => <React.Fragment><Mypage /></React.Fragment>} />
            <Route render={() => <h1>Not Found</h1>} />
          </Switch>
        </div>
      </ConnectedRouter>
    </React.Fragment>
  );
}

export default App;
