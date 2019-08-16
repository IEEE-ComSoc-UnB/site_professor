import React from 'react';
import {Component} from 'react';

class App extends Component {
  constructor() {
    super();
    this.state = {nome: '', telefone: 123, temFilhos: true};
  }

  // METODOS QUE EU CRIEI

  // LIFECYCLE METHODS

  render() {
    return (
      <div className="App">
        <h1>oi</h1>
      </div>
    );
  }
}

export default App;
