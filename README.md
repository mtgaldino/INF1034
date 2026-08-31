<h1 align="center">INF1034 — Práticas de Programação</h1>

<p align="center">
  Repositório individual de atividades da disciplina <strong>Práticas de Programação (INF1034)</strong>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Biblioteca-Turtle-brightgreen" alt="Turtle">
  <img src="https://img.shields.io/badge/Status-Em%20andamento-yellow" alt="Status">
</p>

<hr>

<h2>📌 Sobre o repositório</h2>

<p>
  Este repositório reúne as atividades práticas desenvolvidas ao longo da disciplina
  de <strong>Ciência da Computação</strong>, incluindo exercícios de fixação com a
  biblioteca <code>turtle</code> do Python e demais entregas propostas em sala de aula.
</p>

<h2>👤 Autor</h2>

<table>
  <tr>
    <td><strong>Nome</strong></td>
    <td>Matheus Galdino</td>
  </tr>
  <tr>
    <td><strong>Curso</strong></td>
    <td>Ciência da Computação</td>
  </tr>
  <tr>
    <td><strong>Disciplina</strong></td>
    <td>INF1034 — Práticas de Programação</td>
  </tr>
  <tr>
    <td><strong>Instituição</strong></td>
    <td>PUC-RIO</td>
  </tr>
  <tr>
    <td><strong>Período</strong></td>
    <td>2026.2</td>
  </tr>
</table>

<h2>🗂️ Estrutura do repositório</h2>

<pre>
.
├── atividade-2.1/
│   └── main.py
├── atividade-2.2/
│   ├── austria.py
│   ├── chile.py
│   ├── estados_unidos.py
│   ├── islandia.py
│   ├── israel.py
│   ├── italia.py
│   ├── japao.py
│   ├── monaco.py
│   ├── polonia.py
│   ├── suica.py
│   ├── turquia.py
│   └── africa_do_sul.py
└── README.md
</pre>

<h2>🧭 Atividade 2.1 — Formas geométricas com Turtle</h2>

<p>
  Exercício introdutório de fixação com a biblioteca <code>turtle</code>,
  trabalhando movimentação, repetição (<code>for</code>) e preenchimento de
  cores. O script desenha:
</p>

<ul>
  <li>O plano cartesiano (eixos X e Y) como referência visual</li>
  <li>Uma estrela de 5 pontas</li>
  <li>Um hexágono</li>
  <li>Um triângulo</li>
  <li>Um pentágono</li>
  <li>Uma espiral (desafio extra)</li>
</ul>

<p>
  Cada forma é posicionada em um quadrante diferente do plano cartesiano,
  usando <code>t.pu()</code> / <code>t.pd()</code> para reposicionar a
  tartaruga sem deixar rastro entre um desenho e outro.
</p>

<h2>🚩 Atividade 2.2 — Bandeiras com Turtle</h2>

<p>
  Implementação de bandeiras de diferentes países utilizando a biblioteca
  <code>turtle</code> do Python, somando um total de <strong>500XP</strong>
  conforme os critérios da atividade:
</p>

<table>
  <thead>
    <tr>
      <th>Categoria</th>
      <th>Bandeiras</th>
      <th>XP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>🟢 Fácil (25XP)</td>
      <td>Áustria, Japão, Polônia, Itália, Mônaco, Suíça</td>
      <td>150</td>
    </tr>
    <tr>
      <td>🟡 Médio (50XP)</td>
      <td>Turquia, Islândia, Israel, Chile</td>
      <td>200</td>
    </tr>
    <tr>
      <td>🔴 Difícil (75XP)</td>
      <td>África do Sul, Estados Unidos</td>
      <td>150</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="2" align="right"><strong>Total</strong></td>
      <td><strong>500</strong></td>
    </tr>
  </tfoot>
</table>

<blockquote>
  A bandeira da <strong>Áustria</strong> foi implementada utilizando uma função
  diferente para cada forma geométrica, recebendo a cor como parâmetro,
  conforme exigido no enunciado da atividade.
</blockquote>

<h2>▶️ Como executar</h2>

<p>Cada bandeira é um arquivo <code>.py</code> independente. Para executar, é necessário ter o Python instalado (a biblioteca <code>turtle</code> já vem por padrão).</p>

<pre>
git clone [URL_DESTE_REPOSITORIO]
cd atividade-2.2
python nome_da_bandeira.py
</pre>

<p>Uma janela gráfica será aberta com o desenho da bandeira. Clique nela para fechar.</p>

<h2>🛠️ Tecnologias utilizadas</h2>

<ul>
  <li>Python 3</li>
  <li>Módulo <code>turtle</code> (nativo do Python)</li>
</ul>

<hr>

<p align="center"><sub>Repositório mantido para fins acadêmicos — INF1034, Práticas de Programação.</sub></p>
