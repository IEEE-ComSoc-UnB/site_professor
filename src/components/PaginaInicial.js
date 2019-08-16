import React from 'react';

const data = new Date();
const ano = data.getFullYear();

const PaginaInicial = props => {
  return (
    <div className="PaginaInicial">
      <div className="container">
        <section>
          <h1>Projeto New Education</h1>
          <h2>Faça parte dessa missão!</h2>
          <p>
            Consectetur maiores blanditiis ipsa iusto adipisci, cumque Ex earum
            iste officiis molestias nobis incidunt Eos sit exercitationem ex
            placeat obcaecati expedita. Exercitationem corporis animi id rerum
            est! Saepe incidunt reprehenderit ea quis pariatur? Qui a
            perferendis laudantium doloribus omnis. Sed adipisci esse sint
            architecto quos, alias, pariatur Ut ut blanditiis!
          </p>
        </section>
        <div className="grid-pagina-inicial">
          <h1>Titulo</h1>
          <p>
            Consectetur saepe nobis veniam magni quibusdam Eum quis facilis
            ipsum culpa eaque Aliquid qui reiciendis soluta inventore
            consectetur! Consectetur obcaecati dolor magni dolore quo? Dolorem
            nobis repellat cupiditate dicta repellendus? Harum deserunt sunt
            sint officiis quod. Praesentium esse asperiores at velit
            reprehenderit corporis Temporibus similique excepturi molestiae eum
            sequi autem autem molestias Nulla rerum dolores earum deleniti
            aperiam! Repudiandae suscipit temporibus iste ad in Reprehenderit
            voluptates rerum quae quod quasi. Harum molestias unde modi natus
            distinctio. Atque voluptas voluptatum vel voluptates numquam Ad a
            veniam architecto error asperiores? Atque eius eveniet pariatur
            tempore sapiente. Laborum officia ratione quisquam explicabo nemo.
          </p>
        </div>
      </div>
      <footer>Prática de Lembrar &copy; {ano}</footer>
    </div>
  );
};

export default PaginaInicial;
