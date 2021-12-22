import React from 'react';
import { Route, Switch } from 'react-router'
import { ConnectedRouter } from 'connected-react-router'
import styled from "styled-components";

import Signup from './container/Signup'
import Header from './components/common/Header'

const styledDiv = styled.div`
  width: 100%;
  height: 100%
`

function App(props) {
  return (
    <ConnectedRouter history={props.history}>
      <Header />
      <styledDiv className="App" >
        <Switch>
          <Route path='/signup' exact render={() => <React.Fragment><Signup /></React.Fragment>} />
          <Route render={() => <h1>Not Found</h1>} />
        </Switch>
      </styledDiv >
    </ConnectedRouter>
  );
}

export default App;
