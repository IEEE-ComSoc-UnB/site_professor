import React from 'react';

function Header(props) {
  return (
    <header>
      <div className="container grid-navbar">
        <img
          src="./img/pratica_de_lembrar.png"
          alt="Pratica de lembrar"
          className="logo"
        />
        <ul>
          <li>Quem Somos</li>
          <li>Missão</li>
          <li className="login">Login</li>
        </ul>
      </div>
    </header>
  );
}

export default Header;
