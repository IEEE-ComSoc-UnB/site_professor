import React from 'react';
import {Component} from 'react';
import {Route, NavLink, HashRouter} from 'react-router-dom';
import Header from './Header';
import PaginaInicial from './PaginaInicial';
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
      <div className="App">
        <Header></Header>
        <PaginaInicial></PaginaInicial>
      </div>
    );
  }
}

export default App;
