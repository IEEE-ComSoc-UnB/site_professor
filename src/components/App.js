import React from 'react';
import {Component} from 'react';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import Header from './Header';
import PaginaInicial from './PaginaInicial';
import Login from './Login';
import './App.scss';

class App extends Component {
  constructor() {
    super();
    this.state = {};
  }

  // METODOS QUE EU CRIEI

  // LIFECYCLE METHODS

  render() {
    return (
      <Router>
        <div className="App">
          <Header />
          <Switch>
            <Route path="/" exact component={PaginaInicial} />
            <Route path="/login" component={Login} />
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
