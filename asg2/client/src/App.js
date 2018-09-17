import React, { Component } from 'react';
import './App.css';
import Import from './Components/Import'

class App extends Component {
  render() {
    return (
      <div className="container" style={{border: '1px solid blue'}}>

        <div className="row" style={{margin:'10px', border: '1px solid red'}}>
          <div className="col-12">
            <h1 align="center">COMP9321</h1>
          </div>
        </div>


        <div className="row" style={{margin:'10px', border: '1px solid red'}}>
          <div className="col-6">
            <Import/>
          </div>
        </div>

      </div>
    );
  }
}

export default App;
