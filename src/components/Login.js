import React from 'react';
import Footer from './Footer';

function Login(props) {
  return (
    <div>
      <div className="Login">
        <form method="post">
          <h1>Login</h1>
          <input type="email" placeholder="email" />
          <br />
          <input type="password" placeholder="senha" />
        </form>
        <button className="login">Login</button>
        <button className="criar_conta">Criar conta</button>
      </div>
      <Footer taEmbaixo="true" />
    </div>
  );
}

export default Login;
