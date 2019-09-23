import React from 'react';
import {Link} from 'react-router-dom';

function Header(props) {
  return (
    <header>
      <div className="container grid-navbar">
        <Link to="/" className="logo">
          <img src="./img/pratica_de_lembrar.png" alt="Pratica de lembrar" />
        </Link>
        <ul>
          <li>Quem Somos</li>
          <li>Missão</li>
          <Link to="/login">
            <li className="login">Login</li>
          </Link>
        </ul>
        <p className="hamburguer">&#9776;</p>
      </div>
    </header>
  );
}

export default Header;
