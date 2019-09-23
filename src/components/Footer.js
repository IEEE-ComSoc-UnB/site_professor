import React from 'react';

const data = new Date();
const ano = data.getFullYear();

const bottom = {
  position: 'absolute',
  left: 0,
  right: 0,
  bottom: 0,
};

function Footer(props) {
  return (
    <div className="Footer">
      <footer>Prática de Lembrar &copy; {ano}</footer>
    </div>
  );
}

export default Footer;
