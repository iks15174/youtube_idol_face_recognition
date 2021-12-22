import { Route, Switch } from 'react-router'
import { ConnectedRouter } from 'connected-react-router'

function App(props) {
  return (
    <ConnectedRouter history={props.history}>
      {/* <Header /> */}
      <div className="App" >
        <Switch>
          {/* <Route path='/' exact render={() => <React.Fragment><Main /></React.Fragment>} /> */}
          <Route render={() => <h1>Not Found</h1>} />
        </Switch>
      </div >
    </ConnectedRouter>
  );
}

export default App;
