import React from 'react';
import { Route, Switch } from 'react-router'
import { ConnectedRouter } from 'connected-react-router'

import Signup from './container/Signup'
import Header from './components/common/Header'

function App(props) {
  return (
    <ConnectedRouter history={props.history}>
      <Header />
      <div className="App" >
        <Switch>
          <Route path='/signup' exact render={() => <React.Fragment><Signup /></React.Fragment>} />
          <Route render={() => <h1>Not Found</h1>} />
        </Switch>
      </div>
    </ConnectedRouter>
  );
}

export default App;
